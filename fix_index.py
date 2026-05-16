import re

file_path = 'index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update title
content = re.sub(
    r'<title>.*?</title>',
    '<title>Abhee Projects – Authorised Channel Partner | Luxury Apartments Bangalore</title>',
    content,
    flags=re.DOTALL
)

# 2. Update description
content = re.sub(
    r'<meta name="description"\s*content="[^"]+">',
    '<meta name="description" content="Abhee Projects — authorised channel partner for Abhee Pvt. Ltd. Explore Abhee New Dimension, Abhee Aaria, Abhee Celestial City, Abhee Silicon Shine and more luxury apartments across Bangalore. RERA approved. Zero brokerage.">',
    content
)

# 3. Update keywords
content = re.sub(
    r'<meta name="keywords"\s*content="[^"]+">',
    '<meta name="keywords" content="Abhee projects Bangalore, Abhee New Dimension 45 acres, Abhee Aaria Gunjur, Abhee Celestial City Sarjapur Road, Abhee Silicon Shine, Abhee builders Bangalore, luxury apartments Bangalore 2026, RERA approved apartments Bangalore, new launch apartments East Bangalore, pre-launch apartments Varthur Road, Abhee Pvt Ltd channel partner, authorised channel partner Abhee, 2 BHK 3 BHK apartments Bangalore, gated community Sarjapur Road, Scotland themed township Bangalore">',
    content
)

# 4. Update og:title
content = re.sub(
    r'<meta property="og:title" content="[^"]+">',
    '<meta property="og:title" content="Abhee Projects – Authorised Channel Partner | Bangalore">',
    content
)

# 5. Update hero subtitle text
content = re.sub(
    r'<p class="hero-sub animate-on-load">\s*Bangalore\'s premier real estate developer since 2009. 16\+ RERA-approved luxury projects delivered\s*across prime corridors.\s*</p>',
    '<p class="hero-sub animate-on-load">\n                    Authorised channel partner for Abhee Pvt. Ltd. — explore ongoing luxury projects across Bangalore including New Dimension, Aaria, Celestial City, Silicon Shine and more. Zero brokerage. Direct developer pricing.\n                </p>',
    content
)

# 6. Update project cards links
# Abhee New Dimension
content = content.replace('href="abhee-new-dimension.html"', 'href="/abhee-new-dimension"')

# Abhee Aaria
content = re.sub(
    r'<button class="btn btn-outline clickable" onclick="openEnquiryModal\(\'Abhee Aaria\'\)"([^>]*)>Learn\s*More</button>',
    r'<a href="/abhee-aaria" class="btn btn-outline clickable"\1>Learn\n                            More</a>',
    content
)

# Abhee Celestial City
content = re.sub(
    r'<button class="btn btn-outline clickable" onclick="openEnquiryModal\(\'Abhee Celestial City\'\)"([^>]*)>Learn\s*More</button>',
    r'<a href="/abhee-celestial-city" class="btn btn-outline clickable"\1>Learn\n                            More</a>',
    content
)

# Abhee Silicon Shine
content = re.sub(
    r'<button class="btn btn-outline clickable"\s*onclick="openEnquiryModal\(\'Abhee Silicon Shine(?:\s*\(Bommasandra\))?\'\)"([^>]*)>Learn\s*More</button>',
    r'<a href="/abhee-silicon-shine" class="btn btn-outline clickable"\1>Learn\n                            More</a>',
    content
)

# 7. Update homepage nav 'Blogs' link to point to /blog/
content = content.replace('href="#blogs"', 'href="/blog/"')

# 8. Fix 2025 -> 2026
content = content.replace('2025', '2026')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Success')
