import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到script开始位置
script_start = content.find('<script>', content.find('<!-- JavaScript -->'))

# 提取整个script内容
script_end = content.find('</script>', script_start)
script_content = content[script_start:script_end]

# 找到galleryImages的定义
gallery_start = script_content.find('const galleryImages = {')
gallery_end = script_content.find('};', gallery_start) + 2

gallery_code = script_content[gallery_start:gallery_end]

# 找到carouselState的定义
carousel_state_start = script_content.find('const carouselState = {};')

# 新的顺序：先定义carouselState, 然后galleryImages, 再定义所有函数
new_script_start = script_content[:carousel_state_start]

# 把carouselState和galleryImages移到最前面
variables_part = 'const carouselState = {};\n\n        ' + gallery_code + '\n\n        '

# 找到函数定义的开始（第一个function goToCarousel）
function_start = script_content.find('function goToCarousel')

# 构建新的script内容
new_script_content = new_script_start + variables_part + script_content[function_start:gallery_start]

# 移除原来的galleryImages定义后的重复部分
new_script_content = new_script_content.replace(gallery_code, '')

# 确保没有重复的galleryImages定义
# 重新构建整个script
script_before_carousel = script_content[:carousel_state_start]
script_after_gallery = script_content[gallery_end:]

new_script_content = script_before_carousel + 'const carouselState = {};\n\n        ' + gallery_code + '\n\n        ' + script_after_gallery

# 写入
new_full_content = content[:script_start] + new_script_content + content[script_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_full_content)

print("Fixed! Moved galleryImages definition before functions that use it")
