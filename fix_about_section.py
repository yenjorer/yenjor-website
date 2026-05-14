#!/usr/bin/env python3
# 修改ABOUT YENJOR部分，删除段落2和3，只保留版本二文案

import re

# 读取文件
with open('public/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 定义要保留的版本二段落
paragraph1 = '''                    <p class="text-gray-600 text-lg mb-6 leading-relaxed">
                        With two decades of button manufacturing expertise, Yenjor delivers precision-crafted metal and resin buttons to the global apparel industry. Our 3,000㎡ production facility in the Yangtze River Delta combines modern equipment with traditional craftsmanship, employing over 100 skilled workers. We serve clients across 15+ countries, from Southeast Asia to Europe and America.
                    </p>'''

# 定义要删除的段落2和3
paragraphs_to_remove = '''

                    <p class="text-gray-600 text-lg mb-6 leading-relaxed">
                        <strong>Established in 2003 with two decades of manufacturing expertise</strong>, we specialize in 
                        <strong>metal buttons</strong>, <strong>resin buttons</strong>, and garment accessories. 
                        Located in the Yangtze River Delta near Shanghai, with convenient access to Shanghai and 
                        Ningbo ports for global shipping.
                    </p>
                    <p class="text-gray-600 text-lg mb-6 leading-relaxed">
                        Our products are trusted by garment factories, fashion brands, and wholesalers across 
                        <strong>Southeast Asia</strong> (Bangladesh, Vietnam), <strong>Europe</strong>, 
                        and <strong>America</strong> — 50+ countries worldwide.
                    </p>'''

# 替换：在段落1后面删除段落2和3
old_content = paragraph1 + paragraphs_to_remove
new_content = paragraph1

if old_content in content:
    content = content.replace(old_content, new_content)
    print("成功替换ABOUT YENJOR部分")
else:
    print("未找到匹配的内容，尝试使用正则表达式...")
    # 使用正则表达式匹配
    pattern = r'(                    <p class="text-gray-600 text-lg mb-6 leading-relaxed">\s*With two decades of button manufacturing expertise.*?</p>)\s*<p class="text-gray-600 text-lg mb-6 leading-relaxed">\s*<strong>Established in 2003.*?</p>\s*<p class="text-gray-600 text-lg mb-6 leading-relaxed">\s*Our products are trusted.*?</p>'
    replacement = r'\1'
    content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)
    if count > 0:
        print(f"正则替换成功，替换了{count}处")
    else:
        print("正则替换也失败了，请检查文件内容")
        exit(1)

# 保存修改
with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("ABOUT YENJOR部分修改完成！")
