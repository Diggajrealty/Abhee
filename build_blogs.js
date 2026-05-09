const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

// The hero section starts with `<section class="hero-section"`
const heroIndex = html.indexOf('<section class="hero-section"');
let header = html.substring(0, heroIndex);

// The footer starts with `<footer`
const footerIndex = html.indexOf('<footer');
let footer = html.substring(footerIndex);

// Let's modify the header slightly to remove the page loader for the blogs, or keep it.
// We'll just keep it. 

// The blog content is in abhee-new-dimension.html
const projectHtml = fs.readFileSync('abhee-new-dimension.html', 'utf8');

// Extract the 3 blog contents
function getBlogContent(id) {
    const startTag = `<div id="${id}">`;
    let startIndex = projectHtml.indexOf(startTag);
    if(startIndex === -1) {
        // it might be <div id="blog1-content">
        startIndex = projectHtml.indexOf(`<div id="${id}-content">`);
    }
    if(startIndex === -1) return '';
    
    // We need to find the matching closing div. It's easier to just use regex or split.
    // In our case, the blog content ends before `<div id="blog2-content">` or `</div>` of the parent.
    // Let's just extract the inner HTML roughly.
    const subStr = projectHtml.substring(startIndex);
    const endStr = id === 'blog3-content' ? '</div>\n    </div>' : '<div id="blog';
    const endIndex = subStr.indexOf(endStr, 1);
    
    let content = subStr.substring(0, endIndex > -1 ? endIndex : subStr.length);
    if(id === 'blog3-content') content = content.substring(0, content.lastIndexOf('</div>'));
    return content;
}

const blogs = [
    {
        id: 'blog1-content',
        filename: 'blog-1.html',
        title: "The Rise of Luxury Apartments in Bangalore"
    },
    {
        id: 'blog2-content',
        filename: 'blog-2.html',
        title: "Why Invest in Abhee Sarjapur Projects?"
    },
    {
        id: 'blog3-content',
        filename: 'blog-3.html',
        title: "Whitefield: The Silicon Valley of India"
    }
];

for(let b of blogs) {
    let content = getBlogContent(b.id);
    
    // Wrap it in a nice container
    let pageHtml = header + `
    <!-- BLOG ARTICLE -->
    <section class="blog-article" style="padding: 150px 0 80px; background: var(--bg-secondary);">
        <div class="container" style="max-width: 800px; background: var(--bg-primary); padding: 50px; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid var(--border-gold);">
            <div style="margin-bottom: 30px;">
                <a href="index.html#blogs" style="color: var(--gold); text-decoration: none; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; font-size: 0.85rem;">&larr; Back to Insights</a>
            </div>
            ${content}
        </div>
    </section>
    ` + footer;
    
    // Replace the title to match the blog
    pageHtml = pageHtml.replace('<title>Abhee | Trusted Real Estate Developer in Bangalore Since 2009</title>', `<title>${b.title} | Abhee</title>`);
    
    fs.writeFileSync(b.filename, pageHtml);
    console.log('Created ' + b.filename);
}
