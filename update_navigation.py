#!/usr/bin/env python3
"""
Update navigation menu:
- Add Collection → #products
- Keep Certification and Why Us merged
"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Desktop Navigation
old_desktop = '''                <!-- Desktop Navigation -->
                <div class="hidden lg:flex items-center space-x-8">
                    <a href="#home" class="text-gray-700 hover:text-accent font-medium transition-colors">Home</a>
                    <a href="#about" class="text-gray-700 hover:text-accent font-medium transition-colors">About Us</a>
                    <a href="#why-us" class="text-gray-700 hover:text-accent font-medium transition-colors">Why Us</a>
                    <a href="#contact" class="btn-primary px-6 py-2.5 rounded-full font-medium">Contact Us</a>
                </div>'''

new_desktop = '''                <!-- Desktop Navigation -->
                <div class="hidden lg:flex items-center space-x-8">
                    <a href="#home" class="text-gray-700 hover:text-accent font-medium transition-colors">Home</a>
                    <a href="#about" class="text-gray-700 hover:text-accent font-medium transition-colors">About Us</a>
                    <a href="#products" class="text-gray-700 hover:text-accent font-medium transition-colors">Collection</a>
                    <a href="#why-us" class="text-gray-700 hover:text-accent font-medium transition-colors">Why Us</a>
                    <a href="#contact" class="btn-primary px-6 py-2.5 rounded-full font-medium">Contact Us</a>
                </div>'''

content = content.replace(old_desktop, new_desktop)

# 2. Update Mobile Navigation
old_mobile = '''                <div class="flex flex-col space-y-4">
                    <a href="#home" class="mobile-link py-3 px-4 text-lg font-medium text-gray-700 hover:bg-gray-50 rounded-lg transition-colors">Home</a>
                    <a href="#about" class="mobile-link py-3 px-4 text-lg font-medium text-gray-700 hover:bg-gray-50 rounded-lg transition-colors">About Us</a>
                    <a href="#why-us" class="mobile-link py-3 px-4 text-lg font-medium text-gray-700 hover:bg-gray-50 rounded-lg transition-colors">Why Us</a>
                    <a href="#contact" class="mobile-link btn-primary py-3 px-4 text-lg font-medium text-white rounded-lg text-center mt-4">Contact Us</a>
                </div>'''

new_mobile = '''                <div class="flex flex-col space-y-4">
                    <a href="#home" class="mobile-link py-3 px-4 text-lg font-medium text-gray-700 hover:bg-gray-50 rounded-lg transition-colors">Home</a>
                    <a href="#about" class="mobile-link py-3 px-4 text-lg font-medium text-gray-700 hover:bg-gray-50 rounded-lg transition-colors">About Us</a>
                    <a href="#products" class="mobile-link py-3 px-4 text-lg font-medium text-gray-700 hover:bg-gray-50 rounded-lg transition-colors">Collection</a>
                    <a href="#why-us" class="mobile-link py-3 px-4 text-lg font-medium text-gray-700 hover:bg-gray-50 rounded-lg transition-colors">Why Us</a>
                    <a href="#contact" class="mobile-link btn-primary py-3 px-4 text-lg font-medium text-white rounded-lg text-center mt-4">Contact Us</a>
                </div>'''

content = content.replace(old_mobile, new_mobile)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Navigation menu updated successfully!")
print("- Added Collection → #products to desktop menu")
print("- Added Collection → #products to mobile menu")
print("- Certification and Why Us remain merged")
