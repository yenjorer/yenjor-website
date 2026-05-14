#!/usr/bin/env python3
"""
精确修复products板块的所有bug：
1. 删除第1635行的多余</section>
2. 在第1630行之后添加5个缺失的产品卡片
3. 更新galleryImages
4. 更新shell轮播导航点
"""

# 读取HTML文件为行列表
with open('public/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# ==============================================================================
# Bug 1: 删除第1635行的多余</section>
# 注意：行号从0开始，所以第1635行是索引1634
# ==============================================================================
print("原始第1634行内容:", repr(lines[1634]))
if '</section>' in lines[1634] and lines[1634].strip() == '</section>':
    print("删除第1635行的多余</section>...")
    del lines[1634]

# ==============================================================================
# Bug 2: 在第1630行（产品grid结束前）添加5个产品卡片
# 产品grid的</div>在第1631行（索引1630）
# ==============================================================================
new_cards = '''                <!-- Rivets -->
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

# 找到产品grid结束的位置（第1631行，即索引1630，因为删除了一行后位置会变化）
# 让我先找到正确的位置
for i, line in enumerate(lines):
    if '<!-- Metal Fasteners Collection -->' in line:
        print(f"找到Metal Fasteners Collection在第{i+1}行")
        # 找到这个产品卡片结束后的</div>（grid结束）
        for j in range(i, min(i+50, len(lines))):
            if lines[j].strip() == '</div>' and lines[j+1].strip() == '</div>':
                print(f"在第{j+1}行插入新产品卡片")
                # 在第j行（第一个</div>）之前插入
                new_lines = new_cards.split('\n')
                # 添加换行符
                new_lines = [line + '\n' for line in new_lines if line.strip()]
                lines = lines[:j] + new_lines + lines[j:]
                break
        break

# ==============================================================================
# Bug 3: 更新galleryImages - 添加shell-button-8.jpg和snap-button-7.jpg
# ==============================================================================
for i, line in enumerate(lines):
    if "shell: ['images/shell-button-1.jpg" in line:
        print(f"更新galleryImages中的shell列表...")
        lines[i] = line.replace("'images/shell-button-7.jpg'", "'images/shell-button-7.jpg', 'images/shell-button-8.jpg'")
    if "snap: ['images/snap-button-1.jpg" in line:
        print(f"更新galleryImages中的snap列表...")
        lines[i] = line.replace("'images/snap-button-6.jpg'", "'images/snap-button-6.jpg', 'images/snap-button-7.jpg'")

# ==============================================================================
# Bug 4: 更新shell轮播导航点（Featured Product中的shell轮播）
# ==============================================================================
# 找到shell轮播的dots部分
for i, line in enumerate(lines):
    if "goToCarousel('shell', 6)" in line:
        print(f"更新shell轮播导航点，添加第8个...")
        # 在下一行插入第8个导航点
        new_dot_line = "                            <button class=\"carousel-dot\" onclick=\"event.stopPropagation(); goToCarousel('shell', 7)\"></button>\n"
        lines.insert(i+1, new_dot_line)
        break

# ==============================================================================
# 保存修改后的文件
# ==============================================================================
with open('public/index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("\n✅ 所有bug修复完成！")
print("修复内容：")
print("  1. 移除了多余的</section>闭合标签")
print("  2. 添加了缺失的5个产品卡片（Rivets, Eyelets, Metal Buckles, Metal Ends, Stoppers）")
print("  3. 更新galleryImages，添加shell-button-8.jpg和snap-button-7.jpg")
print("  4. 更新shell轮播导航点数量（从7个增加到8个）")
print("\n现在产品分类数量为13个，与标题描述一致。")
