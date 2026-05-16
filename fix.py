import re

file_path = 'abhee-new-dimension.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Canonical
content = re.sub(
    r'<link rel="canonical" href="[^"]+">',
    '<link rel="canonical" href="https://abheeprelaunch.com/abhee-new-dimension">',
    content
)

# 2. Update og:url
content = re.sub(
    r'<meta property="og:url" content="[^"]+">',
    '<meta property="og:url" content="https://abheeprelaunch.com/abhee-new-dimension">',
    content
)

# 3. Update title
content = re.sub(
    r'<title>.*?</title>',
    '<title>Abhee Codename New Dimension – 45-Acre Scotland Township | Varthur Sarjapur Road Bangalore 2026</title>',
    content,
    flags=re.DOTALL
)

# 4. Update description
content = re.sub(
    r'<meta name="description"\s*content="[^"]+">',
    '<meta name="description"\n        content="Abhee Codename New Dimension — Bangalore\'s first 45-acre Scotland-themed luxury township on Varthur Sarjapur Road. 3,000+ homes, 14 towers, 140+ amenities. 2 to 4.5 BHK from ₹1.14 Cr*. RERA approved. EOI open 2026.">',
    content
)

# 5. Update keywords
content = re.sub(
    r'<meta name="keywords"\s*content="[^"]+">',
    '<meta name="keywords"\n        content="Abhee New Dimension, Abhee Codename New Dimension, Abhee New Dimension price 2026, 45 acre township Varthur Road, Scotland themed apartments Bangalore, luxury apartments Varthur Sarjapur Road, pre-launch apartments East Bangalore 2026, 2 BHK Varthur Road Bangalore, 3 BHK Gunjur Bangalore, 4.5 BHK luxury apartments Bangalore, new launch apartments Whitefield 2026, gated township Bangalore, Abhee builders Bangalore, Abhee Pvt Ltd projects, apartments near Greenwood High School Bangalore, mega township East Bangalore">',
    content
)

# 6. Update og:title
content = re.sub(
    r'<meta property="og:title" content="[^"]+">',
    '<meta property="og:title" content="Abhee Codename New Dimension | 45-Acre Scotland Township, Varthur–Sarjapur Road Bangalore 2026">',
    content
)

# 7. Update og:description
content = re.sub(
    r'<meta property="og:description"\s*content="[^"]+">',
    '<meta property="og:description"\n        content="Bangalore\'s first Scotland-themed 45-acre luxury township. 14 towers, 3,000+ homes, 140+ amenities. 2–4.5 BHK from ₹1.14 Cr*. RERA approved. EOI open now — 2026.">',
    content
)

# 8. Update twitter:title
content = re.sub(
    r'<meta name="twitter:title" content="[^"]+">',
    '<meta name="twitter:title" content="Abhee Codename New Dimension | 45-Acre Scotland Township Bangalore 2026">',
    content
)

# 9. Update 2025 to 2026
content = content.replace('2025', '2026')

# 10. Add FAQPage schema
faq_schema = '''
    <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is Abhee Codename New Dimension?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Abhee Codename New Dimension is Bangalore's first Scotland-themed luxury township spanning 45 acres on Varthur Sarjapur Road. It features 14 high-rise towers, 3,000+ homes, 140+ amenities including a 3-acre golf range, 4 clubhouses totalling 1.5 lakh sq.ft., and a man-made lake. Configurations range from 2 BHK to 4.5 BHK."
      }
    },
    {
      "@type": "Question",
      "name": "What is the starting price of Abhee New Dimension?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Abhee Codename New Dimension starts from ₹1.14 Cr* for 2 BHK apartments. 2.5 BHK starts from ₹1.30 Cr*, 3 BHK from ₹1.59 Cr*, 3.5 BHK from ₹1.88 Cr*, and 4.5 BHK from ₹2.31 Cr*. All prices are indicative and GST is extra."
      }
    },
    {
      "@type": "Question",
      "name": "Where is Abhee New Dimension located?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Abhee Codename New Dimension is located on Varthur Sarjapur Road, East Bangalore. It is near Greenwood High International School, approximately 15 minutes from ITPL Whitefield and 20 minutes from the Outer Ring Road tech corridor."
      }
    },
    {
      "@type": "Question",
      "name": "What is the RERA number for Abhee New Dimension?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The RERA registration number for Abhee Codename New Dimension is PRM/KA/RERA/1251/308/PR/260226/008489. It is fully approved under Karnataka RERA."
      }
    },
    {
      "@type": "Question",
      "name": "What amenities does Abhee New Dimension offer?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Abhee New Dimension offers 140+ amenities including a 3-acre golf range, 4 grand clubhouses spanning 1.5 lakh sq.ft., a man-made loch, infinity pools, a 2-acre central forest, cricket pitch, tennis courts, amphitheatre, sky lounge, retail high street, pet park, cycling track, and 24/7 smart security."
      }
    }
  ]
}
</script>
'''

if 'What is Abhee Codename New Dimension?' not in content:
    content = content.replace('</head>', faq_schema + '</head>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Success')
