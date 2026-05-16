#!/usr/bin/env python3
"""
检查每个轮播的图片数量和dot数量是否匹配 - v2
"""

import re

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("=" * 60)
print("轮播dot数量检查报告 v2")
print("=" * 60)

# 找到所有轮播开始行
carousel_starts = []
for i, line in enumerate(lines):
    if 'class="product-carousel" id="carousel-' in line:
        match = re.search(r'id="carousel-([^"]+)"', line)
        if match:
            carousel_starts.append((i, match.group(1)))

issues = []

for start_line, cid in carousel_starts:
    # 找到这个轮播结束的位置（下一个轮播或足够远的行）
    end_line = start_line + 100  # 每个轮播不会超过100行
    
    block_lines = lines[start_line:end_line]
    block = ''.join(block_lines)
    
    # 统计dot数量
    dot_count = block.count('class="carousel-dot')
    
    # 计算JS中的图片数组长度（查找goToCarousel函数中的调用）
    # 或者查找dot的onclick中的最大索引
    max_index = -1
    for match in re.finditer(rf"goToCarousel\('{cid}',\s*(\d+)\)", block):
        idx = int(match.group(1))
        if idx > max_index:
            max_index = idx
    
    img_count = max_index + 1 if max_index >= 0 else 0
    
    # 如果没有找到JS调用，检查实际的img标签（可能只有1张）
    if img_count == 0:
        img_count = block.count('<img')
    
    status = "✓" if img_count == dot_count and dot_count > 0 else "✗"
    
    if dot_count == 0:
        issues.append(f"{cid}: 完全没有dot!")
    elif img_count != dot_count:
        issues.append(f"{cid}: 图片{img_count}张 != dot{dot_count}个")
    
    print(f"{status} carousel-{cid}: 图片={img_count}张, dots={dot_count}个")

print("=" * 60)
if issues:
    print("发现问题:")
    for issue in issues:
        print(f"  - {issue}")
else:
    print("所有轮播都有正确数量的dots!")
print("=" * 60)
