with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到carouselState位置
carousel_state_pos = content.find('const carouselState = {};')

# 找到galleryImages位置
gallery_pos = content.find('const galleryImages = {')

# 找到galleryImages结束位置
gallery_end = content.find('};', gallery_pos) + 2

# 提取galleryImages代码
gallery_code = content[gallery_pos:gallery_end]

# 删除原来的galleryImages
content_before_gallery = content[:gallery_pos]
content_after_gallery = content[gallery_end:]

# 把galleryImages插到carouselState后面
new_content = content_before_gallery.replace('const carouselState = {};', 
                                            'const carouselState = {};\n\n        ' + gallery_code + '\n') + content_after_gallery

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Fixed successfully!")
