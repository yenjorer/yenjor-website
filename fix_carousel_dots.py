#!/usr/bin/env python3
"""
彻底修复轮播dot（导航点）不显示的问题
问题根源：.product-carousel的overflow:hidden裁剪了carousel-dots
修复方案：
1. 移除.product-carousel的overflow:hidden
2. 给carousel-dots添加足够的z-index确保可见
3. 确保dots位置正确
"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 修复1: 移除.product-carousel的overflow:hidden，改为visible
old_carousel_css = """.product-carousel {
            position: relative;
            width: 100%;
            overflow: hidden;
            border-radius: var(--radius-lg);
        }"""

new_carousel_css = """.product-carousel {
            position: relative;
            width: 100%;
            overflow: visible;
            border-radius: var(--radius-lg);
        }"""

content = content.replace(old_carousel_css, new_carousel_css)

# 修复2: 增强carousel-dots的CSS，确保可见性和z-index
old_dots_css = """.carousel-dots {
            display: flex;
            justify-content: center;
            gap: 0.5rem;
            margin-top: 1rem;
        }"""

new_dots_css = """.carousel-dots {
            display: flex !important;
            justify-content: center;
            gap: 0.5rem;
            margin-top: 1rem;
            position: relative;
            z-index: 100;
            visibility: visible;
            opacity: 1;
        }"""

content = content.replace(old_dots_css, new_dots_css)

# 修复3: 增强carousel-dot的CSS，确保每个dot都可见
old_dot_css = """.carousel-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #d1d5db;
            border: none;
            cursor: pointer;
            transition: all var(--transition-normal);
            padding: 0;
        }"""

new_dot_css = """.carousel-dot {
            width: 10px !important;
            height: 10px !important;
            border-radius: 50%;
            background: #d1d5db !important;
            border: 2px solid rgba(255,255,255,0.5) !important;
            cursor: pointer !important;
            transition: all var(--transition-normal) !important;
            padding: 0 !important;
            display: block !important;
            visibility: visible !important;
            opacity: 1 !important;
            position: relative !important;
            z-index: 101 !important;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
        }"""

content = content.replace(old_dot_css, new_dot_css)

# 修复4: 增强active dot的CSS
old_active_dot_css = """.carousel-dot.active {
            background: var(--color-accent);
            width: 24px;
            border-radius: 4px;
        }"""

new_active_dot_css = """.carousel-dot.active {
            background: var(--color-accent) !important;
            width: 28px !important;
            height: 10px !important;
            border-radius: 5px !important;
            box-shadow: 0 2px 8px rgba(255, 107, 0, 0.4) !important;
            border: none !important;
        }"""

content = content.replace(old_active_dot_css, new_active_dot_css)

# 修复5: 增强hover dot的CSS
old_hover_dot_css = """.carousel-dot:hover:not(.active) {
            background: #9ca3af;
        }"""

new_hover_dot_css = """.carousel-dot:hover:not(.active) {
            background: #9ca3af !important;
            transform: scale(1.2) !important;
        }"""

content = content.replace(old_hover_dot_css, new_hover_dot_css)

# 修复6: 确保carousel-main不会覆盖dots，给它适当的z-index
old_carousel_main_css = """.carousel-main {
            position: relative;
            width: 100%;
            aspect-ratio: 4/3;
            overflow: hidden;
            cursor: pointer;
        }"""

new_carousel_main_css = """.carousel-main {
            position: relative;
            width: 100%;
            aspect-ratio: 4/3;
            overflow: hidden;
            cursor: pointer;
            z-index: 1;
            border-radius: var(--radius-lg);
        }"""

content = content.replace(old_carousel_main_css, new_carousel_main_css)

# 保存文件
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ 轮播dot CSS修复完成")
print("  - 移除了.product-carousel的overflow:hidden")
print("  - 增强了carousel-dots的z-index和可见性")
print("  - 增大了dot尺寸并添加边框")
print("  - 增强了active dot的视觉效果")
