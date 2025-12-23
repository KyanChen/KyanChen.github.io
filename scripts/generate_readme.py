import yaml
import re
from pathlib import Path

def main():
    # 1. 初始化路径 (获取项目根目录)
    # 注意：假设脚本位置是 repo/scripts/generate_readme.py，parents[1] 就是 repo 根目录
    root = Path(__file__).resolve().parents[1]
    
    # 简化的加载函数
    def load_data(path):
        file_path = root / path
        if not file_path.exists():
            print(f"Error: File not found: {file_path}")
            # 返回空字典防止崩溃，或者让它在这里报错以便调试
            return {} 
        return yaml.safe_load(file_path.read_text(encoding='utf-8'))

    config = load_data('_config.yml')
    # 注意：这里依赖 Workflow 正确将私有数据下载到 _data 目录
    profile = load_data('_data/profile.yml')
    news = load_data('_data/news.yml')
    
    if not profile or not news:
        print("Warning: Profile or News data is empty or missing!")
        return

    # 2. 处理 About Me (移除 HTML 注释行)
    raw_bio = profile.get('short_bio', {}).get('en', '')
    bio_lines = [line for line in raw_bio.splitlines() if not line.strip().startswith('<!--')]
    
    # 3. 处理 News (筛选 -> 排序 -> 格式化)
    valid_news = sorted(
        [n for n in news if n.get('selected') and not n.get('archive')],
        key=lambda x: x.get('date', ''), 
        reverse=True
    )

    news_list = []
    for item in valid_news:
        content = item.get('content', {}).get('en', '')
        # 修复：使用 raw string (r'') 处理正则中的反斜杠
        content = re.sub(
            r'<span class="highlight">([^<]+)</span>', 
            r'$\\color{red}{\\textbf{\1}}$', 
            content
        )
        
        content = f"- **[{item.get('date')}]** {content}"
        news_list.append(content)

    # 4. 组装内容
    news_str = "\n".join(news_list)
    email = profile.get('contact', {}).get('email', '').replace('(at)', '@')
    bio_str = "\n".join(bio_lines) 
    
    readme_content = f"""# Hi 👋

## 👋 About Me
{bio_str}

## 📎 Homepages
Personal Pages: [{config.get('url')}]({config.get('url')}) (updated recently🔥)
Google Scholar: [Link](https://scholar.google.com/citations?user={config.get('google_scholar_id')})

## 📰 News
{news_str}

## 📫 Contact Me
Email: {email}
"""
    # === 修复点：修复 SyntaxWarning ===
    # 使用 raw string r'\&' 表示字面量的 反斜杠+&
    safe_readme_content = readme_content.replace('&', r'\\&')

    # 5. 写入文件
    readme_path = root / 'readme_profile.md'
    readme_path.write_text(safe_readme_content, encoding='utf-8')
    print(f"Successfully generated: {readme_path}")

if __name__ == "__main__":
    main()
