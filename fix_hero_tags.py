#!/usr/bin/env python3
"""
Fix hero section tags: separate "Low MOQ Flexible" into two tags
"""

import re

file_path = "public/index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the Low MOQ Flexible section
old_section = '''                            <div class="flex items-center gap-2 text-gray-600 bg-white/80 px-4 py-2 rounded-lg">
                                <i class="fas fa-sliders-h text-accent"></i>
                                <span class="text-sm">Low MOQ Flexible</span>
                            </div>'''

new_section = '''                            <div class="flex items-center gap-2 text-gray-600 bg-white/80 px-4 py-2 rounded-lg">
                                <i class="fas fa-box text-accent"></i>
                                <span class="text-sm">Low MOQ</span>
                            </div>
                            <div class="flex items-center gap-2 text-gray-600 bg-white/80 px-4 py-2 rounded-lg">
                                <i class="fas fa-sliders-h text-accent"></i>
                                <span class="text-sm">Flexible</span>
                            </div>'''

if old_section in content:
    content = content.replace(old_section, new_section)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully updated hero section tags")
    print("Separated 'Low MOQ Flexible' into two tags: 'Low MOQ' and 'Flexible'")
else:
    print("Section not found or already updated")
    # Let's search for what exists
    if "Low MOQ" in content and "Flexible" in content:
        print("Looks like they are already separate")
    else:
        print("Current content around that area:")
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if 'Low MOQ' in line:
                for j in range(max(0, i-5), min(len(lines), i+10)):
                    print(f"{j+1}: {lines[j]}")
                break
