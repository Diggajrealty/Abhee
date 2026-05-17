const fs = require('fs');
const path = require('path');

// Configuration for Author
const author = {
    name: "Vikram Sharma",
    desc: "Senior Market Analyst with 12 years of experience tracking Bangalore's real estate shifts.",
    img: "https://picsum.photos/seed/author1/150"
};

// Standard Lead Form HTML
const leadForm = (slug) => `
<div style="background: var(--bg-secondary); border: 1px solid var(--border-gold); border-radius: 12px; padding: 40px; margin: 40px 0;">
    <h3 style="font-family: var(--font-display); color: var(--text-dark); font-size: 1.5rem; margin-bottom: 8px;">Get Expert Advice & Pricing</h3>
    <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 25px;">Our property advisors will call you within 2 hours.</p>
    <form name="blog-enquiry-${slug}" method="POST" data-netlify="true" action="/success" style="display: grid; gap: 15px;">
        <input type="text" name="name" placeholder="Your Name*" required style="padding: 14px; border: 1px solid var(--border-gold); border-radius: 4px; background: var(--bg-primary); color: var(--text-dark); font-size: 0.95rem; width: 100%; box-sizing: border-box;">
        <input type="tel" name="phone" placeholder="Mobile Number*" required style="padding: 14px; border: 1px solid var(--border-gold); border-radius: 4px; background: var(--bg-primary); color: var(--text-dark); font-size: 0.95rem; width: 100%; box-sizing: border-box;">
        <select name="project" style="padding: 14px; border: 1px solid var(--border-gold); border-radius: 4px; background: var(--bg-primary); color: var(--text-dark); font-size: 0.95rem; width: 100%; box-sizing: border-box;">
            <option value="">I am interested in... (Optional)</option>
            <option>Abhee Codename New Dimension</option>
            <option>Abhee Aaria</option>
            <option>Abhee Celestial City</option>
            <option>General Enquiry</option>
        </select>
        <button type="submit" style="background: #c9a84c; color: #1a1a1a; padding: 16px; border: none; font-weight: 700; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px; cursor: pointer; border-radius: 4px;">Request a Callback &rarr;</button>
    </form>
</div>`;

// Mid-article CTA HTML
const midCta = `
<div style="background: linear-gradient(135deg, #1a1a1a 0%, #2a1f00 100%); border: 1px solid rgba(201,168,76,0.4); border-radius: 12px; padding: 40px; margin: 50px 0; text-align: center;">
    <span style="display:inline-block; background: rgba(201,168,76,0.15); color: #c9a84c; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 2px; padding: 6px 16px; border-radius: 20px; margin-bottom: 15px;">Pre-Launch Opportunity</span>
    <h3 style="color: #fff; font-family: var(--font-display); font-size: 1.8rem; margin-bottom: 12px;">Abhee Codename New Dimension</h3>
    <p style="color: rgba(255,255,255,0.7); font-size: 1rem; margin-bottom: 25px; line-height: 1.6;">45-acre Scotland-themed luxury township on Varthur Sarjapur Road. 140+ amenities. Starting ₹1.14 Cr*</p>
    <div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap;">
        <a href="../../abhee-codename-new-dimension.html" style="background: #c9a84c; color: #1a1a1a; padding: 14px 30px; text-decoration: none; font-weight: 700; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; border-radius: 4px;">View Project &rarr;</a>
        <a href="https://wa.me/919886890004?text=Hi, I'm interested in Abhee Codename New Dimension." style="background: #25D366; color: #fff; padding: 14px 30px; text-decoration: none; font-weight: 700; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; border-radius: 4px;">&#128172; WhatsApp Us</a>
    </div>
</div>`;

function generateTOC(content) {
    const headers = [];
    const h2Regex = /<h2 id="([^"]+)">([^<]+)<\/h2>/g;
    let match;
    while ((match = h2Regex.exec(content)) !== null) {
        headers.push({ id: match[1], text: match[2] });
    }
    if (headers.length === 0) return '';
    let tocHtml = `<div class="toc"><h4>Table of Contents</h4><ul>`;
    headers.forEach(h => { tocHtml += `<li><a href="#${h.id}">${h.text}</a></li>`; });
    tocHtml += `</ul></div>`;
    return tocHtml;
}

const blogs = [
    {
        slug: 'varthur-sarjapur-road-investment-guide-2025',
        title: "Why Varthur–Sarjapur Road Is Bangalore's #1 Investment Corridor in 2025–2026",
        summary: "When it comes to real estate investment in Bangalore, the golden rule has always been to follow the infrastructure. As we look towards 2025 and 2026, no micro-market presents a more compelling case than the Varthur–Sarjapur Road corridor in East Bangalore.",
        image: 'blog-2.jpg',
        category: 'INVESTMENT GUIDE',
        date: 'May 11, 2026',
        content: `
            <h2 id="infrastructure">1. The Infrastructure Boom: PRR and Metro Phase 3</h2>
            <p>The upcoming Peripheral Ring Road (PRR) is set to revolutionize connectivity in East Bangalore. By seamlessly connecting Tumkur Road, Bellary Road, Old Madras Road, and Hosur Road, the PRR will drastically cut down commute times.</p>
            <h2 id="gcc-expansions">2. GCC Expansions and The IT Triangle</h2>
            <p>Varthur and Sarjapur sit at the apex of Bangalore's most lucrative IT triangle: Whitefield, Outer Ring Road (ORR), and Electronic City. With Global Capability Centers (GCCs) aggressively expanding their footprint, demand for luxury housing is hitting an all-time high.</p>
            <h2 id="new-dimension">3. The Ultimate Investment: Abhee Codename New Dimension</h2>
            <p>Abhee Codename New Dimension, a 45-acre luxury township located exactly on this high-growth corridor, represents the pinnacle of investment opportunity in 2025.</p>
        `
    },
    {
        slug: 'abhee-codename-new-dimension-buyers-guide',
        title: "Abhee Codename New Dimension: Complete Buyer's Guide (Price, RERA, Possession)",
        summary: "Are you considering investing in East Bangalore's most anticipated luxury project? Here is your complete, unbiased buyer's guide to Abhee Codename New Dimension, analyzing everything from pricing and RERA compliance to honest pros and cons.",
        image: 'blog-1.jpg',
        category: 'PROJECT REVIEW',
        date: 'May 11, 2026',
        content: `
            <h2 id="overview">1. Project Overview and RERA Status</h2>
            <p>Developed by the trusted Abhee, Codename New Dimension is a 45-acre mega township designed around an authentic Scottish theme. The project is strictly RERA compliant (PRM/KA/RERA/1251/308/PR/260226/008489).</p>
            <h2 id="pricing">2. Floor Plans and Pricing</h2>
            <p>The project caters to diverse needs with meticulously designed floor plans: 2 BHK starting from ₹1.14 Cr*, 3 BHK starting from ₹1.30 Cr*, and Luxury 4.5 BHK options up to ₹2.31 Cr*.</p>
            <h2 id="pros-cons">3. Honest Pros & Cons</h2>
            <p><strong>Pros:</strong> Unmatched scale with 85% open space, 3-acre golf range, and 4 massive clubhouses. <strong>Cons:</strong> Early residents might experience ongoing construction in later phases due to the project's scale.</p>
        `
    },
    {
        slug: 'scotland-themed-townships-bangalore-luxury-market',
        title: "Scotland-Themed Townships: Why This Niche Is Winning Bangalore's Luxury Market",
        summary: "Bangalore’s luxury real estate market is maturing. Buyers are no longer satisfied with standard amenities; they seek experiential living. Enter the era of ultra-thematic mega townships, led by the highly anticipated Scotland-themed development in East Bangalore.",
        image: 'blog-3.jpg',
        category: 'LIFESTYLE TRENDS',
        date: 'May 11, 2026',
        content: `
            <h2 id="experience">1. The Shift from Utilities to Experiences</h2>
            <p>Modern homebuyers want their residences to serve as an escape from the urban hustle. The Scottish theme specifically taps into a desire for vast, rolling green landscapes and serene water bodies.</p>
            <h2 id="benchmark">2. Abhee New Dimension: Setting the Benchmark</h2>
            <p>This 45-acre luxury township doesn't just use "Scotland" as a marketing gimmick; it integrates the theme into its core architecture with a man-made lake (The Loch) and a 3-acre golf range.</p>
            <h2 id="demand">3. Why Thematic Living Wins</h2>
            <p>As 2025 approaches, thematic mega-townships that deliver an immersive lifestyle are seeing the highest demand and fastest appreciation rates in the city.</p>
        `
    }
];

// Load base index for template
const html = fs.readFileSync('index.html', 'utf8');
const footerIndex = html.indexOf('<footer');
const footer = html.substring(footerIndex);

// Define a simplified header for blogs
const header = `
    <nav class="navbar nav-scrolled">
        <div class="container nav-container">
            <a href="../../index.html" class="logo-group clickable">
                <div class="logo-brand">ABHEE</div>
            </a>
            <ul class="nav-links">
                <li><a href="../../index.html#about">About</a></li>
                <li><a href="../../index.html#projects">Projects</a></li>
                <li><a href="../../index.html#blogs">Blogs</a></li>
                <li><a href="../../index.html#contact">Contact</a></li>
            </ul>
        </div>
    </nav>
`;

for(let b of blogs) {
    const dir = path.join('blogs', b.slug);
    if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
    const toc = generateTOC(b.content);
    const pageHtml = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${b.title} | Abhee</title>
    <link rel="stylesheet" href="../../assets/css/style.css">
    <style>
        .blog-header { background: url('../../assets/images/${b.image}') no-repeat center center/cover; padding: 150px 0 100px; position: relative; text-align: center; color: #fff; }
        .blog-header::before { content: ''; position: absolute; inset: 0; background: rgba(0,0,0,0.6); }
        .blog-content-wrapper { max-width: 800px; margin: 0 auto; padding: 60px 5%; background: var(--bg-primary); }
        .blog-summary { background: rgba(201, 168, 76, 0.05); border-left: 4px solid var(--gold-accent); padding: 25px; margin: 40px 0; border-radius: 0 8px 8px 0; }
        .toc { background: var(--bg-secondary); padding: 30px; border-radius: 8px; margin: 40px 0; border: 1px solid var(--border-gold); }
        .toc h4 { color: var(--gold-accent); margin-bottom: 15px; }
        .toc ul { list-style: none; padding: 0; }
        .toc li { margin-bottom: 10px; }
        .toc a { color: var(--text-dark); text-decoration: none; font-size: 0.95rem; }
        .blog-content h2 { margin: 40px 0 20px; color: var(--text-dark); font-family: var(--font-display); font-size: 2rem; }
        .blog-content p { color: var(--text-muted); line-height: 1.8; margin-bottom: 25px; font-size: 1.05rem; }
        .author-box { display: flex; align-items: center; gap: 20px; padding: 30px; background: var(--bg-secondary); border-radius: 8px; margin-top: 60px; }
        .author-box img { width: 80px; height: 80px; border-radius: 50%; object-fit: cover; }
    </style>
</head>
<body>
    ${header}
    <header class="blog-header">
        <div class="container" style="position: relative; z-index: 2;">
            <span style="color: var(--gold-accent); font-weight: bold; letter-spacing: 2px;">${b.category}</span>
            <h1 style="font-family: var(--font-display); font-size: 3.5rem; margin: 20px 0;">${b.title}</h1>
            <p>Published on ${b.date} | By The Abhee Editorial Team</p>
        </div>
    </header>
    <div class="blog-content-wrapper">
        <div class="blog-summary">
            <h4 style="color: var(--gold-accent); margin-bottom: 10px; font-family: var(--font-display); font-size: 1.2rem;">Executive Summary</h4>
            <p style="font-size: 0.95rem; margin-bottom: 0; line-height: 1.6; color: var(--text-dark);">${b.summary}</p>
        </div>
        ${toc}
        <div class="blog-content">${b.content}</div>
        ${midCta}
        ${leadForm(b.slug)}
        <div class="author-box">
            <img src="${author.img}" alt="${author.name}">
            <div><h4 style="margin-bottom: 5px; color: var(--text-dark);">${author.name}</h4><p style="font-size: 0.9rem; margin-bottom: 0;">${author.desc}</p></div>
        </div>
    </div>
    ${footer.replace(/assets\//g, '../../assets/')}
    <script src="../../assets/js/main.js"></script>
</body>
</html>`;
    fs.writeFileSync(path.join(dir, 'index.html'), pageHtml);
    console.log(`Successfully built: ${b.slug}`);
}
