import re

# Read the HTML file
with open('public/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the position between subtitle and button in hero section
# The pattern: </p> followed by the button div
old_pattern = r'(<p class="text-gray-600 text-lg md:text-xl mb-10 max-w-xl animate-fade-in-up delay-200">.*?</p>)(\s*)(<div class="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start animate-fade-in-up delay-300">)'

# New tags HTML
tags_html = '''
                    <!-- Hero Selling Tags -->
                    <div class="flex flex-wrap gap-3 justify-center lg:justify-start mb-8 animate-fade-in-up delay-250">
                        <span class="px-5 py-2.5 bg-white/70 backdrop-blur-md rounded-full text-sm font-medium text-gray-700 shadow-lg border border-white/50">
                            <i class="fas fa-gift text-accent mr-2"></i>Free Samples
                        </span>
                        <span class="px-5 py-2.5 bg-white/70 backdrop-blur-md rounded-full text-sm font-medium text-gray-700 shadow-lg border border-white/50">
                            <i class="fas fa-microchip text-accent mr-2"></i>Advanced Tech
                        </span>
                        <span class="px-5 py-2.5 bg-white/70 backdrop-blur-md rounded-full text-sm font-medium text-gray-700 shadow-lg border border-white/50">
                            <i class="fas fa-globe-americas text-accent mr-2"></i>Global Clients
                        </span>
                    </div>'''

# Replace
new_content = re.sub(old_pattern, r'\1' + tags_html + r'\2\3', content, flags=re.DOTALL)

# Write back
with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Hero tags added successfully!")
