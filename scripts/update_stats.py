import os
import time
import yaml
import difflib
import requests
import urllib.parse
from bs4 import BeautifulSoup

# --- 配置项 / Configuration ---
FILE_PATH = '_data/publications.yml'
FUZZY_THRESHOLD = 0.85
PAGE_SIZE = 100

# 环境变量 (Environment Variables)
SCRAPER_API_KEY = os.getenv("SCRAPER_API_KEY", "YOUR_SCRAPER_API_KEY") # Primary API
SCRAPE_DO_API_KEY = os.getenv("SCRAPE_DO_API_KEY", "YOUR_SCRAPE_DO_TOKEN") # Backup API
SCHOLAR_ID = os.getenv("GOOGLE_SCHOLAR_ID", "YOUR_GOOGLE_SCHOLAR_ID")


# --- 1. 网络请求层 (Network Layer) ---

def fetch_with_scraperapi(target_url):
    """
    尝试使用 ScraperAPI 获取页面
    """
    if not SCRAPER_API_KEY or "YOUR_" in SCRAPER_API_KEY:
        print("⚠️ ScraperAPI Key not configured.")
        return None

    base_url = "https://api.scraperapi.com/"
    params = {
        'api_key': SCRAPER_API_KEY,
        'url': target_url,
        'country': 'us',
        'device_type': 'desktop', 
    }
    
    print(f"   🔹 Trying ScraperAPI...")
    try:
        response = requests.get(base_url, params=params, timeout=30)
        if response.status_code == 200:
            return response.text
        else:
            print(f"   ⚠️ ScraperAPI failed with status: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"   ⚠️ ScraperAPI Connection Error: {e}")
        return None

def fetch_with_scrape_do(target_url):
    """
    尝试使用 Scrape.do 获取页面 (Backup)
    """
    if not SCRAPE_DO_API_KEY or "YOUR_" in SCRAPE_DO_API_KEY:
        print("⚠️ Scrape.do API Token not configured.")
        return None

    # URL Encoding the target URL
    encoded_target = urllib.parse.quote(target_url)
    url = "http://api.scrape.do/?token={}&url={}&geoCode=us&device=desktop".format(SCRAPE_DO_API_KEY, encoded_target)
    
    print(f"   🔸 Switching to Scrape.do (Backup)...")
    try:
        response = requests.get(url, timeout=60)
        if response.status_code == 200:
            return response.text
        else:
            print(f"   ❌ Scrape.do failed with status: {response.status_code}")
            print(f"   Response: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"   ❌ Scrape.do Connection Error: {e}")
        return None

def get_page_html(target_url):
    """
    统一获取 HTML 的入口函数。
    逻辑：优先 ScraperAPI -> 失败/超时 -> Scrape.do
    """
    # 1. 尝试主要 API
    html = fetch_with_scraperapi(target_url)
    
    # 2. 如果主要 API 失败，尝试备用 API
    if not html:
        html = fetch_with_scrape_do(target_url)
        
    return html

# --- 2. 解析层 (Parsing Layer) ---

def parse_scholar_page(html):
    """
    解析 Google Scholar 的 HTML 页面
    返回: (articles_dict, total_cites_found_on_page)
    """
    if not html: return {}, 0
    
    soup = BeautifulSoup(html, 'html.parser')
    page_articles = {}
    total_cites = 0

    # A. 获取总引用数 (通常只会在第一页解析到，但每次检查也无妨)
    stats = soup.find(id='gsc_rsb_st')
    if stats:
        cites_td = stats.find_all('td', class_='gsc_rsb_std')
        if cites_td:
            try:
                total_cites = int(cites_td[0].text.strip())
            except ValueError:
                pass

    # B. 解析文章列表
    rows = soup.find_all('tr', class_='gsc_a_tr')
    for row in rows:
        try:
            title_tag = row.find('a', class_='gsc_a_at')
            cite_tag = row.find('a', class_='gsc_a_ac')
            
            if not title_tag: continue
            
            title = title_tag.text.strip()
            # 解析引用数，如果为空或 * 则设为 0
            cite_text = cite_tag.text.strip() if cite_tag else ""
            cites = int(cite_text) if cite_text.isdigit() else 0
            
            # 提取 Paper ID (citation_for_view 参数)
            href = title_tag.get('href', '')
            paper_id = ""
            if 'citation_for_view=' in href:
                # href 类似于 /citations?view_op=...&citation_for_view=USER_ID:PAPER_ID
                paper_id = href.split('citation_for_view=')[-1]

            page_articles[title.lower()] = {
                'title': title, # 保存原标题用于显示
                'cited_by': cites, 
                'id': paper_id
            }
        except Exception as e:
            print(f"   ⚠️ Error parsing row: {e}")
            continue
            
    return page_articles, total_cites

def fetch_all_scholar_data(scholar_id):
    """
    循环抓取所有分页数据
    """
    all_articles = {}
    max_total_cites = 0
    cstart = 0

    print(f"🚀 Starting fetch for Scholar ID: {scholar_id}")

    while True:
        print(f"☁️ [Page {cstart // PAGE_SIZE + 1}] Requesting data (start={cstart})...")
        
        target_url = f"https://scholar.google.com/citations?user={scholar_id}&cstart={cstart}&pagesize={PAGE_SIZE}"
        
        # 获取 HTML (包含自动切换 API 逻辑)
        html = get_page_html(target_url)
        
        if not html:
            print("❌ Failed to retrieve data from both APIs. Stopping.")
            break

        # 解析数据
        page_articles, page_total_cites = parse_scholar_page(html)
        
        # 更新总引用数 (取最大值，防止某一页解析失败导致归零)
        if page_total_cites > max_total_cites:
            max_total_cites = page_total_cites

        if not page_articles:
            print("✅ No articles found on this page. Reached end.")
            break

        # 合并文章数据
        all_articles.update(page_articles)
        
        count = len(page_articles)
        print(f"   🧩 Parsed {count} articles.")

        # 如果当前页获取的文章数少于 PAGE_SIZE，说明是最后一页
        if count < PAGE_SIZE:
            print("✅ Reached last page.")
            break

        cstart += PAGE_SIZE
        time.sleep(2) # 礼貌性延迟

    print(f"📊 Fetch Summary: {len(all_articles)} articles, {max_total_cites} total citations.")
    return all_articles, max_total_cites

# --- 3. 业务逻辑层 (Business Logic) ---

def find_match(title, scholar_map):
    """
    模糊匹配标题
    """
    if not title or not scholar_map: return None
    key = title.lower().strip()
    
    # 1. 精确匹配
    if key in scholar_map:
        return scholar_map[key]
    
    # 2. 模糊匹配
    matches = difflib.get_close_matches(key, scholar_map.keys(), n=1, cutoff=FUZZY_THRESHOLD)
    return scholar_map[matches[0]] if matches else None

def load_yaml(path):
    if not os.path.exists(path):
        print(f"❌ File not found: {path}")
        return None
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f) or {}
    except Exception as e:
        print(f"❌ Error reading YAML: {e}")
        return None

def save_yaml(data, path):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, sort_keys=False, default_flow_style=False, allow_unicode=True)
        return True
    except Exception as e:
        print(f"❌ Error saving file: {e}")
        return False

def update_publications():
    # 检查必要配置
    if not SCHOLAR_ID:
        print("❌ Error: GOOGLE_SCHOLAR_ID not found in environment variables.")
        return

    # 1. 获取在线数据
    scholar_data, fetched_total_cites = fetch_all_scholar_data(SCHOLAR_ID)
    if not scholar_data:
        print("⚠️ No data fetched. Aborting update.")
        return

    # 2. 读取本地文件
    data = load_yaml(FILE_PATH)
    if data is None: return

    # 兼容 items 列表或根字典结构
    pubs = data.get('items', data) if isinstance(data, dict) else data
    if not isinstance(pubs, list):
        print("❌ YAML format error: expected a list of publications.")
        return

    updates_count = 0
    not_found_list = []

    # 3. 更新总引用数 (如果是字典结构且有该字段)
    if isinstance(data, dict) and fetched_total_cites > 0:
        current_total = data.get('total_cited_by', 0)
        if current_total != fetched_total_cites:
            print(f"📈 Updating total citations: {current_total} -> {fetched_total_cites}")
            data['total_cited_by'] = fetched_total_cites
            updates_count += 1

    # 4. 遍历并更新单篇文章
    for pub in pubs:
        title = pub.get('title')
        match = find_match(title, scholar_data)
        
        if match:
            # 检查引用数更新
            old_cite = pub.get('cited_by', 0)
            new_cite = match['cited_by']
            
            # 检查 ID 更新
            old_id = pub.get('google_scholar_id')
            new_id = match['id']
            
            changed = False
            
            if old_cite != new_cite:
                print(f"📄 Update Cite '{title[:30]}...': {old_cite} -> {new_cite}")
                pub['cited_by'] = new_cite
                changed = True
            
            if new_id and new_id != old_id:
                print(f"🔗 Update ID   '{title[:30]}...': {old_id} -> {new_id}")
                pub['google_scholar_id'] = new_id
                changed = True
                
            if changed:
                updates_count += 1
        else:
            not_found_list.append(title)

    # 5. 保存结果
    if updates_count > 0:
        if save_yaml(data, FILE_PATH):
            print(f"✅ Successfully saved {updates_count} updates to {FILE_PATH}.")
    else:
        print("ℹ️ No changes needed.")

    # 6. 警告未找到的文章
    if not_found_list:
        print("\n" + "="*50)
        print(f"⚠️  WARNING: {len(not_found_list)} Papers from YAML NOT found online")
        print("="*50)
        for i, t in enumerate(not_found_list, 1):
            print(f"{i}. {t}")
        print("="*50 + "\n")

if __name__ == "__main__":
    update_publications()
