// ===================================
// 근쌤의 체육 웹앱 포트폴리오
// Main JavaScript
// ===================================

document.addEventListener('DOMContentLoaded', () => {
    initScrollEffects();
    initSmoothScroll();
    initIntersectionObserver();
});

// Header Scroll Effect
function initScrollEffects() {
    const header = document.getElementById('header');
    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;

        if (currentScroll > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }

        lastScroll = currentScroll;
    });
}

// Smooth Scroll for Navigation
function initSmoothScroll() {
    const navLinks = document.querySelectorAll('a[href^="#"]');

    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = link.getAttribute('href');

            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                const headerHeight = document.getElementById('header').offsetHeight;
                const targetPosition = targetElement.offsetTop - headerHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Intersection Observer for Fade In Animations
function initIntersectionObserver() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe all app cards
    const appCards = document.querySelectorAll('.app-card');
    appCards.forEach(card => {
        card.style.opacity = '0';
        observer.observe(card);
    });
}

// Optional: Preload images for better performance
function preloadImages() {
    const images = document.querySelectorAll('img[data-src]');

    images.forEach(img => {
        const src = img.getAttribute('data-src');
        if (src) {
            const image = new Image();
            image.src = src;
            image.onload = () => {
                img.src = src;
                img.removeAttribute('data-src');
            };
        }
    });
}

// Optional: Add keyboard navigation
document.addEventListener('keydown', (e) => {
    // Escape key to go back to top
    if (e.key === 'Escape') {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }
});
