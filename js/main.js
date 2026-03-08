// ===================================
// 근쌤의 체육 웹앱 포트폴리오
// Toss-style Landing Page JS
// ===================================

document.addEventListener('DOMContentLoaded', () => {
    initScrollAnimations();
    initActiveNav();
    initSmoothScroll();
    initMobileMenu();
    initCountUp();
    initTagFilter();
});

// ===================================
// IntersectionObserver Scroll Animations
// ===================================
function initScrollAnimations() {
    const elements = document.querySelectorAll('[data-animate]');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.15,
        rootMargin: '0px 0px -60px 0px'
    });

    elements.forEach(el => observer.observe(el));
}

// ===================================
// Active Navigation Link
// ===================================
function initActiveNav() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-links a');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${id}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }, {
        threshold: 0.3,
        rootMargin: '-64px 0px -40% 0px'
    });

    sections.forEach(section => observer.observe(section));
}

// ===================================
// Smooth Scroll
// ===================================
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = link.getAttribute('href');
            if (targetId === '#') return;

            const target = document.querySelector(targetId);
            if (target) {
                const navHeight = 64;
                const targetPos = target.offsetTop - navHeight;
                window.scrollTo({ top: targetPos, behavior: 'smooth' });

                // Close mobile menu if open
                const mobileMenu = document.getElementById('mobileMenu');
                if (mobileMenu && mobileMenu.classList.contains('open')) {
                    mobileMenu.classList.remove('open');
                    document.body.style.overflow = '';
                }
            }
        });
    });
}

// ===================================
// Mobile Menu
// ===================================
function initMobileMenu() {
    const btn = document.getElementById('mobileMenuBtn');
    const menu = document.getElementById('mobileMenu');
    if (!btn || !menu) return;

    btn.addEventListener('click', () => {
        const isOpen = menu.classList.toggle('open');
        document.body.style.overflow = isOpen ? 'hidden' : '';
        // Toggle hamburger icon
        const bars = btn.querySelectorAll('rect');
        if (isOpen) {
            bars[0].setAttribute('transform', 'rotate(45 12 6)');
            bars[0].setAttribute('width', '20');
            bars[1].style.opacity = '0';
            bars[2].setAttribute('transform', 'rotate(-45 12 18)');
            bars[2].setAttribute('width', '20');
        } else {
            bars[0].removeAttribute('transform');
            bars[0].setAttribute('width', '18');
            bars[1].style.opacity = '1';
            bars[2].removeAttribute('transform');
            bars[2].setAttribute('width', '14');
        }
    });
}

// ===================================
// Count Up Animation
// ===================================
function initCountUp() {
    const statNumbers = document.querySelectorAll('[data-count]');
    if (!statNumbers.length) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCount(entry.target);
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    statNumbers.forEach(el => observer.observe(el));
}

function animateCount(el) {
    const target = parseInt(el.getAttribute('data-count'), 10);
    const suffix = el.getAttribute('data-suffix') || '';
    const duration = 1500;
    const startTime = performance.now();

    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);

        // Ease out expo curve
        const easeOut = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
        const current = Math.round(easeOut * target);

        el.textContent = current + suffix;

        if (progress < 1) {
            requestAnimationFrame(update);
        }
    }

    requestAnimationFrame(update);
}

// ===================================
// Tag Filter
// ===================================
function initTagFilter() {
    const buttons = document.querySelectorAll('.tag-filter');
    const cards = document.querySelectorAll('.app-card[data-tag]');
    if (!buttons.length || !cards.length) return;

    buttons.forEach(btn => {
        btn.addEventListener('click', () => {
            const filter = btn.getAttribute('data-filter');

            // Update active button
            buttons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            // Filter cards
            cards.forEach(card => {
                const tag = card.getAttribute('data-tag');
                if (filter === 'all' || tag === filter) {
                    card.classList.remove('hidden');
                } else {
                    card.classList.add('hidden');
                }
            });
        });
    });
}

// ===================================
// Keyboard Navigation
// ===================================
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        const mobileMenu = document.getElementById('mobileMenu');
        if (mobileMenu && mobileMenu.classList.contains('open')) {
            mobileMenu.classList.remove('open');
            document.body.style.overflow = '';
        }
    }
});
