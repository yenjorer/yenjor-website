#!/usr/bin/env python3
"""
修改统计数据部分为方案C：
- 整体Section毛玻璃效果
- 去掉每个item的单独卡片
"""

import re

# 读取文件
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 修改stat-item的CSS - 去掉毛玻璃卡片效果
old_stat_item_css = """        .stat-item {
            position: relative;
            text-align: center;
            padding: 1.5rem 1rem;
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 12px;
            box-shadow: 0 4px 24px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }

        .stat-item:hover {
            background: rgba(255, 255, 255, 0.06);
            transform: translateY(-2px);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
        }
        
        .stat-item::after {
            content: '';
            position: absolute;
            right: 0;
            top: 50%;
            transform: translateY(-50%);
            height: 60%;
            width: 1px;
            background: rgba(255,255,255,0.1);
        }
        
        .stat-item:last-child::after {
            display: none;
        }"""

new_stat_item_css = """        .stat-item {
            position: relative;
            text-align: center;
            padding: 1rem 2rem;
        }

        .stat-item::after {
            content: '';
            position: absolute;
            right: 0;
            top: 50%;
            transform: translateY(-50%);
            height: 60%;
            width: 1px;
            background: rgba(255,255,255,0.15);
        }

        .stat-item:last-child::after {
            display: none;
        }"""

content = content.replace(old_stat_item_css, new_stat_item_css)

# 2. 修改Section的HTML - 添加整体毛玻璃效果
old_section_html = """    <!-- Stats Section -->
    <section class="bg-primary py-12">"""

new_section_html = """    <!-- Stats Section -->
    <section class="bg-primary/80 backdrop-blur-xl border-y border-white/10 py-12">"""

content = content.replace(old_section_html, new_section_html)

# 3. 去掉stat-item的px-4类（因为padding在CSS中已经定义）
content = re.sub(r'class="stat-item px-4"', 'class="stat-item"', content)

# 写入文件
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ 统计数据部分已修改为方案C")
print("   - 整体Section添加了毛玻璃效果（backdrop-blur-xl）")
print("   - 去掉了每个item的单独卡片样式")
print("   - 添加了上下边框增加层次感")
print("   - 保留了item之间的垂直分隔线")
