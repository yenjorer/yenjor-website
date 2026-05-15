#!/usr/bin/env python3

with open('public/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到Hero Section的开始和结束位置
hero_start = content.find('    <!-- Hero Section -->')
hero_end = content.find('    <!-- About Section -->', hero_start)

old_hero = content[hero_start:hero_end]

# 新的banner内容，恢复到5月13日及以前的样式和内容
new_hero = '''    <!-- Hero Section -->
    <section id="home" class="hero-gradient min-h-screen flex items-center pt-20">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
            <div class="grid lg:grid-cols-2 gap-12 items-center">
                <div class="text-center lg:text-left">
                    <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold text-gray-900 leading-tight mb-6 animate-fade-in-up delay-100">
                        Premium Buttons for<br>
                        <span class="text-accent">Fashion Brands.</span>
                    </h1>
                    <p class="text-gray-600 text-lg md:text-xl mb-8 max-w-xl animate-fade-in-up delay-200">
                        Leading manufacturer of metal buttons and resin buttons. 
                        Two decades of factory expertise serving garment factories, brands, and SOHO buyers worldwide.
                    </p>
                    <div class="flex flex-wrap justify-center lg:justify-start gap-3 mb-8 animate-fade-in-up delay-200">
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
                    </div>
                    <div class="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start animate-fade-in-up delay-300">
                        <a href="#contact" class="px-8 py-4 rounded-full font-semibold text-lg border-2 border-gray-300 text-gray-700 hover:bg-gray-100 hover:text-gray-900 transition-all inline-flex items-center justify-center gap-2">
                            <i class="fas fa-envelope"></i>
                            <span>Get Quote</span>
                        </a>
                    </div>
                </div>
                <div class="relative animate-fade-in delay-400">
                    <img src="images/banner.jpg" 
                         alt="Yenjor Quality Buttons" 
                         class="rounded-2xl shadow-2xl w-full"
                         style="aspect-ratio: 16/9; object-fit: cover;">
                    <div class="absolute -bottom-6 -left-6 bg-white/15 backdrop-blur-xl p-6 rounded-xl shadow-2xl border border-white/20 ring-1 ring-white/10">
                        <div class="flex items-center gap-4">
                            <div class="w-14 h-14 bg-amber-500/20 rounded-full flex items-center justify-center">
                                <i class="fas fa-award text-accent text-2xl"></i>
                            </div>
                            <div>
                                <p class="text-3xl font-bold text-white">20+</p>
                                <p class="text-gray-300 text-sm">Years Experience</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->'''

new_content = content[:hero_start] + new_hero + content[hero_end + len('    <!-- About Section -->'):]

with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Banner restored successfully!")
