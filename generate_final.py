import json
import os
import math
import re
from pathlib import Path
from bs4 import BeautifulSoup
from datetime import datetime

# ✅ 读取配置文件中的域名
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)
domain = config.get("domain", "https://example.com")

exts = ['.jpg', '.jpeg', '.png', '.webp']

def insert_ads(soup):
    if soup.body and not soup.find('script', src='ads.js'):
        ads = soup.new_tag('script', src='ads.js')
        soup.body.append(ads)

def load_keywords(category):
    try:
        with open(f'keywords/{category}.txt', 'r', encoding='utf-8') as f:
            return [kw.strip() for kw in f if kw.strip()]
    except:
        return []

def get_category_folders():
    return [d for d in os.listdir() if os.path.isdir(d) and not d.startswith('.') and d.lower() not in ['images', 'generator', 'keywords']]

def find_latest_images(folder, count=4):
    images = []
    for file in os.listdir(folder):
        if os.path.splitext(file)[1].lower() in exts:
            path = os.path.join(folder, file)
            images.append((file, os.path.getmtime(path)))
    images.sort(key=lambda x: x[1], reverse=True)
    return [img[0] for img in images[:count]]

# ✅ 新增：自动生成描述与正文
def generate_description(keyword):
    return f"{keyword.capitalize()} themed portrait showcasing unique visual storytelling. Explore how this image captures emotion, light, and style in a way that appeals to refined visual taste and aesthetic appreciation."

def generate_paragraph(keyword):
    return (
        f"This portrait illustrates the essence of {keyword}, blending atmosphere, style, and emotional depth. "
        f"Whether you're a fan of {keyword} inspired photography or simply exploring visual narratives, "
        f"this image offers a glimpse into a world of curated aesthetics. It balances composition, mood, and detail "
        f"to create a memorable visual experience. Keywords like '{keyword}' often attract those who value uniqueness, "
        f"sophistication, and subtle beauty in digital galleries and modern photography portfolios."
    )

def generate_category_blocks(category_root="."):
    html_blocks = ""
    for folder in sorted(os.listdir(category_root)):
        folder_path = os.path.join(category_root, folder)
        if not os.path.isdir(folder_path):
            continue
        images = [f for f in os.listdir(folder_path) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
        if not images:
            continue
        images = sorted(images)[-3:]
        block = f'<h2>{folder.capitalize()}</h2>\n<div class="gallery">\n'
        for img in images:
            block += f'  <img src="{folder}/{img}" style="width:30%; margin:5px; border-radius:10px; box-shadow:0 2px 6px #000;">\n'
        block += f'</div>\n<div class="view-more"><a href="{folder}/page1.html">→ View More</a></div>\n\n'
        html_blocks += block
    return html_blocks.strip()

def update_index_html(index_path='index.html'):
    if not os.path.exists(index_path):
        print('❌ index.html 不存在')
        return
    with open(index_path, 'r', encoding='utf-8') as f:
        html = f.read()
    updated = False
    for folder in get_category_folders():
        latest_imgs = find_latest_images(folder, count=4)
        if len(latest_imgs) == 0:
            continue
        pattern = re.compile(rf'(<h2>{folder.capitalize()}</h2>\s*<div class="gallery">)(.*?)(</div>)', re.DOTALL)
        new_block = ''
        for img in latest_imgs:
            new_block += f'<a data-lightbox="{folder}" href="{folder}/page1.html"><img alt="" src="{folder}/{img}"/></a>\n'
        if pattern.search(html):
            html = pattern.sub(lambda m: f"{m.group(1)}\n{new_block}{m.group(3)}", html)
            updated = True
        else:
            print(f'⚠️ 找不到分类区块：{folder.capitalize()}，请确认 index.html 是否包含对应结构')
    if updated:
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(html)

def generate_pages():
    categories = get_category_folders()
    for cat in categories:
        folder = Path(cat)
        images = sorted([f for f in folder.glob('*.jpg')])
        keywords = load_keywords(cat)
        per_page = 20
        total_pages = math.ceil(len(images) / per_page)
        for page in range(total_pages):
            start = page * per_page
            end = start + per_page
            imgs = images[start:end]
            page_file = folder / f'page{page+1}.html'
            with open(page_file, 'w', encoding='utf-8') as f:
                f.write(f'<html><head><title>{cat} - Page {page+1}</title></head><body>')
                for idx, img_path in enumerate(imgs):
                    name = img_path.stem
                    html_file = folder / f'{name}.html'
                    kw = keywords[start+idx] if start+idx < len(keywords) else cat
                    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <title>{kw}</title>
  <meta name="description" content="{generate_description(kw)}">
  <meta name="keywords" content="{kw}">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body {{ font-family: Arial, sans-serif; text-align: center; background-color: #f5f5f5; color: #333; }}
    img {{ max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }}
    .container {{ max-width: 800px; margin: 20px auto; padding: 20px; background: white; border-radius: 10px; }}
    p {{ font-size: 16px; line-height: 1.6; text-align: left; }}
  </style>
</head>
<body>
  <div class="container">
    <h1>{kw}</h1>
    <img src="{img_path.name}" alt="{kw}">
    <p>{generate_paragraph(kw)}</p>
    <div><a href="page{page+1}.html">Back to List</a> | <a href="../index.html">Home</a></div>
  </div>
</body>
</html>
"""
                    with open(html_file, 'w', encoding='utf-8') as imgf:
                        imgf.write(html)
                    soup = BeautifulSoup(open(html_file, encoding='utf-8'), 'html.parser')
                    insert_ads(soup)
                    with open(html_file, 'w', encoding='utf-8') as imgf:
                        imgf.write(str(soup))
                    f.write(f'<a href="{name}.html"><img src="{img_path.name}" width=200></a>\n')
                f.write('<div style="margin-top:20px">')
                if page > 0:
                    f.write(f'<a href="page{page}.html">Previous</a> ')
                f.write(f'<a href="../index.html">Home</a> ')
                if page < total_pages - 1:
                    f.write(f'<a href="page{page+2}.html">Next</a>')
                f.write('</div></body></html>')

def generate_sitemap(domain='https://example.com'):
    with open('sitemap.xml', 'w', encoding='utf-8') as sm:
        sm.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for cat in get_category_folders():
            folder = Path(cat)
            for file in folder.glob('*.html'):
                file_path = folder / file.name
                lastmod = datetime.utcfromtimestamp(file_path.stat().st_mtime).strftime('%Y-%m-%d')
                sm.write(f'<url><loc>{domain}/{cat}/{file.name}</loc><lastmod>{lastmod}</lastmod></url>\n')
        sm.write('</urlset>')

def generate_robots_txt(domain):
    content = f"""User-agent: *
Allow: /
Sitemap: {domain}/sitemap.xml
"""
    with open("robots.txt", "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ 已生成 robots.txt")

# ✅ 主程序入口
if __name__ == '__main__':
    update_index_html()
    generate_pages()
    generate_sitemap(domain)
    generate_robots_txt(domain)

    index_file = "index.html"
    if os.path.exists(index_file):
        with open(index_file, "r", encoding="utf-8") as f:
            html = f.read()
        blocks = generate_category_blocks(".")
        html = html.replace("<!-- {auto_categories_here} -->", blocks)
        with open(index_file, "w", encoding="utf-8") as f:
            f.write(html)
        print("✅ 已自动更新首页分类图片展示。")

    print('✅ 所有页面生成完毕，包括首页主图、分页图页、SEO结构、广告注入、sitemap、robots ✅')
