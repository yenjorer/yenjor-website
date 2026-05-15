#!/usr/bin/env python3
"""
快速恢复banner到原始样式和内容
同时修改factory图片浮窗文字
"""

import re

# 读取HTML文件
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 修改Banner主标题
# 当前: Elevate Your Garments with Premium Buttons
# 目标: Premium Buttons for Fashion Brands.
old_title = 'Elevate Your Garments with Premium Buttons'
new_title = 'Premium Buttons for Fashion Brands.'
content = content.replace(old_title, new_title)

# 2. 修改Banner副标题
# 当前: Specializing in High-Quality Metal Buttons, Eco-Friendly Resin Buttons, and Sustainable Shell Buttons
# 目标: Leading manufacturer of metal buttons and resin buttons. Two decades of factory expertise serving garment factories, brands, and SOHO buyers worldwide.
old_subtitle = 'Specializing in High-Quality Metal Buttons, Eco-Friendly Resin Buttons, and Sustainable Shell Buttons'
new_subtitle = 'Leading manufacturer of metal buttons and resin buttons. Two decades of factory expertise serving garment factories, brands, and SOHO buyers worldwide.'
content = content.replace(old_subtitle, new_subtitle)

# 3. 修改Factory图片浮窗文字
# 当前: 50+ Countries Shipped
# 目标: 3,000㎡ Production Facility
old_factory_text = '<p class="text-5xl font-bold text-amber-500">50+</p>\n                        <p class="text-sm text-gray-300">Countries Shipped</p>'
new_factory_text = '<p class="text-4xl font-bold text-amber-500">3,000㎡</p>\n                        <p class="text-sm text-gray-300">Production Facility</p>'
content = content.replace(old_factory_text, new_factory_text)

# 保存文件
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Banner内容恢复完成！")
print("✅ Factory图片浮窗文字修改完成！")
print("\n修改摘要:")
print(f"  主标题: {old_title}")
print(f"       → {new_title}")
print(f"  副标题: {old_subtitle[:60]}...")
print(f"       → {new_subtitle[:60]}...")
print(f"  浮窗文字: 50+ Countries Shipped")
print(f"         → 3,000㎡ Production Facility")
