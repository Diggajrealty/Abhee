import re
from bs4 import BeautifulSoup
import json

def build_project(filename, data):
    with open('template_clean.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    # Meta / SEO
    soup.title.string = data['title']
    if soup.find('meta', {'name': 'description'}):
        soup.find('meta', {'name': 'description'})['content'] = data['description']
    if soup.find('meta', {'name': 'keywords'}):
        soup.find('meta', {'name': 'keywords'})['content'] = data['keywords']
    if soup.find('link', {'rel': 'canonical'}):
        soup.find('link', {'rel': 'canonical'})['href'] = data['canonical']
    if soup.find('meta', {'property': 'og:title'}):
        soup.find('meta', {'property': 'og:title'})['content'] = data['og_title']
    if soup.find('meta', {'property': 'og:description'}):
        soup.find('meta', {'property': 'og:description'})['content'] = data['og_description']
    if soup.find('meta', {'name': 'twitter:title'}):
        soup.find('meta', {'name': 'twitter:title'})['content'] = data['title']
    
    # Hero Section
    # Location pill
    hero_badges = soup.find('div', class_='hero-badges')
    if hero_badges:
        pill = hero_badges.find('span', class_='badge filled')
        if pill:
            pill.string = data['location_pill']
        # Status pills
        badges = hero_badges.find_all('span', class_='badge')
        # Clear existing badges
        hero_badges.clear()
        for pill_text in data['status_pills']:
            cls = 'badge filled' if pill_text == data['status_pills'][0] else 'badge'
            span = soup.new_tag('span', attrs={'class': cls})
            span.string = pill_text
            hero_badges.append(span)

    hero_title = soup.find('h1', class_='hero-title h-large')
    if hero_title:
        # data['h1'] might have '*' for italic/accent. E.g. "Abhee Aaria: *Luxury Living in Gunjur.*"
        parts = data['h1'].split('*')
        hero_title.clear()
        if len(parts) > 1:
            hero_title.append(parts[0])
            span = soup.new_tag('span', attrs={'class': 'gold', 'style': 'display:block;'})
            span.string = parts[1]
            hero_title.append(span)
        else:
            hero_title.string = data['h1']
            
    hero_sub = soup.find('p', class_='hero-sub text-lead stagger-2 reveal')
    if hero_sub:
        hero_sub.string = data['subtext']
        
    # Stats Bar
    stat_grid = soup.find('div', class_='stat-grid')
    if stat_grid:
        stat_grid.clear()
        for stat in data['stats']:
            # stat is "Value / Label"
            val, lbl = stat.split(' / ')
            item = soup.new_tag('div', attrs={'class': 'stat-item'})
            span_val = soup.new_tag('span', attrs={'class': 'stat-num'})
            span_val.string = val
            span_lbl = soup.new_tag('span', attrs={'class': 'stat-text'})
            span_lbl.string = lbl
            item.append(span_val)
            item.append(span_lbl)
            stat_grid.append(item)

    # Configurations
    config_cards = soup.find('div', class_='config-cards')
    if config_cards:
        config_cards.clear()
        for conf in data['configs']:
            # conf = {'name': '1 BHK', 'price': 'from ₹75.7 Lakhs*', 'desc': 'Enquire...'}
            card = soup.new_tag('div', attrs={'class': 'card reveal stagger-1'})
            h3 = soup.new_tag('h3', attrs={'class': 'card-title'})
            h3.string = conf['name']
            span_desc = soup.new_tag('span', attrs={'class': 'card-size'})
            span_desc.string = conf['desc']
            div_price = soup.new_tag('div', attrs={'class': 'card-price'})
            small = soup.new_tag('small')
            small.string = 'Starting Price'
            span_price = soup.new_tag('span')
            span_price.string = conf['price']
            div_price.append(small)
            div_price.append(span_price)
            btn = soup.new_tag('button', attrs={'class': 'btn btn-outline clickable', 'onclick': f"openEnquiryModal('{data['project_name']} - {conf['name']}')", 'style': 'width:100%'})
            btn.string = 'Enquire Now'
            
            card.append(h3)
            card.append(span_desc)
            card.append(div_price)
            card.append(btn)
            config_cards.append(card)

    # Amenities Grid
    amenity_grid = soup.find('div', class_='amenity-grid')
    if amenity_grid:
        amenity_grid.clear()
        icons = ['🏊‍♂️','🏋️‍♀️','🌳','🏃‍♂️','🎾','🎉','⚡','🛡️','🚗','🏀','🛍️']
        for i, am in enumerate(data['amenities']):
            item = soup.new_tag('div', attrs={'class': 'am-item reveal stagger-1'})
            icon = soup.new_tag('span', attrs={'class': 'am-icon'})
            icon.string = icons[i % len(icons)]
            text = soup.new_tag('span', attrs={'class': 'am-text'})
            text.string = am
            item.append(icon)
            item.append(text)
            amenity_grid.append(item)

    # Location
    loc_addr = soup.find(lambda tag: tag.name in ['h3', 'h4'] and 'Address' in tag.get_text())
    if loc_addr:
        p = loc_addr.find_next('p')
        if p:
            p.string = data['address']
    
    loc_grid = soup.find('ul', class_='loc-list')
    if loc_grid:
        loc_grid.clear()
        # Parse nearby string: "Sarjapur Road (2 km), Varthur Road (1.5 km), ..."
        places = [p.strip() for p in data['nearby'].split(',')]
        for place in places:
            li = soup.new_tag('li')
            li.string = place
            loc_grid.append(li)

    # Contact Form Dropdown
    forms = soup.find_all('form')
    for form in forms:
        select = form.find('select')
        if select:
            select.clear()
            opt = soup.new_tag('option', attrs={'value': '', 'disabled': '', 'selected': ''})
            opt.string = 'Configuration of Interest *'
            select.append(opt)
            for conf in data['configs']:
                opt = soup.new_tag('option', attrs={'value': conf['name']})
                opt.string = conf['name']
                select.append(opt)
    
    # FAQ Schema
    ldjson_tags = soup.find_all('script', type='application/ld+json')
    faq_added = False
    for tag in ldjson_tags:
        if 'FAQPage' in tag.string:
            tag.string = data['faq_schema']
            faq_added = True
            break
    if not faq_added:
        script = soup.new_tag('script', type='application/ld+json')
        script.string = data['faq_schema']
        if soup.head:
            soup.head.append(script)
        
    # Find 2025 and replace with 2026
    html_str = str(soup)
    html_str = html_str.replace('2025', '2026')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_str)


data_aaria = {
    'project_name': 'Abhee Aaria',
    'title': 'Abhee Aaria – Luxury 1, 2, 3 & 4 BHK Apartments | Gunjur, Bangalore',
    'description': 'Abhee Aaria — premium 1, 2, 3 & 4 BHK luxury apartments in Gunjur, off Sarjapur Road, Bangalore. Starting from ₹75.7 Lakhs*. RERA approved. Zero brokerage. Enquire for price and floor plans.',
    'keywords': 'Abhee Aaria, Abhee Aaria Gunjur, luxury apartments Gunjur, 1 BHK Gunjur Bangalore, 2 BHK Sarjapur Road, Abhee Aaria price, Gunjur apartments 2026, off Sarjapur Road apartments, new launch Gunjur 2026, Abhee builders Gunjur',
    'canonical': 'https://abheeprelaunch.com/abhee-aaria',
    'og_title': 'Abhee Aaria – Luxury 1 to 4 BHK Apartments, Gunjur Bangalore',
    'og_description': 'Premium gated community in Gunjur, off Sarjapur Road. 1 to 4 BHK apartments from ₹75.7 Lakhs*. RERA approved. EOI open.',
    'location_pill': 'Gunjur · Off Sarjapur Road · Bengaluru',
    'h1': 'Abhee Aaria: *Luxury Living in Gunjur.*',
    'subtext': 'Abhee Aaria — a premium gated community in Gunjur, off Sarjapur Road. Offering 1, 2, 3, and 4 BHK apartments with world-class amenities, seamless connectivity to Bangalore\'s IT hubs, and Abhee\'s signature construction quality. Starting from ₹75.7 Lakhs*.',
    'status_pills': ['Ongoing', 'Gunjur', 'RERA Approved'],
    'stats': ['Gunjur / Prime Location', '1–4 BHK / Configurations', 'Premium / Amenities', 'RERA / Approved'],
    'configs': [
        {'name': '1 BHK', 'price': 'from ₹75.7 Lakhs*', 'desc': 'Enquire for size & floor plans'},
        {'name': '2 BHK', 'price': 'On Request', 'desc': 'Enquire for size & floor plans'},
        {'name': '3 BHK', 'price': 'On Request', 'desc': 'Enquire for size & floor plans'},
        {'name': '4 BHK', 'price': 'On Request', 'desc': 'Enquire for size & floor plans'}
    ],
    'amenities': ['Clubhouse', 'Swimming Pool', 'Gymnasium', 'Kids\' Play Area', 'Landscaped Gardens', 'Jogging Track', 'Basketball Court', 'Tennis Court', 'Multipurpose Hall', 'EV Charging', '24/7 Security', 'Visitor Parking'],
    'address': 'Gunjur, Off Sarjapur Road, Bengaluru',
    'nearby': 'Sarjapur Road (2 km), Varthur Road (1.5 km), Whitefield ITPL (15 min), Wipro Campus (10 min), Vibgyor School (5 min), Forum Whitefield (12 min)',
    'faq_schema': '''{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Where is Abhee Aaria located?",
      "acceptedAnswer": {"@type": "Answer", "text": "Abhee Aaria is located in Gunjur, off Sarjapur Road in Bangalore."}
    },
    {
      "@type": "Question",
      "name": "What is the starting price for Abhee Aaria?",
      "acceptedAnswer": {"@type": "Answer", "text": "The starting price for 1 BHK apartments in Abhee Aaria is ₹75.7 Lakhs*."}
    },
    {
      "@type": "Question",
      "name": "What configurations are available at Abhee Aaria?",
      "acceptedAnswer": {"@type": "Answer", "text": "Abhee Aaria offers 1, 2, 3, and 4 BHK luxury apartments."}
    },
    {
      "@type": "Question",
      "name": "Is Abhee Aaria RERA approved?",
      "acceptedAnswer": {"@type": "Answer", "text": "Yes, Abhee Aaria is a fully RERA approved project."}
    },
    {
      "@type": "Question",
      "name": "Who is the builder of Abhee Aaria?",
      "acceptedAnswer": {"@type": "Answer", "text": "Abhee Aaria is developed by Abhee Pvt. Ltd., a trusted Bangalore developer since 2009."}
    }
  ]
}'''
}

build_project('abhee-aaria.html', data_aaria)

data_celestial = {
    'project_name': 'Abhee Celestial City',
    'title': 'Abhee Celestial City – Luxury 2 & 3 BHK Apartments | Sarjapur Road, Bangalore',
    'description': 'Abhee Celestial City — premium 2 & 3 BHK luxury apartments on Sarjapur Road, Bangalore. Starting from ₹1.30 Cr*. RERA approved. Zero brokerage. Enquire for price and floor plans.',
    'keywords': 'Abhee Celestial City, Abhee Celestial City Sarjapur Road, luxury apartments Sarjapur Road, 2 BHK Sarjapur Road 2026, 3 BHK Sarjapur Road Bangalore, Abhee Celestial City price, gated community Sarjapur Road, new launch Sarjapur Road 2026, Abhee builders Sarjapur Road',
    'canonical': 'https://abheeprelaunch.com/abhee-celestial-city',
    'og_title': 'Abhee Celestial City – Luxury 2 & 3 BHK, Sarjapur Road Bangalore',
    'og_description': 'Premium luxury apartments on Sarjapur Road. 2 & 3 BHK from ₹1.30 Cr*. RERA approved. EOI open.',
    'location_pill': 'Sarjapur Road · Bengaluru',
    'h1': 'Abhee Celestial City: *Luxury on Sarjapur Road.*',
    'subtext': 'Abhee Celestial City — premium 2 and 3 BHK apartments on Sarjapur Road, Bangalore\'s most active luxury residential corridor. Designed for modern families and investors with world-class amenities and Abhee\'s guaranteed on-time delivery. Starting from ₹1.30 Cr*.',
    'status_pills': ['Ongoing', 'Sarjapur Road', 'RERA Approved'],
    'stats': ['Sarjapur Road / Prime Location', '2 & 3 BHK / Configurations', 'Premium / Amenities', 'RERA / Approved'],
    'configs': [
        {'name': '2 BHK', 'price': 'from ₹1.30 Cr*', 'desc': 'Enquire for floor plans'},
        {'name': '3 BHK', 'price': 'On Request', 'desc': 'Enquire for floor plans'}
    ],
    'amenities': ['Clubhouse', 'Swimming Pool', 'Gymnasium', 'Kids\' Play Area', 'Landscaped Gardens', 'Jogging Track', 'Basketball Court', 'Tennis Court', 'Multipurpose Hall', 'EV Charging', '24/7 Security', 'Visitor Parking'],
    'address': 'Sarjapur Road, Bengaluru',
    'nearby': 'Outer Ring Road (10 min), Electronic City (20 min), HSR Layout (15 min), Wipro Campus (12 min), Decathlon Sarjapur Road (5 min), Forum Neighbourhood Mall (8 min)',
    'faq_schema': '''{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Where is Abhee Celestial City located?",
      "acceptedAnswer": {"@type": "Answer", "text": "Abhee Celestial City is located on Sarjapur Road, Bangalore."}
    },
    {
      "@type": "Question",
      "name": "What is the price of a 2 BHK in Abhee Celestial City?",
      "acceptedAnswer": {"@type": "Answer", "text": "The price for a 2 BHK starts from ₹1.30 Cr*."}
    },
    {
      "@type": "Question",
      "name": "What configurations are offered?",
      "acceptedAnswer": {"@type": "Answer", "text": "We offer premium 2 and 3 BHK apartments."}
    },
    {
      "@type": "Question",
      "name": "Is Abhee a reliable builder?",
      "acceptedAnswer": {"@type": "Answer", "text": "Yes, Abhee has been a trusted developer since 2009 with over 16 completed projects."}
    },
    {
      "@type": "Question",
      "name": "When is the possession timeline?",
      "acceptedAnswer": {"@type": "Answer", "text": "Please contact us for exact tower-wise possession timelines."}
    }
  ]
}'''
}

build_project('abhee-celestial-city.html', data_celestial)

data_silicon = {
    'project_name': 'Abhee Silicon Shine',
    'title': 'Abhee Silicon Shine – Luxury 1 to 4 BHK Apartments | Bommasandra, Bangalore',
    'description': 'Abhee Silicon Shine — premium 1, 2, 3 & 4 BHK apartments at Bommasandra, Bangalore. Starting from ₹70 Lakhs*. RERA approved. Close to Electronic City and Bommasandra Industrial Area. Zero brokerage.',
    'keywords': 'Abhee Silicon Shine, Abhee Silicon Shine Bommasandra, 1 BHK Bommasandra Bangalore, 2 BHK Electronic City corridor, luxury apartments Bommasandra, Abhee Silicon Shine price 2026, new launch Bommasandra 2026, apartments near Electronic City Bangalore',
    'canonical': 'https://abheeprelaunch.com/abhee-silicon-shine',
    'og_title': 'Abhee Silicon Shine – 1 to 4 BHK Apartments, Bommasandra Bangalore',
    'og_description': 'Premium gated community near Electronic City. 1 to 4 BHK from ₹70 Lakhs*. RERA approved.',
    'location_pill': 'Bommasandra · Near Electronic City · Bengaluru',
    'h1': 'Abhee Silicon Shine: *Smart Living Near Electronic City.*',
    'subtext': 'Abhee Silicon Shine — premium 1, 2, 3 and 4 BHK gated community apartments at Bommasandra, Bangalore\'s fastest growing affordable-luxury corridor adjacent to Electronic City. Starting from ₹70 Lakhs*. Ideal for IT professionals and first-time buyers.',
    'status_pills': ['Ongoing', 'Bommasandra', 'RERA Approved'],
    'stats': ['Bommasandra / Prime Location', '1–4 BHK / Configurations', 'Electronic City / 5 Min Drive', 'RERA / Approved'],
    'configs': [
        {'name': '1 BHK', 'price': 'from ₹70 Lakhs*', 'desc': 'Enquire for size & floor plans'},
        {'name': '2 BHK', 'price': 'On Request', 'desc': 'Enquire for size & floor plans'},
        {'name': '3 BHK', 'price': 'On Request', 'desc': 'Enquire for size & floor plans'},
        {'name': '4 BHK', 'price': 'On Request', 'desc': 'Enquire for size & floor plans'}
    ],
    'amenities': ['Clubhouse', 'Swimming Pool', 'Gymnasium', 'Kids\' Play Area', 'Landscaped Gardens', 'Jogging Track', 'Basketball Court', 'Tennis Court', 'Multipurpose Hall', 'EV Charging', '24/7 Security', 'Visitor Parking'],
    'address': 'Bommasandra, Bengaluru',
    'nearby': 'Electronic City Phase 1 (5 min), Electronic City Phase 2 (8 min), Hosur Road (2 min), Infosys Campus (10 min), Narayana Hospital (5 min), Bommasandra Metro Station (7 min)',
    'faq_schema': '''{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Where is Abhee Silicon Shine located?",
      "acceptedAnswer": {"@type": "Answer", "text": "It is located in Bommasandra, close to Electronic City."}
    },
    {
      "@type": "Question",
      "name": "What is the starting price?",
      "acceptedAnswer": {"@type": "Answer", "text": "Prices start from ₹70 Lakhs* for a 1 BHK."}
    },
    {
      "@type": "Question",
      "name": "How far is Electronic City?",
      "acceptedAnswer": {"@type": "Answer", "text": "Electronic City is just a 5-minute drive away."}
    },
    {
      "@type": "Question",
      "name": "Are there amenities?",
      "acceptedAnswer": {"@type": "Answer", "text": "Yes, it features a clubhouse, pool, gym, and more."}
    },
    {
      "@type": "Question",
      "name": "Is it a reliable investment?",
      "acceptedAnswer": {"@type": "Answer", "text": "Yes, Abhee has a stellar track record and the location is seeing rapid appreciation."}
    }
  ]
}'''
}

build_project('abhee-silicon-shine.html', data_silicon)
