#!/usr/bin/env python3
"""
Fix mobile banner tag transparency and perform overall website inspection
"""

import re

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def fix_mobile_banner_tags(html_content):
    """Fix mobile banner tag transparency"""
    
    # 1. First, add a specific class to the hero feature tags
    # Find the hero feature tags section
    old_feature_pattern = r'(<div class="flex flex-wrap justify-center lg:justify-start gap-3 mb-8 animate-fade-in-up delay-200">)(.*?)(</div>\s*<div class="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start animate-fade-in-up delay-300">)'
    
    # Replace with a class for styling
    def replace_feature_tags(match):
        opening = match.group(1)
        content = match.group(2)
        closing = match.group(3)
        
        # Replace each feature tag's bg-white/90 with a custom class
        modified_content = content.replace(
            'bg-white/90 px-4 py-2 rounded-full shadow-sm border border-gray-100',
            'hero-feature-tag bg-white/90 px-4 py-2 rounded-full shadow-sm border border-gray-100'
        )
        return opening + modified_content + closing
    
    html_content = re.sub(old_feature_pattern, replace_feature_tags, html_content, flags=re.DOTALL)
    
    # 2. Add CSS for mobile view
    # Find the existing CSS section
    css_pattern = r'(\.hero-feature i \{\s*color: var\(--color-eco-light\);\s*\})'
    
    new_css = '''\\1

        /* Hero Feature Tags - Mobile Optimization */
        .hero-feature-tag {
            background: rgba(255, 255, 255, 0.9);
        }

        @media (max-width: 768px) {
            .hero-feature-tag {
                background: rgba(255, 255, 255, 0.98) !important;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
                border-color: rgba(0, 0, 0, 0.08) !important;
            }
        }'''
    
    html_content = re.sub(css_pattern, new_css, html_content)
    
    return html_content

def inspect_website(html_content):
    """Perform overall website inspection"""
    issues = []
    checks = []
    
    # Check 1: All images exist (we'll verify common images)
    common_images = [
        'banner.jpg', 'factory.jpg', 
        'shell-button-1.jpg', 'coconut-button-1.jpg', 'horn-button-1.jpg', 'wooden-button-1.jpg',
        'cert-oeko-tex.png', 'cert-sgs.png', 'cert-grs.png', 'cert-bsci.png', 'cert-gots.png', 'cert-recycled-100.png',
        'brand-nike-v2.png', 'brand-adidas-v2.png', 'brand-zara-v2.png', 
        'brand-hm-v2.png', 'brand-uniqlo-v2.png', 'brand-kappa-v2.png'
    ]
    
    import os
    missing_images = []
    for img in common_images:
        img_path = f'./images/{img}'
        if not os.path.exists(img_path):
            missing_images.append(img)
    
    if missing_images:
        issues.append(f"Missing images: {', '.join(missing_images)}")
    else:
        checks.append("All common images present")
    
    # Check 2: All section IDs exist
    section_ids = ['home', 'about', 'products', 'strength', 'trusted', 'why-us', 'contact']
    missing_sections = []
    for sid in section_ids:
        if f'id="{sid}"' not in html_content:
            missing_sections.append(sid)
    
    if missing_sections:
        issues.append(f"Missing sections: {', '.join(missing_sections)}")
    else:
        checks.append("All navigation sections present")
    
    # Check 3: Links
    # Check if all navigation links have targets
    nav_links = re.findall(r'href="(#.*?)"', html_content)
    valid_links = set(section_ids)
    broken_links = []
    for link in nav_links:
        link_id = link.lstrip('#')
        if link_id and link_id not in valid_links:
            broken_links.append(link)
    
    if broken_links:
        issues.append(f"Potential broken anchor links: {', '.join(set(broken_links))}")
    else:
        checks.append("Navigation links validated")
    
    # Check 4: JavaScript functions
    js_functions = ['openLightbox', 'prevCarousel', 'nextCarousel', 'goToCarousel', 'toggleMobileMenu']
    missing_js = []
    for func in js_functions:
        if f'function {func}' not in html_content and f'{func}(' not in html_content:
            missing_js.append(func)
    
    if missing_js:
        issues.append(f"Missing JavaScript functions: {', '.join(missing_js)}")
    else:
        checks.append("Core JavaScript functions present")
    
    # Check 5: Mobile responsive classes
    if 'lg:hidden' in html_content and 'sm:px-6' in html_content:
        checks.append("Mobile responsive classes present")
    else:
        issues.append("Mobile responsive classes may be incomplete")
    
    return checks, issues

def main():
    html_path = './public/index.html'
    
    # Read original file
    html_content = read_file(html_path)
    
    # Inspect before changes
    print("=" * 60)
    print("WEBSITE INSPECTION REPORT")
    print("=" * 60)
    
    checks, issues = inspect_website(html_content)
    
    print("\n✅ CHECKS PASSED:")
    for check in checks:
        print(f"   - {check}")
    
    if issues:
        print("\n⚠️ ISSUES FOUND:")
        for issue in issues:
            print(f"   - {issue}")
    else:
        print("\n✅ No major issues found!")
    
    # Fix mobile banner tags
    print("\n" + "=" * 60)
    print("FIXING MOBILE BANNER TAG TRANSPARENCY")
    print("=" * 60)
    
    modified_html = fix_mobile_banner_tags(html_content)
    
    # Save backup
    backup_path = './public/index.html.backup.mobile-fix'
    write_file(backup_path, html_content)
    print(f"\n✅ Backup saved to: {backup_path}")
    
    # Save modified file
    write_file(html_path, modified_html)
    print(f"✅ Modified HTML saved to: {html_path}")
    
    # Verify changes
    if 'hero-feature-tag' in modified_html and '@media (max-width: 768px)' in modified_html:
        print("\n✅ Changes verified successfully!")
        print("\nSummary of changes:")
        print("1. Added 'hero-feature-tag' class to all banner feature tags")
        print("2. Added CSS to make tags more opaque on mobile (98% opacity)")
        print("3. Added subtle shadow on mobile for better visibility")
        print("4. Enhanced border visibility on mobile")
    else:
        print("\n⚠️ Warning: Changes may not have been applied correctly")
    
    print("\n" + "=" * 60)

if __name__ == '__main__':
    main()
