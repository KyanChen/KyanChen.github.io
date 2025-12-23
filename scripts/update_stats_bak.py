import os
import time
import yaml
import difflib
import requests
from bs4 import BeautifulSoup

# --- 配置项 ---
FILE_PATH = '_data/publications.yml'
FUZZY_THRESHOLD = 0.85
PAGE_SIZE = 100
# 请将 Key 和 ID 放入环境变量，或在此处填入
SCRAPER_API_KEY = os.getenv("SCRAPER_API_KEY", "YOUR_SCRAPER_API_KEY")
SCHOLAR_ID = os.getenv("GOOGLE_SCHOLAR_ID", "YOUR_GOOGLE_SCHOLAR_ID")

def fetch_scholar_data(api_key, scholar_id):
    """抓取指定学者的所有文章数据及总引用数"""
    session = requests.Session()
    base_url = "https://api.scraperapi.com/"
    all_articles = {}
    total_cites = 0
    cstart = 0

    print(f"🚀 Starting fetch for Scholar ID: {scholar_id}")

    while True:
        target_url = f"https://scholar.google.com/citations?user={scholar_id}&hl=en&cstart={cstart}&pagesize={PAGE_SIZE}"
        params = {
            'api_key': api_key, 
            'url': target_url,
            'country': 'us',
            'device_type': 'desktop', # 建议加上这个以保证获取桌面版页面
        }
        
        print(f"☁️ [Page {cstart // PAGE_SIZE + 1}] Requesting data...")
        
        try:
            resp = session.get(base_url, params=params, timeout=60)
            if resp.status_code != 200:
                print(f"❌ API Error: {resp.status_code}")
                break
            
            soup = BeautifulSoup(resp.text, 'html.parser')
            
            # 1. 获取总引用数
            if total_cites == 0:
                # 兼容 table 和 div 查找
                stats = soup.find(id='gsc_rsb_st')
                if stats:
                    cites_td = stats.find_all('td', class_='gsc_rsb_std')
                    if cites_td:
                        total_cites = int(cites_td[0].text.strip())

            # 2. 解析文章列表
            rows = soup.find_all('tr', class_='gsc_a_tr')
            if not rows:
                print("✅ No more articles found. Finished.")
                break

            for row in rows:
                try:
                    title_tag = row.find('a', class_='gsc_a_at')
                    cite_tag = row.find('a', class_='gsc_a_ac')
                    
                    if not title_tag: continue
                    
                    title = title_tag.text.strip()
                    cites = int(cite_tag.text.strip()) if cite_tag and cite_tag.text.strip().isdigit() else 0
                    
                    # 提取 Paper ID
                    href = title_tag.get('href', '')
                    paper_id = href.split('citation_for_view=')[-1] if 'citation_for_view=' in href else ''

                    all_articles[title.lower()] = {'cited_by': cites, 'id': paper_id}
                except Exception:
                    continue

            count = len(rows)
            print(f"   🧩 Parsed {count} articles.")
            
            if count < PAGE_SIZE:
                print("✅ Reached last page.")
                break

            cstart += PAGE_SIZE
            time.sleep(1) # 避免请求过快

        except Exception as e:
            print(f"❌ Network/Parse Error: {e}")
            break

    print(f"📊 Fetch Summary: {len(all_articles)} articles, {total_cites} total citations.")
    return all_articles, total_cites

def find_match(title, scholar_map):
    """在抓取的数据中模糊匹配标题"""
    if not title or not scholar_map: return None
    key = title.lower().strip()
    
    # 精确匹配
    if key in scholar_map:
        return scholar_map[key]
    
    # 模糊匹配
    matches = difflib.get_close_matches(key, scholar_map.keys(), n=1, cutoff=FUZZY_THRESHOLD)
    return scholar_map[matches[0]] if matches else None

def update_yaml():
    if not SCRAPER_API_KEY or not SCHOLAR_ID:
        print("❌ Configuration missing: API Key or Scholar ID not set.")
        return

    # 1. 获取最新数据
    scholar_data, fetched_total_cites = fetch_scholar_data(SCRAPER_API_KEY, SCHOLAR_ID)
    if not scholar_data:
        print("⚠️ No data fetched. Aborting.")
        return

    # 2. 读取本地 YAML
    if not os.path.exists(FILE_PATH):
        print(f"❌ File not found: {FILE_PATH}")
        return

    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f) or {}
    except Exception as e:
        print(f"❌ Error reading YAML: {e}")
        return

    # 兼容 items 列表或根字典结构
    pubs = data.get('items', data) if isinstance(data, dict) else data
    if not isinstance(pubs, list):
        print("❌ YAML format error: expected a list of publications.")
        return

    updates = 0
    not_found_list = [] # 用于存储未匹配到的论文

    # 3. 更新总引用数
    if isinstance(data, dict) and fetched_total_cites > 0:
        if data.get('total_cited_by') != fetched_total_cites:
            print(f"📈 Updating total citations: {data.get('total_cited_by')} -> {fetched_total_cites}")
            data['total_cited_by'] = fetched_total_cites
            updates += 1

    # 4. 更新单篇文章
    for pub in pubs:
        title = pub.get('title')
        match = find_match(title, scholar_data)
        
        if match:
            # 匹配成功：更新数据
            old_cite = pub.get('cited_by', 0)
            new_cite = match['cited_by']
            if old_cite != new_cite:
                print(f"📄 '{title[:20]}...': {old_cite} -> {new_cite}")
                pub['cited_by'] = new_cite
                updates += 1
            
            if match['id'] and match['id'] != pub.get('google_scholar_id'):
                pub['google_scholar_id'] = match['id']
                updates += 1
        else:
            # 匹配失败：加入未找到列表
            not_found_list.append(title)

    # 5. 保存更改
    if updates > 0:
        try:
            with open(FILE_PATH, 'w', encoding='utf-8') as f:
                yaml.dump(data, f, sort_keys=False, default_flow_style=False, allow_unicode=True)
            print(f"✅ Successfully saved {updates} updates.")
        except Exception as e:
            print(f"❌ Error saving file: {e}")
    else:
        print("ℹ️ No changes detected in file.")

    # 6. 打印未被更新（未找到）的论文
    if not_found_list:
        print("\n" + "="*40)
        print(f"⚠️  WARNING: {len(not_found_list)} Papers NOT Found in Google Scholar Data")
        print("="*40)
        for i, t in enumerate(not_found_list, 1):
            print(f"{i}. {t}")
        print("="*40 + "\n")

if __name__ == "__main__":
    update_yaml()
