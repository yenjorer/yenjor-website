#!/usr/bin/env python3
"""
彻底修复所有轮播的dot（导航点）
1. 为每个轮播添加正确数量的dots
2. 确保第一个dot是active状态
3. 确保dot的数量和图片数量一致
"""

import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 轮播图片数量定义（来自galleryImages）
carousel_image_counts = {
    'shell': 7,
    'resin': 10,
    'shankMetal': 10,
    'shell-card': 7,
    'coconut': 4,
    'horn': 3,
    'wooden': 8,
    'resin-card': 10,
    'shankMetal-card': 10,
    'jeans': 10,
    'snap': 8
}

def generate_dots_html(category, count):
    """生成dots的HTML"""
    dots_html = ['                        <div class="carousel-dots">']
    for i in range(count):
        active_class = ' active' if i == 0 else ''
        dots_html.append(f'                            <button class="carousel-dot{active_class}" onclick="event.stopPropagation(); goToCarousel(\'{category}\', {i})"></button>')
    dots_html.append('                        </div>')
    return '\n'.join(dots_html)

# 处理每个轮播
fixed_count = 0

for category, expected_count in carousel_image_counts.items():
    # 查找轮播块
    pattern = rf'(<div class="product-carousel" id="carousel-{re.escape(category)}".*?</button>\s*)<div class="carousel-dots">.*?</div>(\s*</div>)'
    
    match = re.search(pattern, content, re.DOTALL)
    if match:
        # 生成新的dots
        new_dots = generate_dots_html(category, expected_count)
        content = content[:match.start()] + match.group(1) + new_dots + match.group(2) + content[match.end():]
        fixed_count += 1
        print(f"✓ 修复 carousel-{category}: 设置为 {expected_count} 个dots")

# 保存文件
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n" + "=" * 60)
print(f"共修复了 {fixed_count} 个轮播的dots")
print("=" * 60)
