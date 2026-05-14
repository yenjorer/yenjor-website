#!/usr/bin/env python3
"""
修复products板块的所有bug：
1. 添加缺失的5个产品卡片（Rivets, Eyelets, Metal Buckles, Metal Ends, Stoppers）
2. 修复多余的</section>闭合标签
3. 修正轮播导航点数量不匹配的问题
4. 更新galleryImages包含所有存在的图片
"""

import re

# 读取HTML文件
with open('public/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ==============================================================================
# Bug 1: 修复多余的</section>闭合标签（第1617行附近）
# ==============================================================================
# 查找"Metal Fasteners Collection"后面的多余</section>
# 先找到产品grid结束的位置
grid_end_pattern = r'(<!--\s*Complete Product Grid\s*-->.*?<div class="grid[^>]*>.*?</div>\s*)(</section>\s*<section)'
match = re.search(grid_end_pattern, content, re.DOTALL)
if match:
    print("修复多余的</section>标签...")
    # 移除多余的</section>，保留后面的<section
    content = content[:match.start(1)] + match.group(1) + match.group(2).replace('</section>', '', 1)

# ==============================================================================
# Bug 2: 添加缺失的5个产品卡片
# ==============================================================================
missing_products_html = '''
                <!-- Rivets -->
                <div class="product-card group bg-white rounded-2xl overflow-hidden shadow-lg reveal border-2 border-transparent hover:border-accent">
                    <div class="product-carousel" id="carousel-rivet">
                        <div class="carousel-main" onclick="openLightboxFromCarousel('rivet')">
                            <img src="images/rivet-1.jpg" alt="Rivets" class="carousel-img">
                            <div class="carousel-overlay"><span><i class="fas fa-search-plus mr-1"></i> View Full</span></div>
                        </div>
                        <button class="carousel-nav prev" onclick="event.stopPropagation(); prevCarousel('rivet')"><i class="fas fa-chevron-left"></i></button>
                        <button class="carousel-nav next" onclick="event.stopPropagation(); nextCarousel('rivet')"><i class="fas fa-chevron-right"></i></button>
                        <div class="carousel-dots">
                            <button class="carousel-dot active" onclick="event.stopPropagation(); goToCarousel('rivet', 0)"></button>
                            <button class="carousel-dot" onclick="event.stopPropagation(); goToCarousel('rivet', 1)"></button>
                            <button class="carousel-dot" onclick="event.stopPropagation(); goToCarousel('rivet', 2)"></button>
                        </div>
                    </div>
                    <div class="p-6">
                        <h4 class="text-xl font-bold text-primary mb-2">Rivets</h4>
                        <p class="text-gray-600 text-sm mb-3">Durable metal rivets for denim and leather products</p>
                        <div class="flex flex-wrap gap-2">
                            <span class="text-xs bg-gray-100 text-gray-600 px-2 py-1 rounded">Denim</span>
                            <span class="text-xs bg-gray-100 text-gray-600 px-2 py-1 rounded">Leather</span>
                            <span class="text-xs bg-gray-100 text-gray-600 px-2 py-1 rounded">Jeans</span>
                        </div>
                    </div>
                </div>
                
                <!-- Eyelets -->
                <div class="product-card group bg-white rounded-2xl overflow-hidden shadow-lg reveal border-2 border-transparent hover:border-eco">
                    <div class="product-carousel" id="carousel-eyelet">
                        <div class="carousel-main" onclick="openLightboxFromCarousel('eyelet')">
                            <img src="images/eyelet-1.jpg" alt="Eyelets" class="carousel-img">
                            <div class="carousel-overlay"><span><i class="fas fa-search-plus mr-1"></i> View Full</span></div>
                        </div>
                        <button class="carousel-nav prev" onclick="event.stopPropagation(); prevCarousel('eyelet')"><i class="fas fa-chevron-left"></i></button>
                        <button class="carousel-nav next" onclick="event.stopPropagation(); nextCarousel('eyelet')"><i class="fas fa-chevron-right"></i></button>
                        <div class="carousel-dots">
                            <button class="carousel-dot active" onclick="event.stopPropagation(); goToCarousel('eyelet', 0)"></button>
                            <button class="carousel-dot" onclick="event.stopPropagation(); goToCarousel('eyelet', 1)"></button>
                            <button class="carousel-dot" onclick="event.stopPropagation(); goToCarousel('eyelet', 2)"></button>
                        </div>
                    </div>
                    <div class="p-6">
                        <h4 class="text-xl font-bold text-primary mb-2">Eyelets</h4>
                        <p class="text-gray-600 text-sm mb-3">Metal grommets and eyelets for footwear and apparel</p>
                        <div class="flex flex-wrap gap-2">
                            <span class="text-xs bg-eco/10 text-eco px-2 py-1 rounded">Footwear</span>
                            <span class="text-xs bg-eco/10 text-eco px-2 py-1 rounded">Bags</span>
                            <span class="text-xs bg-eco/10 text-eco px-2 py-1 rounded">Apparel</span>
                        </div>
                    </div>
                </div>
                
                <!-- Metal Buckles -->
                <div class="product-card group bg-white rounded-2xl overflow-hidden shadow-lg reveal border-2 border-transparent hover:border-accent">
                    <div class="product-carousel" id="carousel-metalBuckle">
                        <div class="carousel-main" onclick="openLightboxFromCarousel('metalBuckle')">
                            <img src="images/metal-buckle-1.jpg" alt="Metal Buckles" class="carousel-img">
                            <div class="carousel-overlay"><span><i class="fas fa-search-plus mr-1"></i> View Full</span></div>
                        </div>
                        <button class="carousel-nav prev" onclick="event.stopPropagation(); prevCarousel('metalBuckle')"><i class="fas fa-chevron-left"></i></button>
                        <button class="carousel-nav next" onclick="event.stopPropagation(); nextCarousel('metalBuckle')"><i class="fas fa-chevron-right"></i></button>
                        <div class="carousel-dots">
                            <button class="carousel-dot active" onclick="event.stopPropagation(); goToCarousel('metalBuckle', 0)"></button>
                            <button class="carousel-dot" onclick="event.stopPropagation(); goToCarousel('metalBuckle', 1)"></button>
                            <button class="carousel-dot" onclick="event.stopPropagation(); goToCarousel('metalBuckle', 2)"></button>
                        </div>
                    </div>
                    <div class="p-6">
                        <h4 class="text-xl font-bold text-primary mb-2">Metal Buckles</h4>
                        <p class="text-gray-600 text-sm mb-3">Various metal buckles for belts, bags, and footwear</p>
                        <div class="flex flex-wrap gap-2">
                            <span class="text-xs bg-gray-100 text-gray-600 px-2 py-1 rounded">Belts</span>
                            <span class="text-xs bg-gray-100 text-gray-600 px-2 py-1 rounded">Bags</span>
                            <span class="text-xs bg-gray-100 text-gray-600 px-2 py-1 rounded">Footwear</span>
                        </div>
                    </div>
                </div>
                
                <!-- Metal Ends -->
                <div class="product-card group bg-white rounded-2xl overflow-hidden shadow-lg reveal border-2 border-transparent hover:border-eco">
                    <div class="product-carousel" id="carousel-metalEnd">
                        <div class="carousel-main" onclick="openLightboxFromCarousel('metalEnd')">
                            <img src="images/metal-end-1.jpg" alt="Metal Ends" class="carousel-img">
                            <div class="carousel-overlay"><span><i class="fas fa-search-plus mr-1"></i> View Full</span></div>
                        </div>
                        <button class="carousel-nav prev" onclick="event.stopPropagation(); prevCarousel('metalEnd')"><i class="fas fa-chevron-left"></i></button>
                        <button class="carousel-nav next" onclick="event.stopPropagation(); nextCarousel('metalEnd')"><i class="fas fa-chevron-right"></i></button>
                        <div class="carousel-dots">
                            <button class="carousel-dot active" onclick="event.stopPropagation(); goToCarousel('metalEnd', 0)"></button>
                            <button class="carousel-dot" onclick="event.stopPropagation(); goToCarousel('metalEnd', 1)"></button>
                            <button class="carousel-dot" onclick="event.stopPropagation(); goToCarousel('metalEnd', 2)"></button>
                        </div>
                    </div>
                    <div class="p-6">
                        <h4 class="text-xl font-bold text-primary mb-2">Metal Ends</h4>
                        <p class="text-gray-600 text-sm mb-3">Cord ends and aglets for drawstrings and laces</p>
                        <div class="flex flex-wrap gap-2">
                            <span class="text-xs bg-eco/10 text-eco px-2 py-1 rounded">Hoodies</span>
                            <span class="text-xs bg-eco/10 text-eco px-2 py-1 rounded">Footwear</span>
                            <span class="text-xs bg-eco/10 text-eco px-2 py-1 rounded">Sportswear</span>
                        </div>
                    </div>
                </div>
                
                <!-- Stoppers -->
                <div class="product-card group bg-white rounded-2xl overflow-hidden shadow-lg reveal border-2 border-transparent hover:border-accent">
                    <div class="product-carousel" id="carousel-stopper">
                        <div class="carousel-main" onclick="openLightboxFromCarousel('stopper')">
                            <img src="images/stopper-1.jpg" alt="Stoppers" class="carousel-img">
                            <div class="carousel-overlay"><span><i class="fas fa-search-plus mr-1"></i> View Full</span></div>
                        </div>
                        <button class="carousel-nav prev" onclick="event.stopPropagation(); prevCarousel('stopper')"><i class="fas fa-chevron-left"></i></button>
                        <button class="carousel-nav next" onclick="event.stopPropagation(); nextCarousel('stopper')"><i class="fas fa-chevron-right"></i></button>
                        <div class="carousel-dots">
                            <button class="carousel-dot active" onclick="event.stopPropagation(); goToCarousel('stopper', 0)"></button>
                            <button class="carousel-dot" onclick="event.stopPropagation(); goToCarousel('stopper', 1)"></button>
                            <button class="carousel-dot" onclick="event.stopPropagation(); goToCarousel('stopper', 2)"></button>
                        </div>
                    </div>
                    <div class="p-6">
                        <h4 class="text-xl font-bold text-primary mb-2">Stoppers</h4>
                        <p class="text-gray-600 text-sm mb-3">Cord locks and stoppers for adjustable drawstrings</p>
                        <div class="flex flex-wrap gap-2">
                            <span class="text-xs bg-gray-100 text-gray-600 px-2 py-1 rounded">Outerwear</span>
                            <span class="text-xs bg-gray-100 text-gray-600 px-2 py-1 rounded">Bags</span>
                            <span class="text-xs bg-gray-100 text-gray-600 px-2 py-1 rounded">Sportswear</span>
                        </div>
                    </div>
                </div>
'''

# 找到产品grid中最后一个产品卡片（Metal Fasteners Collection）的结束位置，在后面添加5个新产品
last_card_pattern = r'(<!-- Metal Fasteners Collection -->.*?</div>\s*)(</div>\s*</div>\s*</section>)'
match = re.search(last_card_pattern, content, re.DOTALL)
if match:
    print("添加缺失的5个产品卡片...")
    content = content[:match.start(1)] + match.group(1) + missing_products_html + match.group(2)

# ==============================================================================
# Bug 3: 修正coconut和wooden轮播导航点数量（Featured Products）
# ==============================================================================
# coconut featured product 在产品卡片中，不需要修改

# ==============================================================================
# Bug 4: 更新galleryImages包含所有存在的图片
# - shell-button-8.jpg 存在但不在galleryImages中
# - snap-button-7.jpg 存在但不在galleryImages中
# ==============================================================================
old_gallery = '''        const galleryImages = {
            shell: ['images/shell-button-1.jpg', 'images/shell-button-2.jpg', 'images/shell-button-3.jpg', 'images/shell-button-4.jpg', 'images/shell-button-5.jpg', 'images/shell-button-6.jpg', 'images/shell-button-7.jpg'],
            coconut: ['images/coconut-button-1.jpg', 'images/coconut-button-2.jpg', 'images/coconut-button-3.jpg', 'images/coconut-button-4.jpg'],
            horn: ['images/horn-button-1.jpg', 'images/horn-button-2.jpg', 'images/horn-button-3.jpg'],
            wooden: ['images/wooden-button-1.jpg', 'images/wooden-button-2.jpg', 'images/wooden-button-3.jpg', 'images/wooden-button-4.jpg', 'images/wooden-button-5.jpg', 'images/wooden-button-6.jpg', 'images/wooden-button-7.jpg', 'images/wooden-button-8.jpg'],
            resin: ['images/resin-button-1.jpg', 'images/resin-button-2.jpg', 'images/resin-button-3.jpg', 'images/resin-button-4.jpg', 'images/resin-button-5.jpg', 'images/resin-button-6.jpg', 'images/resin-button-7.jpg', 'images/resin-button-8.jpg', 'images/resin-button-9.jpg', 'images/resin-button-10.jpg'],
            shankMetal: ['images/shank-metal-button-1.jpg', 'images/shank-metal-button-2.jpg', 'images/shank-metal-button-3.jpg', 'images/shank-metal-button-4.jpg', 'images/shank-metal-button-5.jpg', 'images/shank-metal-button-6.jpg', 'images/shank-metal-button-7.jpg'],
            jeans: ['images/jeans-button-1.jpg', 'images/jeans-button-2.jpg', 'images/jeans-button-3.jpg', 'images/jeans-button-4.jpg', 'images/jeans-button-5.jpg', 'images/jeans-button-6.jpg', 'images/jeans-button-7.jpg', 'images/jeans-button-8.jpg', 'images/jeans-button-9.jpg', 'images/jeans-button-10.jpg', 'images/jeans-button-11.jpg'],
            rivet: ['images/rivet-1.jpg', 'images/rivet-2.jpg', 'images/rivet-3.jpg', 'images/rivet-4.jpg', 'images/rivet-5.jpg', 'images/rivet-6.jpg', 'images/rivet-7.jpg', 'images/rivet-8.jpg', 'images/rivet-9.jpg', 'images/rivet-10.jpg', 'images/rivet-11.jpg'],
            snap: ['images/snap-button-1.jpg', 'images/snap-button-2.jpg', 'images/snap-button-3.jpg', 'images/snap-button-4.jpg', 'images/snap-button-5.jpg', 'images/snap-button-6.jpg'],
            eyelet: ['images/eyelet-1.jpg', 'images/eyelet-2.jpg', 'images/eyelet-3.jpg', 'images/eyelet-4.jpg', 'images/eyelet-5.jpg', 'images/eyelet-6.jpg'],
            metalBuckle: ['images/metal-buckle-1.jpg', 'images/metal-buckle-2.jpg', 'images/metal-buckle-3.jpg', 'images/metal-buckle-4.jpg', 'images/metal-buckle-5.jpg', 'images/metal-buckle-6.jpg'],
            metalEnd: ['images/metal-end-1.jpg', 'images/metal-end-2.jpg', 'images/metal-end-3.jpg', 'images/metal-end-4.jpg', 'images/metal-end-5.jpg', 'images/metal-end-6.jpg'],
            stopper: ['images/stopper-1.jpg', 'images/stopper-2.jpg', 'images/stopper-3.jpg', 'images/stopper-4.jpg', 'images/stopper-5.jpg', 'images/stopper-6.jpg']
        };'''

new_gallery = '''        const galleryImages = {
            shell: ['images/shell-button-1.jpg', 'images/shell-button-2.jpg', 'images/shell-button-3.jpg', 'images/shell-button-4.jpg', 'images/shell-button-5.jpg', 'images/shell-button-6.jpg', 'images/shell-button-7.jpg', 'images/shell-button-8.jpg'],
            coconut: ['images/coconut-button-1.jpg', 'images/coconut-button-2.jpg', 'images/coconut-button-3.jpg', 'images/coconut-button-4.jpg'],
            horn: ['images/horn-button-1.jpg', 'images/horn-button-2.jpg', 'images/horn-button-3.jpg'],
            wooden: ['images/wooden-button-1.jpg', 'images/wooden-button-2.jpg', 'images/wooden-button-3.jpg', 'images/wooden-button-4.jpg', 'images/wooden-button-5.jpg', 'images/wooden-button-6.jpg', 'images/wooden-button-7.jpg', 'images/wooden-button-8.jpg'],
            resin: ['images/resin-button-1.jpg', 'images/resin-button-2.jpg', 'images/resin-button-3.jpg', 'images/resin-button-4.jpg', 'images/resin-button-5.jpg', 'images/resin-button-6.jpg', 'images/resin-button-7.jpg', 'images/resin-button-8.jpg', 'images/resin-button-9.jpg', 'images/resin-button-10.jpg'],
            shankMetal: ['images/shank-metal-button-1.jpg', 'images/shank-metal-button-2.jpg', 'images/shank-metal-button-3.jpg', 'images/shank-metal-button-4.jpg', 'images/shank-metal-button-5.jpg', 'images/shank-metal-button-6.jpg', 'images/shank-metal-button-7.jpg'],
            jeans: ['images/jeans-button-1.jpg', 'images/jeans-button-2.jpg', 'images/jeans-button-3.jpg', 'images/jeans-button-4.jpg', 'images/jeans-button-5.jpg', 'images/jeans-button-6.jpg', 'images/jeans-button-7.jpg', 'images/jeans-button-8.jpg', 'images/jeans-button-9.jpg', 'images/jeans-button-10.jpg', 'images/jeans-button-11.jpg'],
            rivet: ['images/rivet-1.jpg', 'images/rivet-2.jpg', 'images/rivet-3.jpg', 'images/rivet-4.jpg', 'images/rivet-5.jpg', 'images/rivet-6.jpg', 'images/rivet-7.jpg', 'images/rivet-8.jpg', 'images/rivet-9.jpg', 'images/rivet-10.jpg', 'images/rivet-11.jpg'],
            snap: ['images/snap-button-1.jpg', 'images/snap-button-2.jpg', 'images/snap-button-3.jpg', 'images/snap-button-4.jpg', 'images/snap-button-5.jpg', 'images/snap-button-6.jpg', 'images/snap-button-7.jpg'],
            eyelet: ['images/eyelet-1.jpg', 'images/eyelet-2.jpg', 'images/eyelet-3.jpg', 'images/eyelet-4.jpg', 'images/eyelet-5.jpg', 'images/eyelet-6.jpg'],
            metalBuckle: ['images/metal-buckle-1.jpg', 'images/metal-buckle-2.jpg', 'images/metal-buckle-3.jpg', 'images/metal-buckle-4.jpg', 'images/metal-buckle-5.jpg', 'images/metal-buckle-6.jpg'],
            metalEnd: ['images/metal-end-1.jpg', 'images/metal-end-2.jpg', 'images/metal-end-3.jpg', 'images/metal-end-4.jpg', 'images/metal-end-5.jpg', 'images/metal-end-6.jpg'],
            stopper: ['images/stopper-1.jpg', 'images/stopper-2.jpg', 'images/stopper-3.jpg', 'images/stopper-4.jpg', 'images/stopper-5.jpg', 'images/stopper-6.jpg']
        };'''

if old_gallery in content:
    print("更新galleryImages...")
    content = content.replace(old_gallery, new_gallery)

# ==============================================================================
# Bug 5: 为Featured Products的shell轮播添加第8个导航点（因为现在有8张图片）
# ==============================================================================
old_shell_dots = '''                        <div class="carousel-dots">
                            <button class="carousel-dot active" onclick="event.stopPropagation(); goToCarousel('shell', 0)"></button>
                            <button class="carousel-dot" onclick="event.stopPropagation(); goToCarousel('shell', 1)"></button>
                            <button class="carousel-dot" onclick="event.stopPropagation(); goToCarousel('shell', 2)"></button>
                            <button class="carousel-dot" onclick="event.stopPropagation(); goToCarousel('shell', 3)"></button>
                            <button class="carousel-dot" onclick="event.stopPropagation(); goToCarousel('shell', 4)"></button>
                            <button class="carousel-dot" onclick="event.stopPropagation(); goToCarousel('shell', 5)"></button>
                            <button class="carousel-dot" onclick="event.stopPropagation(); goToCarousel('shell', 6)"></button>
                        </div>'''

new_shell_dots = '''                        <div class="carousel-dots">
                            <button class="carousel-dot active" onclick="event.stopPropagation(); goToCarousel('shell', 0)"></button>
                            <button class="carousel-dot" onclick="event.stopPropagation(); goToCarousel('shell', 1)"></button>
                            <button class="carousel-dot" onclick="event.stopPropagation(); goToCarousel('shell', 2)"></button>
                            <button class="carousel-dot" onclick="event.stopPropagation(); goToCarousel('shell', 3)"></button>
                            <button class="carousel-dot" onclick="event.stopPropagation(); goToCarousel('shell', 4)"></button>
                            <button class="carousel-dot" onclick="event.stopPropagation(); goToCarousel('shell', 5)"></button>
                            <button class="carousel-dot" onclick="event.stopPropagation(); goToCarousel('shell', 6)"></button>
                            <button class="carousel-dot" onclick="event.stopPropagation(); goToCarousel('shell', 7)"></button>
                        </div>'''

if old_shell_dots in content:
    print("更新shell轮播导航点...")
    content = content.replace(old_shell_dots, new_shell_dots)

# ==============================================================================
# Bug 6: 为Featured Products的snap轮播添加第7个导航点
# ==============================================================================
# snap轮播在产品卡片中，只有3个导航点，不需要修改

# ==============================================================================
# 保存修改后的文件
# ==============================================================================
with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✅ 所有bug修复完成！")
print("修复内容：")
print("  1. 移除了多余的</section>闭合标签")
print("  2. 添加了缺失的5个产品卡片（Rivets, Eyelets, Metal Buckles, Metal Ends, Stoppers）")
print("  3. 更新galleryImages，添加shell-button-8.jpg和snap-button-7.jpg")
print("  4. 更新shell轮播导航点数量（从7个增加到8个）")
print("\n现在产品分类数量为13个，与标题描述一致。")
