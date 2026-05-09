// Global Modal Functions (Outside DOMContentLoaded for maximum availability)
window.openEnquiryModal = (projectName) => {
    const modal = document.getElementById('enquiry-modal');
    const modalProjectName = document.getElementById('modal-project-name');
    const modalProjectInput = document.getElementById('modal-project-input');

    if (modalProjectName) modalProjectName.textContent = `Enquire for ${projectName}`;
    if (modalProjectInput) modalProjectInput.value = projectName;
    if (modal) {
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    }
};

window.closeEnquiryModal = () => {
    const modal = document.getElementById('enquiry-modal');
    if (modal) modal.classList.remove('active');
    document.body.style.overflow = '';
};

document.addEventListener('DOMContentLoaded', () => {
    // --- 1. Page Load Overlay & Hero Animation ---
    const loader = document.getElementById('page-loader');
    const triggerHeroAnimation = () => {
        const words = document.querySelectorAll('.hero-editorial .word');
        words.forEach((word, index) => {
            setTimeout(() => word.classList.add('active'), index * 150);
        });

        const loadAnims = document.querySelectorAll('.animate-on-load');
        loadAnims.forEach((el, index) => {
            setTimeout(() => el.classList.add('reveal-active'), 600 + (index * 200));
        });
    };

    setTimeout(() => {
        if (loader) {
            loader.style.opacity = '0';
            setTimeout(() => {
                loader.style.display = 'none';
                document.body.classList.remove('loading');
                triggerHeroAnimation();
            }, 1000);
        }
    }, 800);

    // --- 3. Lenis Smooth Scroll ---
    let lenis;
    try {
        if (typeof Lenis !== 'undefined') {
            lenis = new Lenis({
                duration: 1.2,
                easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
                direction: 'vertical',
                smooth: true,
            });

            function raf(time) {
                lenis.raf(time);
                requestAnimationFrame(raf);
            }
            requestAnimationFrame(raf);
        }
    } catch (e) {
        console.warn('Lenis failed:', e);
    }

    // --- 4. Navbar Scroll State ---
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        if (navbar && window.scrollY > 80) {
            navbar.classList.add('nav-scrolled');
        } else if (navbar) {
            navbar.classList.remove('nav-scrolled');
        }
    });

    // --- 5. Parallax Logic ---
    const parallaxItems = document.querySelectorAll('.parallax');
    if (lenis) {
        lenis.on('scroll', () => {
            parallaxItems.forEach(item => {
                const speed = item.getAttribute('data-speed') || 0.1;
                const yPos = -(window.scrollY * speed);
                item.style.transform = `translateY(${yPos}px)`;
            });
        });
    }

    // --- 6. Mobile Menu ---
    const menuToggle = document.getElementById('menu-toggle');
    const drawer = document.getElementById('mobile-drawer');
    const drawerCloseBtn = document.getElementById('drawer-close');
    const mobileLinks = document.querySelectorAll('.mobile-nav-links a');

    if (menuToggle && drawer) {
        const closeDrawer = () => {
            drawer.classList.remove('active');
            menuToggle.classList.remove('active');
        };

        menuToggle.addEventListener('click', () => {
            drawer.classList.toggle('active');
            menuToggle.classList.toggle('active');
        });

        if (drawerCloseBtn) {
            drawerCloseBtn.addEventListener('click', closeDrawer);
        }

        mobileLinks.forEach(link => {
            link.addEventListener('click', closeDrawer);
        });
    }

    // --- 7. CountUp ---
    const countUp = (element) => {
        const target = parseInt(element.getAttribute('data-target'));
        const suffix = element.getAttribute('data-suffix') || '';
        let current = 0;
        const increment = target / 100;
        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                element.textContent = target + suffix;
                clearInterval(timer);
            } else {
                element.textContent = Math.round(current) + suffix;
            }
        }, 20);
    };

    // --- 8. Intersection Observer ---
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const el = entry.target;
                el.classList.add('reveal-active');
                if (el.classList.contains('stats-strip')) {
                    el.querySelectorAll('.stat-num').forEach(num => countUp(num));
                }
            }
        });
    }, { threshold: 0.15 });

    document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .stats-strip').forEach(el => {
        observer.observe(el);
    });

    // --- 9. Filtering ---
    const filterBtns = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');
    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            const filter = btn.getAttribute('data-filter');
            projectCards.forEach(card => {
                if (filter === 'all' || card.classList.contains(filter)) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });

    // --- 10. FAQ Accordion ---
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        if (question) {
            question.addEventListener('click', () => {
                const isActive = item.classList.contains('active');
                faqItems.forEach(i => i.classList.remove('active'));
                if (!isActive) {
                    item.classList.add('active');
                }
            });
        }
    });

    // Modal Close logic for clicks outside content
    const modal = document.getElementById('enquiry-modal');
    if (modal) {
        modal.addEventListener('click', (e) => {
            if (e.target === modal) window.closeEnquiryModal();
        });
    }
});
