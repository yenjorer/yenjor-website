#!/usr/bin/env python3
"""
修复导航菜单问题：
1. 添加Products直接链接到#products
2. 修复透明底问题，确保不透明背景
"""

# 读取HTML文件
with open('public/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 处理每一行
modified_lines = []
skip_next = False

for i, line in enumerate(lines):
    if skip_next:
        skip_next = False
        continue
    
    # 1. 修复导航栏背景色
    if 'bg-white/95 backdrop-blur-md' in line:
        modified_lines.append(line.replace('bg-white/95 backdrop-blur-md', 'bg-white shadow-sm'))
        continue
    
    # 2. 在桌面端导航菜单中添加Products链接（在About之后）
    if 'href="#about"' in line and 'text-gray-700 hover:text-accent' in line and 'Home' not in lines[i-1]:
        modified_lines.append(line)
        # 添加Products链接
        modified_lines.append('                    <a href="#products" class="text-gray-700 hover:text-accent font-medium transition-colors">Products</a>\n')
        continue
    
    # 3. 在移动端导航菜单中添加Products链接（在About之后）
    if 'href="#about"' in line and 'mobile-link py-3 px-4' in line and 'Home' not in lines[i-1]:
        modified_lines.append(line)
        # 添加Products链接
        modified_lines.append('                    <a href="#products" class="mobile-link py-3 px-4 text-lg font-medium text-gray-700 hover:bg-gray-50 rounded-lg transition-colors">Products</a>\n')
        continue
    
    modified_lines.append(line)

# 写入文件
with open('public/index.html', 'w', encoding='utf-8') as f:
    f.writelines(modified_lines)

print("导航菜单修复完成！")
print("1. 已添加Products链接到桌面端和移动端菜单")
print("2. 已将导航栏背景改为完全不透明（bg-white）")

# 验证修改
with open('public/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("\n验证修改结果：")
print("-" * 50)

# 检查桌面端导航
if 'href="#products"' in content and 'text-gray-700 hover:text-accent font-medium transition-colors">Products' in content:
    print("✓ Products链接已添加到桌面端导航")
else:
    print("✗ Products链接未找到在桌面端导航")

# 检查移动端导航
if 'mobile-link py-3 px-4 text-lg font-medium text-gray-700 hover:bg-gray-50 rounded-lg transition-colors">Products' in content:
    print("✓ Products链接已添加到移动端导航")
else:
    print("✗ Products链接未找到在移动端导航")

# 检查背景色
if 'bg-white shadow-sm' in content:
    print("✓ 导航栏背景已改为完全不透明")
else:
    print("✗ 导航栏背景色未正确修改")
