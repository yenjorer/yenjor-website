#!/usr/bin/env python3
"""
检查每个轮播的图片数量和dot数量是否匹配
"""

import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到所有轮播ID
carousel_ids = re.findall(r'id="carousel-([^"]+)"', content)
carousel_ids = list(set(carousel_ids))
carousel_ids.sort()

print("=" * 60)
print("轮播dot数量检查报告")
print("=" * 60)

issues = []

for cid in carousel_ids:
    # 查找该轮播的HTML块
    pattern = rf'<div class="product-carousel" id="carousel-{cid}".*?</div>\s*</div>'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        block = match.group(0)
        
        # 统计图片数量
        img_count = len(re.findall(r'<img[^>]+class="carousel-img"', block))
        
        # 统计dot数量
        dot_count = len(re.findall(r'class="carousel-dot', block))
        
        status = "✓" if img_count == dot_count else "✗"
        
        if img_count != dot_count:
            issues.append(f"{cid}: 图片{img_count}张 != dot{dot_count}个")
        
        print(f"{status} carousel-{cid}: 图片={img_count}张, dots={dot_count}个")

print("=" * 60)
if issues:
    print("发现问题:")
    for issue in issues:
        print(f"  - {issue}")
else:
    print("所有轮播的图片数量与dot数量匹配!")
print("=" * 60)
