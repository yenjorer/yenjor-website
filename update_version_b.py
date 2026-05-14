#!/usr/bin/env python3
import re

def update_html_file():
    file_path = 'index.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # ================================
    # 1. Update Hero (Banner) Section
    # ================================
    
    # Update main heading
    old_heading = '''                    <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold text-gray-900 leading-tight mb-6 animate-fade-in-up delay-100">
                        Premium Buttons for&lt;br&gt;
                        <span class="text-accent">Fashion Brands.</span>
                    </h1>'''
    
    new_heading = '''                    <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold text-gray-900 leading-tight mb-6 animate-fade-in-up delay-100 text-center lg:text-left">
                        Buttons Made Easy.
                    </h1>'''
    
    content = content.replace(old_heading, new_heading)
    
    # Update subtitle
    old_subtitle = '''                    <p class="text-gray-600 text-lg md:text-xl mb-8 max-w-xl animate-fade-in-up delay-200">
                        Leading manufacturer of metal buttons and resin buttons. 
                        Two decades of factory expertise serving garment factories, brands, and SOHO buyers worldwide.
                    </p>'''
    
    new_subtitle = '''                    <p class="text-gray-600 text-lg md:text-xl mb-8 max-w-xl animate-fade-in-up delay-200 text-center lg:text-left mx-auto lg:mx-0">
                        Yenjor — China\'s trusted button factory. 20 years making metal & resin buttons for garment factories and brands worldwide.
                    </p>'''
    
    content = content.replace(old_subtitle, new_subtitle)
    
    # Update selling points - replace the two sections with a single clean row
    old_selling_points_1 = '''                    <div class="flex flex-wrap gap-4 justify-center lg:justify-start mb-8 animate-fade-in-up delay-200">
                        <div class="flex items-center gap-2 text-gray-600">
                            <i class="fas fa-check-circle text-eco"></i>
                            <span class="text-sm">Free Samples Available</span>
                        </div>
                        <div class="flex items-center gap-2 text-gray-600">
                            <i class="fas fa-check-circle text-eco"></i>
                            <span class="text-sm">Small Batch Support</span>
                        </div>
                        <div class="flex items-center gap-2 text-gray-600">
                            <i class="fas fa-check-circle text-eco"></i>
                            <span class="text-sm">OEM/ODM Custom</span>
                        </div>
                    </div>

                        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-8 animate-fade-in-up delay-200">
                            <div class="flex items-center gap-2 text-gray-600 bg-white/80 px-4 py-2 rounded-lg">
                                <i class="fas fa-bolt text-accent"></i>
                                <span class="text-sm">24h Fast Response</span>
                            </div>
                            <div class="flex items-center gap-2 text-gray-600 bg-white/80 px-4 py-2 rounded-lg">
                                <i class="fas fa-sliders-h text-accent"></i>
                                <span class="text-sm">Low MOQ Flexible</span>
                            </div>
                            <div class="flex items-center gap-2 text-gray-600 bg-white/80 px-4 py-2 rounded-lg">
                                <i class="fas fa-check-circle text-accent"></i>
                                <span class="text-sm">Quality Guaranteed</span>
                            </div>
                        </div>'''
    
    new_selling_points = '''                    <div class="flex flex-wrap justify-center lg:justify-start gap-3 mb-8 animate-fade-in-up delay-200">
                        <div class="flex items-center gap-2 text-gray-600 bg-white/90 px-4 py-2 rounded-full shadow-sm border border-gray-100">
                            <i class="fas fa-gift text-accent"></i>
                            <span class="text-sm font-medium">Free Samples</span>
                        </div>
                        <div class="flex items-center gap-2 text-gray-600 bg-white/90 px-4 py-2 rounded-full shadow-sm border border-gray-100">
                            <i class="fas fa-file-invoice-dollar text-accent"></i>
                            <span class="text-sm font-medium">Fast Quotes</span>
                        </div>
                        <div class="flex items-center gap-2 text-gray-600 bg-white/90 px-4 py-2 rounded-full shadow-sm border border-gray-100">
                            <i class="fas fa-boxes text-accent"></i>
                            <span class="text-sm font-medium">Low MOQ</span>
                        </div>
                        <div class="flex items-center gap-2 text-gray-600 bg-white/90 px-4 py-2 rounded-full shadow-sm border border-gray-100">
                            <i class="fas fa-clock text-accent"></i>
                            <span class="text-sm font-medium">24hr Reply</span>
                        </div>
                        <div class="flex items-center gap-2 text-gray-600 bg-white/90 px-4 py-2 rounded-full shadow-sm border border-gray-100">
                            <i class="fas fa-tags text-accent"></i>
                            <span class="text-sm font-medium">Good Prices</span>
                        </div>
                        <div class="flex items-center gap-2 text-gray-600 bg-white/90 px-4 py-2 rounded-full shadow-sm border border-gray-100">
                            <i class="fas fa-shipping-fast text-accent"></i>
                            <span class="text-sm font-medium">Ship Worldwide</span>
                        </div>
                    </div>'''
    
    content = content.replace(old_selling_points_1, new_selling_points)
    
    # ================================
    # 2. Update About Us Section
    # ================================
    
    # Update About section title
    old_about_title = '''                    <h2 class="text-3xl md:text-4xl lg:text-5xl font-bold text-primary mb-6 leading-tight">
                        Your Trusted Partner for&lt;br&gt;
                        <span class="text-accent">Quality Button Solutions</span>
                    </h2>'''
    
    new_about_title = '''                    <h2 class="text-3xl md:text-4xl lg:text-5xl font-bold text-primary mb-6 leading-tight">
                        Your Reliable Button Manufacturer
                    </h2>'''
    
    content = content.replace(old_about_title, new_about_title)
    
    # Update About section content - replace the existing paragraphs and grid
    old_about_content = '''                    <p class="text-gray-600 text-lg mb-6 leading-relaxed">
                        <strong>Established in 2003 with two decades of manufacturing expertise</strong>, we specialize in 
                        <strong>metal buttons</strong>, <strong>resin buttons</strong>, and garment accessories. 
                        Located in the Yangtze River Delta near Shanghai, with convenient access to Shanghai and 
                        Ningbo ports for global shipping.
                    </p>
                    <p class="text-gray-600 text-lg mb-6 leading-relaxed">
                        Our products are trusted by garment factories, fashion brands, and wholesalers across 
                        <strong>Southeast Asia</strong> (Bangladesh, Vietnam), <strong>Europe</strong>, 
                        and <strong>America</strong> — 50+ countries worldwide.
                    </p>

                    <div class="grid grid-cols-2 gap-6 mb-8">
                        <div class="flex items-start gap-4">
                            <div class="w-12 h-12 bg-accent/20 rounded-lg flex items-center justify-center flex-shrink-0">
                                <i class="fas fa-check text-accent text-xl"></i>
                            </div>
                            <div>
                                <h4 class="font-semibold text-primary">Small Batch Support</h4>
                                <p class="text-gray-500 text-sm">Perfect for SOHO buyers</p>
                            </div>
                        </div>
                        <div class="flex items-start gap-4">
                            <div class="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center flex-shrink-0">
                                <i class="fas fa-globe text-blue-500 text-xl"></i>
                            </div>
                            <div>
                                <h4 class="font-semibold text-primary">Global Reach</h4>
                                <p class="text-gray-500 text-sm">50+ countries served</p>
                            </div>
                        </div>
                        <div class="flex items-start gap-4">
                            <div class="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center flex-shrink-0">
                                <i class="fas fa-bolt text-blue-500 text-xl"></i>
                            </div>
                            <div>
                                <h4 class="font-semibold text-primary">Fast Sample</h4>
                                <p class="text-gray-500 text-sm">7 days sample lead time</p>
                            </div>
                        </div>
                        <div class="flex items-start gap-4">
                            <div class="w-12 h-12 bg-accent/20 rounded-lg flex items-center justify-center flex-shrink-0">
                                <i class="fas fa-check text-accent text-xl"></i>
                            </div>
                            <div>
                                <h4 class="font-semibold text-primary">OEM/ODM Service</h4>
                                <p class="text-gray-500 text-sm">Custom design available</p>
                            </div>
                        </div>
                    </div>'''
    
    new_about_content = '''                    <p class="text-gray-600 text-lg mb-8 leading-relaxed text-justify">
                        Yenjor is a professional button manufacturer based in the Yangtze River Delta, China.
                    </p>
                    
                    <div class="space-y-4 mb-8">
                        <div class="flex items-start gap-4">
                            <span class="text-accent font-bold text-xl mt-0.5">•</span>
                            <div class="flex-1">
                                <h4 class="font-semibold text-primary">20+ years manufacturing experience</h4>
                            </div>
                        </div>
                        <div class="flex items-start gap-4">
                            <span class="text-accent font-bold text-xl mt-0.5">•</span>
                            <div class="flex-1">
                                <h4 class="font-semibold text-primary">3,000㎡ modern production facility</h4>
                            </div>
                        </div>
                        <div class="flex items-start gap-4">
                            <span class="text-accent font-bold text-xl mt-0.5">•</span>
                            <div class="flex-1">
                                <h4 class="font-semibold text-primary">100+ skilled workers</h4>
                            </div>
                        </div>
                        <div class="flex items-start gap-4">
                            <span class="text-accent font-bold text-xl mt-0.5">•</span>
                            <div class="flex-1">
                                <h4 class="font-semibold text-primary">Metal buttons & resin buttons</h4>
                            </div>
                        </div>
                        <div class="flex items-start gap-4">
                            <span class="text-accent font-bold text-xl mt-0.5">•</span>
                            <div class="flex-1">
                                <h4 class="font-semibold text-primary">Serving 15+ countries worldwide</h4>
                            </div>
                        </div>
                    </div>
                    
                    <p class="text-gray-600 text-lg mb-8 leading-relaxed text-justify">
                        We make quality buttons at competitive prices. Simple. Reliable. Fast.
                    </p>'''
    
    content = content.replace(old_about_content, new_about_content)
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✓ Version B content updated successfully")
    print("  - Banner heading: 'Buttons Made Easy.'")
    print("  - Banner subtitle updated")
    print("  - Banner selling points: 6 items with perfect alignment")
    print("  - About title: 'Your Reliable Button Manufacturer'")
    print("  - About content with bullet points, text justified")

if __name__ == '__main__':
    update_html_file()
