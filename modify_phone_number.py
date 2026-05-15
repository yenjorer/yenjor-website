#!/usr/bin/env python3
import re

# 读取HTML文件
with open('public/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 修改电话号码显示：将+86 152-5739-7811改为+86 152-XXX-7811
# 保留WhatsApp跳转链接不变
old_pattern = r'\+86 152-5739-7811'
new_display = '+86 152-XXX-7811'

# 替换所有显示的电话号码
content = content.replace('+86 152-5739-7811', new_display)

# 确保WhatsApp链接正确（wa.me/8615257397811）
# 检查并确保WhatsApp跳转链接不变
whatsapp_link = 'https://wa.me/8615257397811'
if whatsapp_link not in content:
    print("Warning: WhatsApp link not found!")
else:
    print("WhatsApp link verified: OK")

# 写入修改后的内容
with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("电话号码修改完成！")
print(f"显示格式已改为: {new_display}")
print(f"WhatsApp跳转链接保持: {whatsapp_link}")

# 验证修改结果
print("\n=== 验证结果 ===")
with open('public/index.html', 'r', encoding='utf-8') as f:
    content_check = f.read()

if new_display in content_check:
    print("✓ 电话号码显示格式已成功更新")
if whatsapp_link in content_check:
    print("✓ WhatsApp跳转链接正确")

print(f"修改的位置: {content_check.count(new_display)} 处")
