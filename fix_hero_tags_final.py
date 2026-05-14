#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# 读取文件
with open('public/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 要删除的卖点标签部分的HTML
# 从第1111行开始的grid div到第1140行
old_tags_pattern = r'''                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-8 animate-fade-in-up delay-200">
                        <div class="flex items-center justify-center gap-2 text-gray-600 bg-white/80 backdrop-blur-sm px-4 py-2.5 rounded-lg shadow-sm">
                            <i class="fas fa-gift text-eco"></i>
                            <span class="text-sm font-medium whitespace-nowrap">Free Samples</span>
                        </div>
                        <div class="flex items-center justify-center gap-2 text-gray-600 bg-white/80 backdrop-blur-sm px-4 py-2.5 rounded-lg shadow-sm">
                            <i class="fas fa-cogs text-eco"></i>
                            <span class="text-sm font-medium whitespace-nowrap">Advanced Tech</span>
                        </div>
                        <div class="flex items-center justify-center gap-2 text-gray-600 bg-white/80 backdrop-blur-sm px-4 py-2.5 rounded-lg shadow-sm">
                            <i class="fas fa-globe text-eco"></i>
                            <span class="text-sm font-medium whitespace-nowrap">Global Clients</span>
                        </div>
                        <div class="flex items-center justify-center gap-2 text-gray-600 bg-white/80 backdrop-blur-sm px-4 py-2.5 rounded-lg shadow-sm">
                            <i class="fas fa-bolt text-accent"></i>
                            <span class="text-sm font-medium whitespace-nowrap">24h Response</span>
                        </div>
                        <div class="flex items-center justify-center gap-2 text-gray-600 bg-white/80 backdrop-blur-sm px-4 py-2.5 rounded-lg shadow-sm">
                            <i class="fas fa-box text-accent"></i>
                            <span class="text-sm font-medium whitespace-nowrap">Low MOQ</span>
                        </div>
                        <div class="flex items-center justify-center gap-2 text-gray-600 bg-white/80 backdrop-blur-sm px-4 py-2.5 rounded-lg shadow-sm">
                            <i class="fas fa-sliders-h text-accent"></i>
                            <span class="text-sm font-medium whitespace-nowrap">Flexible MOQ</span>
                        </div>
                        <div class="flex items-center justify-center gap-2 text-gray-600 bg-white/80 backdrop-blur-sm px-4 py-2.5 rounded-lg shadow-sm sm:col-start-2">
                            <i class="fas fa-shield-alt text-accent"></i>
                            <span class="text-sm font-medium whitespace-nowrap">Quality Assured</span>
                        </div>
                    </div>
'''

# 检查是否匹配
if old_tags_pattern.strip() in content:
    print("找到卖点标签元素，准备删除...")
    # 删除卖点标签部分
    content = content.replace(old_tags_pattern, '')
else:
    print("未找到精确匹配，尝试使用正则表达式...")
    # 使用正则表达式匹配grid div及其内容
    # 匹配从grid grid-cols-2开始到</div>结束的部分
    pattern = r'                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-8 animate-fade-in-up delay-200">.*?                    </div>\n'
    content = re.sub(pattern, '', content, flags=re.DOTALL)
    print("正则表达式替换完成")

# 调整副标题和按钮之间的间距
# 将副标题的mb-8改为更合适的值，或者在按钮部分添加适当的margin
# 当前副标题是mb-8（margin-bottom: 2rem），删除标签后可以适当增加这个间距
# 或者给按钮部分添加额外的margin-top

# 我们可以将副标题的mb-8调整为mb-10（2.5rem），让间距更协调
old_subtitle = '                    <p class="text-gray-600 text-lg md:text-xl mb-8 max-w-xl animate-fade-in-up delay-200">'
new_subtitle = '                    <p class="text-gray-600 text-lg md:text-xl mb-10 max-w-xl animate-fade-in-up delay-200">'

if old_subtitle in content:
    content = content.replace(old_subtitle, new_subtitle)
    print("副标题间距已调整")
else:
    print("未找到副标题样式")

# 写入文件
with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("修改完成！")
