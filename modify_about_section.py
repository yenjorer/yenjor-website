import re

# 读取文件
with open('public/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 要插入的文案
new_intro = '''                    <p class="text-gray-600 text-lg mb-6 leading-relaxed">
                        Established in 2004, Yenjor specializes in high-quality metal buttons, resin buttons, and garment accessories. Located in the Yangtze River Delta with easy access to Shanghai and Ningbo ports, our 3,000㎡ facility houses over 100 skilled craftsmen. Our products are trusted by garment factories, fashion brands, and wholesalers across 15+ countries worldwide.
                    </p>

'''

# 找到分割线和四个亮点grid之间的位置插入
# 定位点：分割线 `<div class="section-divider mb-8"></div>` 之后，四个亮点的grid之前
pattern = r'(<div class="section-divider mb-8"></div>\n)(\s*<p class="text-gray-600 text-lg mb-6 leading-relaxed">)'

# 在分割线之后、现有段落之前插入新文案
replacement = r'\1' + new_intro + r'\2'
new_content = re.sub(pattern, replacement, content)

# 保存文件
with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("修改完成！")
