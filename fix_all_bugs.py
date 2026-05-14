#!/usr/bin/env python3
"""
完整的网站Bug修复脚本
修复所有发现的问题：
1. 文字表述一致性
2. HTML结构问题
3. 轮播导航点匹配
4. 电话号码显示
"""

def fix_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # ============ 1. 文字表述一致性修复 ============
    # 修复 "15+ countries" 与 "50+ countries" 不一致问题
    content = content.replace(
        'Serving 15+ countries worldwide',
        'Serving 50+ countries worldwide'
    )
    
    # ============ 2. HTML结构问题修复 ============
    # 问题1: Products section后面有多余的 </section>
    # 查找 Products section 结束位置的两个 </section>
    # 当前的模式：
    #             </div>
    #         </div>
    #     </section>
    # 
    #     </section>
    # 
    #     <!-- Our Strength Section -->
    # 多余的那个 </section> 需要删除
    content = content.replace(
        '''            </div>
        </div>
    </section>

    </section>


    <!-- Our Strength Section -->''',
        '''            </div>
        </div>
    </section>

    <!-- Our Strength Section -->'''
    )
    
    # 问题2: Brand Partners section 缺少闭合的 </div>
    # 查找问题位置并添加缺少的闭合标签
    old_brands = '''                    <div class="flex items-center justify-center p-5 bg-white rounded-lg border border-gray-200 h-20">
                        <img src="images/brand-kappa-v2.png" alt="Kappa" class="max-h-9 w-auto object-contain">
                    </div>
    </section>'''
    
    new_brands = '''                    <div class="flex items-center justify-center p-5 bg-white rounded-lg border border-gray-200 h-20">
                        <img src="images/brand-kappa-v2.png" alt="Kappa" class="max-h-9 w-auto object-contain">
                    </div>
                </div>
            </div>
    </section>'''
    
    content = content.replace(old_brands, new_brands)
    
    # ============ 3. 轮播导航点匹配修复 ============
    # Coconut 轮播有4张图片，但只有3个导航点，需要添加第4个导航点
    old_coconut_dots = '''                        <div class="carousel-dots">
                            <button class="carousel-dot active" onclick="event.stopPropagation(); goToCarousel('coconut', 0)"></button>
                            <button class="carousel-dot" onclick="event.stopPropagation(); goToCarousel('coconut', 1)"></button>
                            <button class="carousel-dot" onclick="event.stopPropagation(); goToCarousel('coconut', 2)"></button>
                        </div>'''
    
    new_coconut_dots = '''                        <div class="carousel-dots">
                            <button class="carousel-dot active" onclick="event.stopPropagation(); goToCarousel('coconut', 0)"></button>
                            <button class="carousel-dot" onclick="event.stopPropagation(); goToCarousel('coconut', 1)"></button>
                            <button class="carousel-dot" onclick="event.stopPropagation(); goToCarousel('coconut', 2)"></button>
                            <button class="carousel-dot" onclick="event.stopPropagation(); goToCarousel('coconut', 3)"></button>
                        </div>'''
    
    content = content.replace(old_coconut_dots, new_coconut_dots)
    
    # ============ 4. 电话号码显示修复 ============
    # 显示完整的电话号码，而不是XXX
    content = content.replace(
        '+86 152-XXX-7811',
        '+86 152-5739-7811'
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ 已修复 {filepath}")

def main():
    html_files = [
        './public/index.html',
        './index.html'
    ]
    
    for html_file in html_files:
        fix_html_file(html_file)
    
    print("\n所有Bug修复完成！")

if __name__ == '__main__':
    main()
