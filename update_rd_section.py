#!/usr/bin/env python3
"""
Update R&D section to be more pragmatic and SOHO-style
"""

import re

def update_rd_section():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update R&D Team: 10人 → 3-5人核心骨干，创始人亲自带队，每人10年+经验
    # Update team count card
    content = re.sub(
        r'<div class="text-3xl font-bold text-primary mb-2">10</div>\s*<div class="text-sm text-gray-600">Total R&D Personnel</div>',
        '<div class="text-3xl font-bold text-primary mb-2">3-5</div>\n<div class="text-sm text-gray-600">Core R&D Members</div>',
        content
    )
    
    # Update team structure - simplify to SOHO style
    old_team_cards = r'''<div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
                        <div class="bg-gray-50 rounded-2xl p-6 text-center hover:shadow-lg transition-shadow">
                            <div class="w-14 h-14 bg-accent/20 rounded-xl flex items-center justify-center mx-auto mb-4">
                                <i class="fas fa-user-tie text-accent text-2xl"></i>
                            </div>
                            <div class="text-3xl font-bold text-primary mb-2">3-5</div>
                            <div class="text-sm text-gray-600">Core R&D Members</div>
                        </div>
                        <div class="bg-gray-50 rounded-2xl p-6 text-center hover:shadow-lg transition-shadow">
                            <div class="w-14 h-14 bg-blue-100 rounded-xl flex items-center justify-center mx-auto mb-4">
                                <i class="fas fa-flask text-blue-500 text-2xl"></i>
                            </div>
                            <div class="text-3xl font-bold text-primary mb-2">2</div>
                            <div class="text-sm text-gray-600">Material Engineers</div>
                        </div>
                        <div class="bg-gray-50 rounded-2xl p-6 text-center hover:shadow-lg transition-shadow">
                            <div class="w-14 h-14 bg-purple-100 rounded-xl flex items-center justify-center mx-auto mb-4">
                                <i class="fas fa-paint-brush text-purple-500 text-2xl"></i>
                            </div>
                            <div class="text-3xl font-bold text-primary mb-2">4</div>
                            <div class="text-sm text-gray-600">Designers & CAD Experts</div>
                        </div>
                        <div class="bg-gray-50 rounded-2xl p-6 text-center hover:shadow-lg transition-shadow">
                            <div class="w-14 h-14 bg-green-100 rounded-xl flex items-center justify-center mx-auto mb-4">
                                <i class="fas fa-cogs text-green-500 text-2xl"></i>
                            </div>
                            <div class="text-3xl font-bold text-primary mb-2">3</div>
                            <div class="text-sm text-gray-600">Technical Specialists</div>
                            <div class="text-xs text-gray-400 mt-1">+1 R&D Director</div>
                        </div>
                    </div>'''
    
    new_team_cards = '''<div class="grid md:grid-cols-3 gap-6">
                        <div class="bg-gray-50 rounded-2xl p-6 text-center hover:shadow-lg transition-shadow">
                            <div class="w-14 h-14 bg-accent/20 rounded-xl flex items-center justify-center mx-auto mb-4">
                                <i class="fas fa-user-tie text-accent text-2xl"></i>
                            </div>
                            <div class="text-3xl font-bold text-primary mb-2">3-5</div>
                            <div class="text-sm text-gray-600">Core Members</div>
                        </div>
                        <div class="bg-gray-50 rounded-2xl p-6 text-center hover:shadow-lg transition-shadow">
                            <div class="w-14 h-14 bg-blue-100 rounded-xl flex items-center justify-center mx-auto mb-4">
                                <i class="fas fa-star text-blue-500 text-2xl"></i>
                            </div>
                            <div class="text-3xl font-bold text-primary mb-2">10+</div>
                            <div class="text-sm text-gray-600">Avg. Years Exp</div>
                        </div>
                        <div class="bg-gray-50 rounded-2xl p-6 text-center hover:shadow-lg transition-shadow">
                            <div class="w-14 h-14 bg-green-100 rounded-xl flex items-center justify-center mx-auto mb-4">
                                <i class="fas fa-handshake text-green-500 text-2xl"></i>
                            </div>
                            <div class="text-3xl font-bold text-primary mb-2">1</div>
                            <div class="text-sm text-gray-600">Founder-led</div>
                        </div>
                    </div>'''
    
    content = re.sub(re.escape(old_team_cards), new_team_cards, content)
    
    # 2. & 3. & 4. Update R&D stats: 2.8% → 1-2%, 6+ → 10+, 42 → 15-25
    old_stats = '''<div class="flex items-center justify-center gap-8 flex-wrap">
                            <div class="text-center">
                                <div class="text-2xl font-bold text-accent">2.8%</div>
                                <div class="text-sm text-gray-600">Annual R&D Investment</div>
                            </div>
                            <div class="text-gray-300 text-2xl">|</div>
                            <div class="text-center">
                                <div class="text-2xl font-bold text-accent">6+</div>
                                <div class="text-sm text-gray-600">Avg. Years Experience</div>
                            </div>
                            <div class="text-gray-300 text-2xl">|</div>
                            <div class="text-center">
                                <div class="text-2xl font-bold text-accent">42</div>
                                <div class="text-sm text-gray-600">New Products/Year</div>
                            </div>
                        </div>'''
    
    new_stats = '''<div class="flex items-center justify-center gap-8 flex-wrap">
                            <div class="text-center">
                                <div class="text-2xl font-bold text-accent">1-2%</div>
                                <div class="text-sm text-gray-600">Annual R&D Investment</div>
                            </div>
                            <div class="text-gray-300 text-2xl">|</div>
                            <div class="text-center">
                                <div class="text-2xl font-bold text-accent">10+</div>
                                <div class="text-sm text-gray-600">Avg. Years Experience</div>
                            </div>
                            <div class="text-gray-300 text-2xl">|</div>
                            <div class="text-center">
                                <div class="text-2xl font-bold text-accent">15-25</div>
                                <div class="text-sm text-gray-600">New Styles/Year</div>
                            </div>
                        </div>'''
    
    content = re.sub(re.escape(old_stats), new_stats, content)
    
    # 5. Update Laboratory - simplify to pragmatic SOHO style
    old_lab_section = '''<!-- Laboratory & Testing Capabilities -->
                <div class="reveal">
                    <h3 class="text-2xl font-bold text-primary mb-8 text-center">
                        <i class="fas fa-vials text-accent mr-3"></i>Laboratory & Testing Capabilities
                    </h3>
                    <div class="grid md:grid-cols-3 gap-6">
                        <div class="feature-card rounded-2xl p-6">
                            <div class="flex items-start gap-4">
                                <div class="w-12 h-12 bg-accent/20 rounded-lg flex items-center justify-center flex-shrink-0">
                                    <i class="fas fa-certificate text-accent text-xl"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold text-primary mb-2">In-House Basic Lab</h4>
                                    <p class="text-sm text-gray-600">Self-operated basic testing facility, with SGS & ITS third-party partnerships for comprehensive certification and compliance testing.</p>
                                </div>
                            </div>
                        </div>
                        <div class="feature-card rounded-2xl p-6">
                            <div class="flex items-start gap-4">
                                <div class="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center flex-shrink-0">
                                    <i class="fas fa-thermometer-half text-blue-500 text-xl"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold text-primary mb-2">Environmental Testing</h4>
                                    <p class="text-sm text-gray-600">Temperature cycling, humidity resistance, and corrosion testing chambers for durability validation.</p>
                                </div>
                            </div>
                        </div>
                        <div class="feature-card rounded-2xl p-6">
                            <div class="flex items-start gap-4">
                                <div class="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center flex-shrink-0">
                                    <i class="fas fa-tint text-purple-500 text-xl"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold text-primary mb-2">Chemical Analysis</h4>
                                    <p class="text-sm text-gray-600">Spectrometers and chromatography equipment for material composition and heavy metal testing.</p>
                                </div>
                            </div>
                        </div>
                        <div class="feature-card rounded-2xl p-6">
                            <div class="flex items-start gap-4">
                                <div class="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center flex-shrink-0">
                                    <i class="fas fa-bullseye text-green-500 text-xl"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold text-primary mb-2">Physical Testing</h4>
                                    <p class="text-sm text-gray-600">Tensile strength, abrasion resistance, and impact testing to verify mechanical performance.</p>
                                </div>
                            </div>
                        </div>
                        <div class="feature-card rounded-2xl p-6">
                            <div class="flex items-start gap-4">
                                <div class="w-12 h-12 bg-orange-100 rounded-lg flex items-center justify-center flex-shrink-0">
                                    <i class="fas fa-tshirt text-orange-500 text-xl"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold text-primary mb-2">Wash & Wear Testing</h4>
                                    <p class="text-sm text-gray-600">Industrial wash simulation, color fastness, and dry cleaning resistance evaluation.</p>
                                </div>
                            </div>
                        </div>
                        <div class="feature-card rounded-2xl p-6">
                            <div class="flex items-start gap-4">
                                <div class="w-12 h-12 bg-red-100 rounded-lg flex items-center justify-center flex-shrink-0">
                                    <i class="fas fa-check-double text-red-500 text-xl"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold text-primary mb-2">Compliance Standards</h4>
                                    <p class="text-sm text-gray-600">Follow ISO 10993, GB/T 21655, OEKO-TEX Standard 100, and REACH regulations.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>'''
    
    new_lab_section = '''<!-- Laboratory & Testing Capabilities -->
                <div class="reveal">
                    <h3 class="text-2xl font-bold text-primary mb-8 text-center">
                        <i class="fas fa-vials text-accent mr-3"></i>Quality Testing & Certification
                    </h3>
                    <div class="grid md:grid-cols-2 gap-6 max-w-3xl mx-auto">
                        <div class="feature-card rounded-2xl p-6">
                            <div class="flex items-start gap-4">
                                <div class="w-12 h-12 bg-accent/20 rounded-lg flex items-center justify-center flex-shrink-0">
                                    <i class="fas fa-check-circle text-accent text-xl"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold text-primary mb-2">Basic In-House QC</h4>
                                    <p class="text-sm text-gray-600">Practical visual inspection and basic functional testing for every batch before shipment.</p>
                                </div>
                            </div>
                        </div>
                        <div class="feature-card rounded-2xl p-6">
                            <div class="flex items-start gap-4">
                                <div class="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center flex-shrink-0">
                                    <i class="fas fa-handshake text-blue-500 text-xl"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold text-primary mb-2">SGS & ITS Partnership</h4>
                                    <p class="text-sm text-gray-600">Work with trusted third-party labs for professional certification and compliance testing when needed.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>'''
    
    content = re.sub(re.escape(old_lab_section), new_lab_section, content)
    
    # 6. Update Patents: 19项 → 3-5项核心专利
    old_patents_section = '''<!-- Patents & Intellectual Property -->
                <div class="reveal">
                    <h3 class="text-2xl font-bold text-primary mb-8 text-center">
                        <i class="fas fa-lightbulb text-accent mr-3"></i>Patents & Intellectual Property
                    </h3>
                    <div class="bg-gray-50 rounded-2xl p-8">
                        <div class="grid md:grid-cols-3 gap-8 mb-8">
                            <div class="text-center">
                                <div class="w-20 h-20 bg-accent/20 rounded-full flex items-center justify-center mx-auto mb-4">
                                    <i class="fas fa-award text-accent text-3xl"></i>
                                </div>
                                <div class="text-4xl font-bold text-primary mb-2">19</div>
                                <div class="text-gray-600">Total Patents Granted</div>
                            </div>
                            <div class="text-center">
                                <div class="w-20 h-20 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-4">
                                    <i class="fas fa-cogs text-blue-500 text-3xl"></i>
                                </div>
                                <div class="text-4xl font-bold text-primary mb-2">4</div>
                                <div class="text-gray-600">Invention Patents</div>
                            </div>
                            <div class="text-center">
                                <div class="w-20 h-20 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
                                    <i class="fas fa-shapes text-green-500 text-3xl"></i>
                                </div>
                                <div class="text-4xl font-bold text-primary mb-2">12</div>
                                <div class="text-gray-600">Utility Models</div>
                            </div>
                            <div class="text-center">
                                <div class="w-20 h-20 bg-purple-100 rounded-full flex items-center justify-center mx-auto mb-4">
                                    <i class="fas fa-palette text-purple-500 text-3xl"></i>
                                </div>
                                <div class="text-4xl font-bold text-primary mb-2">3</div>
                                <div class="text-gray-600">Design Patents</div>
                            </div>
                        </div>
                        <div class="grid md:grid-cols-2 gap-4">
                            <div class="bg-white rounded-xl p-4 flex items-center gap-3">
                                <i class="fas fa-layer-group text-accent text-xl"></i>
                                <div>
                                    <div class="font-semibold text-primary">Material Innovation</div>
                                    <div class="text-sm text-gray-500">3 patents on biodegradable resin formulations</div>
                                </div>
                            </div>
                            <div class="bg-white rounded-xl p-4 flex items-center gap-3">
                                <i class="fas fa-industry text-accent text-xl"></i>
                                <div>
                                    <div class="font-semibold text-primary">Process Technology</div>
                                    <div class="text-sm text-gray-500">6 patents on electroplating & coating processes</div>
                                </div>
                            </div>
                            <div class="bg-white rounded-xl p-4 flex items-center gap-3">
                                <i class="fas fa-puzzle-piece text-accent text-xl"></i>
                                <div>
                                    <div class="font-semibold text-primary">Structure Design</div>
                                    <div class="text-sm text-gray-500">4 patents on button mechanical structures</div>
                                </div>
                            </div>
                            <div class="bg-white rounded-xl p-4 flex items-center gap-3">
                                <i class="fas fa-copyright text-accent text-xl"></i>
                                <div>
                                    <div class="font-semibold text-primary">Design Patents</div>
                                    <div class="text-sm text-gray-500">3 design patents for decorative button patterns</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>'''
    
    new_patents_section = '''<!-- Technical Know-how -->
                <div class="reveal">
                    <h3 class="text-2xl font-bold text-primary mb-8 text-center">
                        <i class="fas fa-lightbulb text-accent mr-3"></i>Technical Know-how & Experience
                    </h3>
                    <div class="bg-gray-50 rounded-2xl p-8 max-w-3xl mx-auto">
                        <div class="grid md:grid-cols-2 gap-8 mb-8">
                            <div class="text-center">
                                <div class="w-20 h-20 bg-accent/20 rounded-full flex items-center justify-center mx-auto mb-4">
                                    <i class="fas fa-award text-accent text-3xl"></i>
                                </div>
                                <div class="text-4xl font-bold text-primary mb-2">3-5</div>
                                <div class="text-gray-600">Core Techniques</div>
                            </div>
                            <div class="text-center">
                                <div class="w-20 h-20 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-4">
                                    <i class="fas fa-star text-blue-500 text-3xl"></i>
                                </div>
                                <div class="text-4xl font-bold text-primary mb-2">20+</div>
                                <div class="text-gray-600">Years Experience</div>
                            </div>
                        </div>
                        <div class="text-center text-gray-600">
                            <p class="mb-4">Rather than focusing on patents, we focus on practical production expertise that delivers real value to our customers.</p>
                            <p>Our core strength lies in proven manufacturing techniques that save costs and improve quality for your button orders.</p>
                        </div>
                    </div>
                </div>'''
    
    content = re.sub(re.escape(old_patents_section), new_patents_section, content)
    
    # 7. Update Case Studies - change to 3 "帮客户省成本" cases
    old_cases_section = '''<!-- Collaboration Cases -->
                <div class="reveal">
                    <h3 class="text-2xl font-bold text-primary mb-8 text-center">
                        <i class="fas fa-lightbulb text-accent mr-3"></i>Innovation Case Studies
                    </h3>
                    <div class="grid md:grid-cols-2 gap-6">
                        <div class="feature-card rounded-2xl p-6">
                                <div class="flex items-start gap-4">
                                    <div class="w-14 h-14 bg-blue-100 rounded-xl flex items-center justify-center flex-shrink-0">
                                        <i class="fas fa-magnet text-blue-500 text-2xl"></i>
                                    </div>
                                    <div>
                                        <h4 class="font-bold text-primary mb-2">Magnetic Button Series</h4>
                                        <p class="text-sm text-gray-600 mb-3">Innovative magnetic closure button line for easy one-hand operation on jackets and coats</p>
                                        <div class="flex flex-wrap gap-2">
                                            <span class="bg-blue-100 text-blue-600 text-xs px-2 py-1 rounded">2 Utility Patents</span>
                                            <span class="bg-blue-100 text-blue-600 text-xs px-2 py-1 rounded">8 SKUs</span>
                                            <span class="bg-blue-100 text-blue-600 text-xs px-2 py-1 rounded">Launched 2023</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        <div class="feature-card rounded-2xl p-6">
                                <div class="flex items-start gap-4">
                                    <div class="w-14 h-14 bg-purple-100 rounded-xl flex items-center justify-center flex-shrink-0">
                                        <i class="fas fa-thermometer-half text-purple-500 text-2xl"></i>
                                    </div>
                                    <div>
                                        <h4 class="font-bold text-primary mb-2">Thermochromic Buttons</h4>
                                        <p class="text-sm text-gray-600 mb-3">Temperature-sensitive color-changing buttons for children's wear and outdoor apparel collections</p>
                                        <div class="flex flex-wrap gap-2">
                                            <span class="bg-purple-100 text-purple-600 text-xs px-2 py-1 rounded">1 Invention Patent</span>
                                            <span class="bg-purple-100 text-purple-600 text-xs px-2 py-1 rounded">5 Color Options</span>
                                            <span class="bg-purple-100 text-purple-600 text-xs px-2 py-1 rounded">Launched 2024</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        <div class="feature-card rounded-2xl p-6">
                            <div class="flex items-start gap-4">
                                <div class="w-14 h-14 bg-green-100 rounded-xl flex items-center justify-center flex-shrink-0">
                                    <i class="fas fa-flask text-green-500 text-2xl"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold text-primary mb-2">Material Testing Institute</h4>
                                    <p class="text-sm text-gray-600 mb-3">Third-party collaboration with SGS for certification and testing</p>
                                    <div class="flex flex-wrap gap-2">
                                        <span class="bg-green-100 text-green-600 text-xs px-2 py-1 rounded">Annual Audits</span>
                                        <span class="bg-green-100 text-green-600 text-xs px-2 py-1 rounded">Certified Lab</span>
                                        <span class="bg-green-100 text-green-600 text-xs px-2 py-1 rounded">REACH Compliance</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="feature-card rounded-2xl p-6">
                                <div class="flex items-start gap-4">
                                    <div class="w-14 h-14 bg-orange-100 rounded-xl flex items-center justify-center flex-shrink-0">
                                        <i class="fas fa-recycle text-orange-500 text-2xl"></i>
                                    </div>
                                    <div>
                                        <h4 class="font-bold text-primary mb-2">Biodegradable Resin Series</h4>
                                        <p class="text-sm text-gray-600 mb-3">Plant-based biodegradable button collection certified for industrial and home composting</p>
                                        <div class="flex flex-wrap gap-2">
                                            <span class="bg-orange-100 text-orange-600 text-xs px-2 py-1 rounded">2 Material Patents</span>
                                            <span class="bg-orange-100 text-orange-600 text-xs px-2 py-1 rounded">15 Styles</span>
                                            <span class="bg-orange-100 text-orange-600 text-xs px-2 py-1 rounded">GRS Certified</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                    </div>
                </div>'''
    
    new_cases_section = '''<!-- Cost-Saving Cases -->
                <div class="reveal">
                    <h3 class="text-2xl font-bold text-primary mb-8 text-center">
                        <i class="fas fa-hand-holding-usd text-accent mr-3"></i>Customer Cost-Saving Cases
                    </h3>
                    <div class="grid md:grid-cols-3 gap-6">
                        <div class="feature-card rounded-2xl p-6">
                            <div class="flex items-start gap-4">
                                <div class="w-14 h-14 bg-green-100 rounded-xl flex items-center justify-center flex-shrink-0">
                                    <i class="fas fa-coins text-green-500 text-2xl"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold text-primary mb-2">Material Substitution</h4>
                                    <p class="text-sm text-gray-600 mb-3">Helped a UK SOHO switch from expensive zamak to cost-effective alloy buttons - saved 35% on material costs</p>
                                    <div class="flex flex-wrap gap-2">
                                        <span class="bg-green-100 text-green-600 text-xs px-2 py-1 rounded">35% Cost Saved</span>
                                        <span class="bg-green-100 text-green-600 text-xs px-2 py-1 rounded">UK Customer</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="feature-card rounded-2xl p-6">
                            <div class="flex items-start gap-4">
                                <div class="w-14 h-14 bg-blue-100 rounded-xl flex items-center justify-center flex-shrink-0">
                                    <i class="fas fa-cogs text-blue-500 text-2xl"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold text-primary mb-2">Process Optimization</h4>
                                    <p class="text-sm text-gray-600 mb-3">Simplified plating process for a German fashion buyer - reduced lead time by 7 days and cut costs by 20%</p>
                                    <div class="flex flex-wrap gap-2">
                                        <span class="bg-blue-100 text-blue-600 text-xs px-2 py-1 rounded">7 Days Faster</span>
                                        <span class="bg-blue-100 text-blue-600 text-xs px-2 py-1 rounded">German Buyer</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="feature-card rounded-2xl p-6">
                            <div class="flex items-start gap-4">
                                <div class="w-14 h-14 bg-orange-100 rounded-xl flex items-center justify-center flex-shrink-0">
                                    <i class="fas fa-boxes text-orange-500 text-2xl"></i>
                                </div>
                                <div>
                                    <h4 class="font-bold text-primary mb-2">Small Batch Solution</h4>
                                    <p class="text-sm text-gray-600 mb-3">Created a mixed-style production plan for a US boutique - allowed MOQ 100 instead of 500, saved inventory costs</p>
                                    <div class="flex flex-wrap gap-2">
                                        <span class="bg-orange-100 text-orange-600 text-xs px-2 py-1 rounded">MOQ 100</span>
                                        <span class="bg-orange-100 text-orange-600 text-xs px-2 py-1 rounded">US Boutique</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>'''
    
    content = re.sub(re.escape(old_cases_section), new_cases_section, content)
    
    # 8. Update R&D Capability card to be more pragmatic
    old_rd_capability = '''<div class="feature-card rounded-2xl p-8 reveal">
                    <div class="w-16 h-16 bg-purple-100 rounded-2xl flex items-center justify-center mb-6">
                        <i class="fas fa-microscope text-purple-500 text-2xl"></i>
                    </div>
                    <h3 class="text-xl font-bold text-primary mb-4">R&D Capability</h3>
                    <p class="text-gray-600 mb-4">
                        Dedicated R&D team developing new designs, materials, and manufacturing processes.
                    </p>
                    <ul class="text-sm text-gray-500 space-y-2">
                        <li><i class="fas fa-check text-purple-500 mr-2"></i>Custom mold development</li>
                        <li><i class="fas fa-check text-purple-500 mr-2"></i>New material research</li>
                        <li><i class="fas fa-check text-purple-500 mr-2"></i>Annual new product launches</li>
                    </ul>
                </div>'''
    
    new_rd_capability = '''<div class="feature-card rounded-2xl p-8 reveal">
                    <div class="w-16 h-16 bg-purple-100 rounded-2xl flex items-center justify-center mb-6">
                        <i class="fas fa-users text-purple-500 text-2xl"></i>
                    </div>
                    <h3 class="text-xl font-bold text-primary mb-4">Small & Specialized</h3>
                    <p class="text-gray-600 mb-4">
                        Focused, founder-led team with deep practical experience. We don't overpromise - we deliver practical solutions.
                    </p>
                    <ul class="text-sm text-gray-500 space-y-2">
                        <li><i class="fas fa-check text-purple-500 mr-2"></i>Fast custom response</li>
                        <li><i class="fas fa-check text-purple-500 mr-2"></i>Flexible small batches</li>
                        <li><i class="fas fa-check text-purple-500 mr-2"></i>Direct founder communication</li>
                    </ul>
                </div>'''
    
    content = re.sub(re.escape(old_rd_capability), new_rd_capability, content)
    
    # Update section title from Technology & Innovation to Practical & Focused
    content = re.sub(
        r'<h2 class="text-3xl md:text-4xl lg:text-5xl font-bold text-primary mb-6">\s*Technology & Innovation\s*</h2>',
        '<h2 class="text-3xl md:text-4xl lg:text-5xl font-bold text-primary mb-6">Practical & Focused</h2>',
        content
    )
    
    # Update section subtitle
    content = re.sub(
        r'<p class="text-gray-600 text-lg max-w-2xl mx-auto">\s*Continuous investment in research and development to bring you the latest in button technology.\s*</p>',
        '<p class="text-gray-600 text-lg max-w-2xl mx-auto">Small, experienced team delivering practical button solutions. No hype - just reliable quality and flexible service.</p>',
        content
    )
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ R&D section updated successfully!")

if __name__ == '__main__':
    update_rd_section()
