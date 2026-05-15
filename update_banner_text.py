#!/usr/bin/env python3
"""
Update banner text to match user's screenshot:
- Main title: Elevate Your Garments with Premium Buttons
- Subtitle: Specializing in High-Quality Metal Buttons, Eco-Friendly Resin Buttons, and Sustainable Shell Buttons
- Keep tags unchanged
- Ensure text alignment is justified (左右平齐)
"""

import re

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update main title
old_title = """                    <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold text-gray-900 leading-tight mb-6 animate-fade-in-up delay-100 text-center lg:text-left">
                        Buttons Made Easy.
                    </h1>"""

new_title = """                    <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold text-gray-900 leading-tight mb-6 animate-fade-in-up delay-100 text-center lg:text-left" style="text-align: justify;">
                        Elevate Your Garments with Premium Buttons
                    </h1>"""

content = content.replace(old_title, new_title)

# 2. Update subtitle
old_subtitle = """                    <p class="text-gray-600 text-lg md:text-xl mb-8 max-w-xl animate-fade-in-up delay-200 text-center lg:text-left mx-auto lg:mx-0">
                        Yenjor — China's trusted button factory. 20 years making metal & resin buttons for garment factories and brands worldwide.
                    </p>"""

new_subtitle = """                    <p class="text-gray-600 text-lg md:text-xl mb-8 max-w-xl animate-fade-in-up delay-200 text-center lg:text-left mx-auto lg:mx-0" style="text-align: justify;">
                        Specializing in High-Quality Metal Buttons, Eco-Friendly Resin Buttons, and Sustainable Shell Buttons
                    </p>"""

content = content.replace(old_subtitle, new_subtitle)

# Write the updated content
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Banner text updated successfully!")
print("- Main title: 'Elevate Your Garments with Premium Buttons'")
print("- Subtitle: 'Specializing in High-Quality Metal Buttons, Eco-Friendly Resin Buttons, and Sustainable Shell Buttons'")
print("- Tags unchanged")
print("- Text alignment set to justify (左右平齐)")
