#!/usr/bin/env python3
"""Modify Contact section and Footer for better visual balance and compactness"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ========== CONTACT SECTION MODIFICATION ==========
# Old Contact section start
old_contact_start = '''    <!-- Contact Section -->
    <section id="contact" class="py-16 lg:py-24 bg-gray-900 text-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid lg:grid-cols-2 gap-16">
                <div class="reveal">
                    <span class="inline-block px-4 py-2 bg-accent/20 text-accent rounded-full text-sm font-medium mb-4">
                        CONTACT US
                    </span>
                    <h2 class="text-3xl md:text-4xl lg:text-5xl font-bold mb-6">
                        Let's Start Your Project
                    </h2>
                    <p class="text-gray-400 text-lg mb-8">
                        Ready to discuss your button and garment accessory needs? 
                        Get in touch for a free consultation and quotation. We respond within 24 hours.
                    </p>
                    
                    <div class="space-y-6">'''

# New Contact section start - with Get in Touch title and styled container
new_contact_start = '''    <!-- Contact Section -->
    <section id="contact" class="py-12 lg:py-16 bg-gray-900 text-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid lg:grid-cols-2 gap-6 lg:gap-8">
                <div class="reveal bg-white/5 border border-white/10 rounded-2xl p-6 lg:p-8">
                    <h3 class="text-xl font-bold mb-6 text-white">
                        Get in Touch
                    </h3>
                    
                    <div class="space-y-4">'''

# Replace contact start
content = content.replace(old_contact_start, new_contact_start)

# Update contact info items spacing (space-y-6 -> space-y-4)
# Already handled above

# ========== UPDATE QUICK BENEFITS SECTION ==========
# Make it more compact
old_quick_benefits = '''                    <!-- Quick Benefits -->
                    <div class="mt-8 p-6 bg-white/5 rounded-xl">
                        <h4 class="font-semibold mb-4 text-white">
                            <i class="fas fa-bolt text-accent mr-2"></i>Why Contact Us?
                        </h4>
                        <div class="grid grid-cols-2 gap-4 text-sm">
                            <div class="flex items-center gap-2 text-gray-600">
                                <i class="fas fa-check text-eco"></i>
                                <span>Free samples available</span>
                            </div>
                            <div class="flex items-center gap-2 text-gray-600">
                                <i class="fas fa-check text-eco"></i>
                                <span>7-day sample lead time</span>
                            </div>
                            <div class="flex items-center gap-2 text-gray-600">
                                <i class="fas fa-check text-eco"></i>
                                <span>Small MOQ supported</span>
                            </div>
                            <div class="flex items-center gap-2 text-gray-600">
                                <i class="fas fa-check text-eco"></i>
                                <span>Custom design service</span>
                            </div>
                        </div>
                    </div>
                    
                    <div class="flex gap-4 mt-8">'''

new_quick_benefits = '''                    <!-- Quick Benefits -->
                    <div class="mt-6 p-4 bg-white/5 rounded-xl">
                        <h4 class="font-semibold mb-3 text-white text-sm">
                            <i class="fas fa-bolt text-accent mr-2"></i>Why Contact Us?
                        </h4>
                        <div class="grid grid-cols-2 gap-2 text-xs">
                            <div class="flex items-center gap-1.5 text-gray-600">
                                <i class="fas fa-check text-eco text-xs"></i>
                                <span>Free samples</span>
                            </div>
                            <div class="flex items-center gap-1.5 text-gray-600">
                                <i class="fas fa-check text-eco text-xs"></i>
                                <span>7-day samples</span>
                            </div>
                            <div class="flex items-center gap-1.5 text-gray-600">
                                <i class="fas fa-check text-eco text-xs"></i>
                                <span>Small MOQ</span>
                            </div>
                            <div class="flex items-center gap-1.5 text-gray-600">
                                <i class="fas fa-check text-eco text-xs"></i>
                                <span>Custom design</span>
                            </div>
                        </div>
                    </div>
                    
                    <div class="flex gap-3 mt-6">'''

content = content.replace(old_quick_benefits, new_quick_benefits)

# Update social icons size in contact section
old_social_icons = '''                        <a href="#" class="w-12 h-12 bg-white/10 rounded-lg flex items-center justify-center hover:bg-accent transition-colors">
                            <i class="fab fa-facebook-f text-xl"></i>
                        </a>
                        <a href="#" class="w-12 h-12 bg-white/10 rounded-lg flex items-center justify-center hover:bg-accent transition-colors">
                            <i class="fab fa-linkedin-in text-xl"></i>
                        </a>
                        <a href="#" class="w-12 h-12 bg-white/10 rounded-lg flex items-center justify-center hover:bg-accent transition-colors">
                            <i class="fab fa-instagram text-xl"></i>
                        </a>
                        <a href="#" class="w-12 h-12 bg-white/10 rounded-lg flex items-center justify-center hover:bg-accent transition-colors">
                            <i class="fab fa-whatsapp text-xl"></i>
                        </a>
                    </div>
                </div>
                
                <div class="bg-white rounded-2xl p-6 lg:p-8 text-gray-800 reveal">'''

new_social_icons = '''                        <a href="#" class="w-10 h-10 bg-white/10 rounded-lg flex items-center justify-center hover:bg-accent transition-colors">
                            <i class="fab fa-facebook-f"></i>
                        </a>
                        <a href="#" class="w-10 h-10 bg-white/10 rounded-lg flex items-center justify-center hover:bg-accent transition-colors">
                            <i class="fab fa-linkedin-in"></i>
                        </a>
                        <a href="#" class="w-10 h-10 bg-white/10 rounded-lg flex items-center justify-center hover:bg-accent transition-colors">
                            <i class="fab fa-instagram"></i>
                        </a>
                        <a href="#" class="w-10 h-10 bg-white/10 rounded-lg flex items-center justify-center hover:bg-accent transition-colors">
                            <i class="fab fa-whatsapp"></i>
                        </a>
                    </div>
                </div>
                
                <div class="bg-white rounded-2xl p-6 lg:p-8 text-gray-800 reveal">'''

content = content.replace(old_social_icons, new_social_icons)

# Update Send Us a Message title to match left side (already good, just make sure padding is consistent)
# Reduce form spacing
old_form = '''                    <h3 class="text-xl font-bold text-primary mb-6">Send Us a Message</h3>
                    <form id="contact-form" class="space-y-5">'''

new_form = '''                    <h3 class="text-xl font-bold text-primary mb-6">Send Us a Message</h3>
                    <form id="contact-form" class="space-y-4">'''

content = content.replace(old_form, new_form)

# Reduce form input padding
old_input_padding = '''class="form-input w-full px-4 py-2.5 rounded-lg focus:outline-none"'''
new_input_padding = '''class="form-input w-full px-4 py-2 rounded-lg focus:outline-none"'''
content = content.replace(old_input_padding, new_input_padding)

# Reduce submit button padding
old_submit = '''class="w-full btn-primary py-3.5 rounded-lg font-semibold flex items-center justify-center gap-2"'''
new_submit = '''class="w-full btn-primary py-3 rounded-lg font-semibold flex items-center justify-center gap-2"'''
content = content.replace(old_submit, new_submit)

# Reduce bottom margin of contact form message
old_form_message = '''                    <p class="text-center text-gray-500 text-sm mt-4">
                        <i class="fas fa-lock mr-1"></i>
                        Your information is secure and will never be shared.
                    </p>'''

new_form_message = '''                    <p class="text-center text-gray-500 text-xs mt-3">
                        <i class="fas fa-lock mr-1"></i>
                        Your information is secure and will never be shared.
                    </p>'''

content = content.replace(old_form_message, new_form_message)

# ========== FOOTER SECTION MODIFICATION ==========
# Make footer more compact - reduce all spacing by 1/3
old_footer = '''    <!-- Footer -->
    <footer class="bg-gray-50 py-10 border-t border-gray-200">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center">
                <!-- Logo -->
                <div class="mb-6">
                    <img src="images/logo-transparent.png" alt="Yenjor Logo" class="h-10 w-auto object-contain mx-auto">
                </div>
                
                <!-- Short Description -->
                <p class="text-gray-600 mb-6 max-w-xl mx-auto text-sm leading-relaxed">
                    Leading manufacturer of quality buttons and garment accessories since 2003. 
                    GRS-accredited supplier for garment factories and fashion brands worldwide.
                </p>
                
                <!-- Certification Badges -->
                <div class="flex justify-center gap-3 flex-wrap mb-6">
                    <span class="bg-white border border-gray-200 px-3 py-1.5 rounded-full text-xs text-gray-600 flex items-center shadow-sm">
                        <img src="images/cert-oeko-tex-small.png" alt="OEKO-TEX" class="w-4 h-4 mr-1.5">OEKO-TEX
                    </span>
                    <span class="bg-white border border-gray-200 px-3 py-1.5 rounded-full text-xs text-gray-600 flex items-center shadow-sm">
                        <img src="images/cert-grs-small.png" alt="GRS" class="w-4 h-4 mr-1.5">GRS
                    </span>
                    <span class="bg-white border border-gray-200 px-3 py-1.5 rounded-full text-xs text-gray-600 flex items-center shadow-sm">
                        <img src="images/cert-iso-small.png" alt="ISO 9001" class="w-4 h-4 mr-1.5">ISO 9001
                    </span>
                </div>
                
                <!-- Social Icons -->
                <div class="flex justify-center gap-3 mb-8">
                    <a href="#" class="w-9 h-9 bg-white border border-gray-200 rounded-full flex items-center justify-center hover:bg-accent hover:border-accent hover:text-white transition-all duration-300 shadow-sm">
                        <i class="fab fa-facebook-f text-gray-600 text-sm"></i>
                    </a>
                    <a href="#" class="w-9 h-9 bg-white border border-gray-200 rounded-full flex items-center justify-center hover:bg-accent hover:border-accent hover:text-white transition-all duration-300 shadow-sm">
                        <i class="fab fa-linkedin-in text-gray-600 text-sm"></i>
                    </a>
                    <a href="#" class="w-9 h-9 bg-white border border-gray-200 rounded-full flex items-center justify-center hover:bg-accent hover:border-accent hover:text-white transition-all duration-300 shadow-sm">
                        <i class="fab fa-instagram text-gray-600 text-sm"></i>
                    </a>
                    <a href="#" class="w-9 h-9 bg-white border border-gray-200 rounded-full flex items-center justify-center hover:bg-accent hover:border-accent hover:text-white transition-all duration-300 shadow-sm">
                        <i class="fab fa-whatsapp text-gray-600 text-sm"></i>
                    </a>
                </div>
                
                <!-- Divider -->
                <div class="border-t border-gray-200 pt-6">
                    <!-- Copyright -->
                    <p class="text-gray-500 text-xs">
                        © 2024 Yenjor Co., Ltd. All rights reserved.
                    </p>
                </div>
            </div>
        </div>
    </footer>'''

new_footer = '''    <!-- Footer -->
    <footer class="bg-gray-50 py-7 border-t border-gray-200">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center">
                <!-- Logo -->
                <div class="mb-4">
                    <img src="images/logo-transparent.png" alt="Yenjor Logo" class="h-8 w-auto object-contain mx-auto">
                </div>
                
                <!-- Short Description -->
                <p class="text-gray-600 mb-4 max-w-xl mx-auto text-xs leading-relaxed">
                    Leading manufacturer of quality buttons and garment accessories since 2003. 
                    GRS-accredited supplier for garment factories and fashion brands worldwide.
                </p>
                
                <!-- Certification Badges -->
                <div class="flex justify-center gap-2 flex-wrap mb-4">
                    <span class="bg-white border border-gray-200 px-2 py-1 rounded-full text-xs text-gray-600 flex items-center shadow-sm">
                        <img src="images/cert-oeko-tex-small.png" alt="OEKO-TEX" class="w-3.5 h-3.5 mr-1">OEKO-TEX
                    </span>
                    <span class="bg-white border border-gray-200 px-2 py-1 rounded-full text-xs text-gray-600 flex items-center shadow-sm">
                        <img src="images/cert-grs-small.png" alt="GRS" class="w-3.5 h-3.5 mr-1">GRS
                    </span>
                    <span class="bg-white border border-gray-200 px-2 py-1 rounded-full text-xs text-gray-600 flex items-center shadow-sm">
                        <img src="images/cert-iso-small.png" alt="ISO 9001" class="w-3.5 h-3.5 mr-1">ISO 9001
                    </span>
                </div>
                
                <!-- Social Icons -->
                <div class="flex justify-center gap-2 mb-5">
                    <a href="#" class="w-7 h-7 bg-white border border-gray-200 rounded-full flex items-center justify-center hover:bg-accent hover:border-accent hover:text-white transition-all duration-300 shadow-sm">
                        <i class="fab fa-facebook-f text-gray-600 text-xs"></i>
                    </a>
                    <a href="#" class="w-7 h-7 bg-white border border-gray-200 rounded-full flex items-center justify-center hover:bg-accent hover:border-accent hover:text-white transition-all duration-300 shadow-sm">
                        <i class="fab fa-linkedin-in text-gray-600 text-xs"></i>
                    </a>
                    <a href="#" class="w-7 h-7 bg-white border border-gray-200 rounded-full flex items-center justify-center hover:bg-accent hover:border-accent hover:text-white transition-all duration-300 shadow-sm">
                        <i class="fab fa-instagram text-gray-600 text-xs"></i>
                    </a>
                    <a href="#" class="w-7 h-7 bg-white border border-gray-200 rounded-full flex items-center justify-center hover:bg-accent hover:border-accent hover:text-white transition-all duration-300 shadow-sm">
                        <i class="fab fa-whatsapp text-gray-600 text-xs"></i>
                    </a>
                </div>
                
                <!-- Divider -->
                <div class="border-t border-gray-200 pt-4">
                    <!-- Copyright -->
                    <p class="text-gray-500 text-xs">
                        © 2024 Yenjor Co., Ltd. All rights reserved.
                    </p>
                </div>
            </div>
        </div>
    </footer>'''

content = content.replace(old_footer, new_footer)

# Write the modified content
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Contact and Footer sections modified successfully!")
print("- Contact: Removed large title/description, added Get in Touch title")
print("- Contact: Added semi-transparent background to left column")
print("- Contact: Reduced spacing between columns by ~60%")
print("- Contact: Added padding to contact info, updated icon backgrounds")
print("- Contact: Form padding aligned with left column")
print("- Footer: All spacing reduced by 1/3, overall more compact")
