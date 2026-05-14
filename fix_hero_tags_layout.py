#!/usr/bin/env python3
import re

# Read the HTML file
with open('public/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the old hero tags section pattern
old_pattern = r'''                    <div class="flex flex-wrap gap-4 justify-center lg:justify-start mb-8 animate-fade-in-up delay-200">
                        <div class="flex items-center gap-2 text-gray-600">
                            <i class="fas fa-check-circle text-eco"></i>
                            <span class="text-sm">Free Samples Available</span>
                        </div>
                        <div class="flex items-center gap-2 text-gray-600">
                            <i class="fas fa-check-circle text-eco"></i>
                            <span class="text-sm">Advanced Equipment</span>
                        </div>
                        <div class="flex items-center gap-2 text-gray-600">
                            <i class="fas fa-check-circle text-eco"></i>
                            <span class="text-sm">Global Clients</span>
                        </div>
                    </div>

                        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-8 animate-fade-in-up delay-200">
                            <div class="flex items-center gap-2 text-gray-600 bg-white/80 px-4 py-2 rounded-lg">
                                <i class="fas fa-bolt text-accent"></i>
                                <span class="text-sm">24h Fast Response</span>
                            </div>
                            <div class="flex items-center gap-2 text-gray-600 bg-white/80 px-4 py-2 rounded-lg">
                                <i class="fas fa-box text-accent"></i>
                                <span class="text-sm">Low MOQ</span>
                            </div>
                            <div class="flex items-center gap-2 text-gray-600 bg-white/80 px-4 py-2 rounded-lg">
                                <i class="fas fa-sliders-h text-accent"></i>
                                <span class="text-sm">Flexible</span>
                            </div>
                            <div class="flex items-center gap-2 text-gray-600 bg-white/80 px-4 py-2 rounded-lg">
                                <i class="fas fa-check-circle text-accent"></i>
                                <span class="text-sm">Quality Guaranteed</span>
                            </div>
                        </div>'''

# Define the new hero tags section
# Unified style: all tags with white background and glass effect, 2 rows layout (4 + 3), adjusted text lengths
new_tags = '''                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-8 animate-fade-in-up delay-200">
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
                    </div>'''

# Replace the old pattern with the new one
content = content.replace(old_pattern, new_tags)

# Write the modified content back
with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Hero tags layout has been updated successfully!")
print("Changes:")
print("1. Unified all tags to white background glass effect style")
print("2. Adjusted text lengths for better balance")
print("3. 2 rows layout: 4 tags in first row, 3 tags in second row")
print("4. Second row centered (sm:col-start-2 for last tag in 4-column grid)")
print("5. Added backdrop-blur-sm for modern glass effect")
print("6. Added shadow-sm for better visual hierarchy")
print("7. Added font-medium and whitespace-nowrap for better readability")
