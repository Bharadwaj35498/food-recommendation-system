// ============================================================
// ENHANCED FOOD RECOMMENDATION WEBSITE - JAVASCRIPT
// Interactive animations, particle effects, and cool features
// ============================================================

// ============================================================
// PARTICLE EFFECT SYSTEM
// ============================================================

class ParticleEffect {
    constructor(x, y, count = 10, color = '#FF6B6B') {
        this.particles = [];
        this.x = x;
        this.y = y;
        this.color = color;
        
        for (let i = 0; i < count; i++) {
            this.particles.push({
                x: x,
                y: y,
                vx: (Math.random() - 0.5) * 8,
                vy: (Math.random() - 0.5) * 8 - 3,
                life: 1,
                decay: Math.random() * 0.02 + 0.015,
                size: Math.random() * 5 + 2
            });
        }
    }
    
    update() {
        this.particles = this.particles.filter(p => {
            p.x += p.vx;
            p.y += p.vy;
            p.vy += 0.2; // gravity
            p.life -= p.decay;
            return p.life > 0;
        });
        return this.particles.length > 0;
    }
    
    render(canvas, ctx) {
        this.particles.forEach(p => {
            ctx.save();
            ctx.globalAlpha = p.life;
            ctx.fillStyle = this.color;
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
            ctx.fill();
            ctx.restore();
        });
    }
}

// Particle system
let particles = [];
let animationFrameId = null;

function createParticleCanvas() {
    const canvas = document.createElement('canvas');
    canvas.id = 'particle-canvas';
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    canvas.style.position = 'fixed';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.pointerEvents = 'none';
    canvas.style.zIndex = '999';
    document.body.appendChild(canvas);
    
    const ctx = canvas.getContext('2d');
    
    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        particles = particles.filter(p => p.update());
        particles.forEach(p => p.render(canvas, ctx));
        
        if (particles.length > 0) {
            animationFrameId = requestAnimationFrame(animate);
        }
    }
    
    return canvas;
}

const particleCanvas = createParticleCanvas();

function createParticles(x, y, count = 15, color = '#FF6B6B') {
    particles.push(new ParticleEffect(x, y, count, color));
    if (!animationFrameId) {
        animationFrameId = requestAnimationFrame(() => {
            const ctx = particleCanvas.getContext('2d');
            ctx.clearRect(0, 0, particleCanvas.width, particleCanvas.height);
            
            particles = particles.filter(p => p.update());
            particles.forEach(p => p.render(particleCanvas, ctx));
            
            if (particles.length > 0) {
                animationFrameId = requestAnimationFrame(arguments.callee);
            } else {
                animationFrameId = null;
            }
        });
    }
}

// ============================================================
// CONFETTI ANIMATION
// ============================================================

function createConfetti() {
    const confetti = [];
    const canvas = particleCanvas;
    const ctx = canvas.getContext('2d');
    
    for (let i = 0; i < 50; i++) {
        confetti.push({
            x: Math.random() * canvas.width,
            y: -10,
            vx: (Math.random() - 0.5) * 10,
            vy: Math.random() * 5 + 5,
            rotation: Math.random() * Math.PI * 2,
            rotationSpeed: (Math.random() - 0.5) * 0.3,
            life: 1,
            color: ['#FF6B6B', '#4ECDC4', '#FFE66D', '#51CF66'][Math.floor(Math.random() * 4)]
        });
    }
    
    let frame = 0;
    const drawConfetti = () => {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        confetti.forEach((c, idx) => {
            c.x += c.vx;
            c.y += c.vy;
            c.vy += 0.2;
            c.rotation += c.rotationSpeed;
            c.life -= 0.01;
            
            ctx.save();
            ctx.globalAlpha = c.life;
            ctx.translate(c.x, c.y);
            ctx.rotate(c.rotation);
            ctx.fillStyle = c.color;
            ctx.fillRect(-5, -5, 10, 10);
            ctx.restore();
        });
        
        confetti = confetti.filter(c => c.life > 0);
        
        if (confetti.length > 0) {
            requestAnimationFrame(drawConfetti);
        }
    };
    
    drawConfetti();
}

// ============================================================
// TOAST NOTIFICATIONS
// ============================================================

function showToast(message, duration = 3000, type = 'success') {
    const toast = document.getElementById('toast');
    toast.textContent = message;
    toast.className = `toast show ${type}`;
    
    setTimeout(() => {
        toast.classList.remove('show');
    }, duration);
}

// ============================================================
// SCROLL UTILITIES
// ============================================================

function scrollToElement(id) {
    const element = document.getElementById(id);
    if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
    }
}

function scrollToRecommender() {
    scrollToElement('recommender');
}

// ============================================================
// INTERACTIVE FORM ELEMENTS
// ============================================================

// Hunger slider with visual feedback
const hungerSlider = document.getElementById('hunger');
if (hungerSlider) {
    hungerSlider.addEventListener('input', (e) => {
        const value = parseInt(e.target.value);
        const percent = (value / 2) * 100;
        e.target.style.background = `linear-gradient(to right, var(--primary) 0%, var(--primary) ${percent}%, #ddd ${percent}%, #ddd 100%)`;
    });
    
    // Initial setup
    const initialValue = parseInt(hungerSlider.value);
    const initialPercent = (initialValue / 2) * 100;
    hungerSlider.style.background = `linear-gradient(to right, var(--primary) 0%, var(--primary) ${initialPercent}%, #ddd ${initialPercent}%, #ddd 100%)`;
}

// Particle effects removed for cleaner UI

// ============================================================
// FORM SUBMISSION & RECOMMENDATIONS
// ============================================================

document.getElementById('preferencesForm')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = new FormData(e.target);
    const submitBtn = document.getElementById('submitBtn');
    const loadingDiv = document.getElementById('loading');
    const resultDiv = document.getElementById('result');
    const emptyState = document.getElementById('empty-state');
    
    // Get hunger value (0 = light, 1 = medium, 2 = heavy)
    const hungerMap = { 0: 'low', 1: 'medium', 2: 'high' };
    const hungerLevel = hungerMap[formData.get('hunger')];
    
    const data = {
        mood: formData.get('mood'),
        time_of_day: formData.get('time_of_day'),
        hunger: hungerLevel,
        diet: formData.get('diet'),
        weather: formData.get('weather'),
        goal: formData.get('goal'),
        spice: formData.get('spice'),
        description: formData.get('description')
    };
    
    // Show loading state with animation
    submitBtn.classList.add('loading');
    submitBtn.disabled = true;
    
    loadingDiv.style.display = 'block';
    resultDiv.style.display = 'none';
    emptyState.style.display = 'none';
    
    try {
        const response = await fetch('/api/recommend', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });
        
        const responseData = await response.json();
        
        if (responseData.status === 'success') {
            displayRecommendation(responseData.recommendation);
            showToast('🎉 Perfect recommendation found!', 3000, 'success');
            createConfetti();
        } else {
            showToast('Error: ' + responseData.message, 3000, 'error');
        }
    } catch (error) {
        showToast('Error fetching recommendation: ' + error.message, 3000, 'error');
        console.error('Error:', error);
    } finally {
        submitBtn.classList.remove('loading');
        submitBtn.disabled = false;
        loadingDiv.style.display = 'none';
    }
});

// ============================================================
// DISPLAY RECOMMENDATION
// ============================================================

function displayRecommendation(recommendation) {
    const resultDiv = document.getElementById('result');
    const emptyState = document.getElementById('empty-state');
    
    const topFood = recommendation.foods_detailed[0];
    const alternatives = recommendation.foods_detailed.slice(1, 3);
    
    // Extract percentage number
    const confidencePercent = parseInt(topFood.confidence_pct);
    
    let html = `
        <div class="food-card-main animate-reveal">
            <div class="food-card-emoji">🎯</div>
            <h3>${topFood.food_name}</h3>
            <p class="food-description">${topFood.description}</p>
            
            <div class="food-details">
                <div class="detail-item">
                    <i class="fas fa-clock"></i>
                    <span><strong>Prep:</strong> ${topFood.prep_time}</span>
                </div>
                <div class="detail-item">
                    <i class="fas fa-fire"></i>
                    <span><strong>Calories:</strong> ${topFood.calories}</span>
                </div>
            </div>
            
            <div class="confidence-section">
                <div class="confidence-label">
                    <strong>AI Confidence:</strong>
                    <span class="confidence-percentage">${confidencePercent}%</span>
                </div>
                <div class="confidence-bar">
                    <div class="confidence-fill" style="width: 0; --target-width: ${confidencePercent}%;" data-width="${confidencePercent}"></div>
                </div>
            </div>
        </div>
    `;
    
    if (alternatives.length > 0) {
        html += `
            <div class="alternatives animate-reveal" style="animation-delay: 0.3s">
                <h4><i class="fas fa-list"></i> Other Great Options</h4>
        `;
        
        alternatives.forEach((food, index) => {
            const altPercent = parseInt(food.confidence_pct);
            html += `
                <div class="alternative-item" style="animation-delay: ${(index + 1) * 0.15}s">
                    <div class="alt-info">
                        <div class="alternative-name">${index + 2}. ${food.food_name}</div>
                        <div class="alt-meta">
                            ${food.prep_time} • ${food.calories}
                        </div>
                    </div>
                    <div class="alternative-confidence">
                        <span class="alt-percent">${altPercent}%</span>
                    </div>
                </div>
            `;
        });
        
        html += `</div>`;
    }
    
    resultDiv.innerHTML = html;
    resultDiv.style.display = 'block';
    emptyState.style.display = 'none';
    
    // Animate confidence bars
    setTimeout(() => {
        document.querySelectorAll('.confidence-fill').forEach(bar => {
            const targetWidth = bar.getAttribute('data-width');
            bar.style.width = targetWidth + '%';
        });
    }, 100);
}

// ============================================================
// LOAD INDIAN FOODS
// ============================================================

async function loadIndianFoods() {
    try {
        const response = await fetch('/api/indian-foods');
        const foodData = await response.json();
        
        if (foodData.status === 'success') {
            displayIndianFoods(foodData.foods);
            document.getElementById('indianCount').textContent = foodData.count;
        }
    } catch (error) {
        console.error('Error loading Indian foods:', error);
    }
}

function displayIndianFoods(foods) {
    const grid = document.getElementById('indianFoodsGrid');
    
    let html = '';
    foods.forEach((food, index) => {
        const emoji = {
            'light meal': '🥗',
            'heavy meal': '🍜',
            'snack': '🥒',
            'comfort food': '🍲'
        }[food.category] || '🍽️';
        
        const vegTag = food.veg ? 'veg' : 'non-veg';
        const vegLabel = food.veg ? 'Vegetarian' : 'Non-Veg';
        
        html += `
            <div class="food-card hover-lift" style="animation-delay: ${index * 0.05}s">
                <div class="food-card-header">${emoji}</div>
                <div class="food-card-content">
                    <h3>${food.name}</h3>
                    <p>${food.description}</p>
                    <div class="food-card-meta">
                        <span class="food-tag ${vegTag}">${vegLabel}</span>
                        <span class="food-tag">${food.cuisine}</span>
                    </div>
                    <div class="food-info">
                        <div class="food-prep"><i class="fas fa-clock"></i> ${food.prep_time}</div>
                        <div class="food-calories"><i class="fas fa-fire"></i> ${food.calories}</div>
                    </div>
                </div>
            </div>
        `;
    });
    
    grid.innerHTML = html;
}

// ============================================================
// LOAD STATISTICS
// ============================================================

async function loadStatistics() {
    try {
        const response = await fetch('/api/cuisine-stats');
        const statsData = await response.json();
        
        if (statsData.status === 'success') {
            createCuisineChart(statsData.stats);
        }
    } catch (error) {
        console.error('Error loading statistics:', error);
    }
}

function createCuisineChart(stats) {
    const ctx = document.getElementById('cuisineChart')?.getContext('2d');
    if (!ctx) return;
    
    const colors = {
        'Indian': '#FF6B6B',
        'Western': '#4ECDC4'
    };
    
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: Object.keys(stats),
            datasets: [{
                data: Object.values(stats),
                backgroundColor: Object.keys(stats).map(key => colors[key]),
                borderColor: '#fff',
                borderWidth: 3,
                hoverOffset: 10
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        padding: 20,
                        font: {
                            size: 14,
                            weight: 'bold'
                        }
                    }
                },
                tooltip: {
                    backgroundColor: 'rgba(0, 0, 0, 0.8)',
                    padding: 12,
                    titleFont: {
                        size: 14
                    },
                    bodyFont: {
                        size: 13
                    },
                    callbacks: {
                        label: function(context) {
                            return context.label + ': ' + context.parsed + ' dishes';
                        }
                    }
                }
            }
        }
    });
}

// ============================================================
// INTERSECTION OBSERVER FOR ANIMATIONS
// ============================================================

const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate-in');
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observe elements for staggered animation
document.querySelectorAll('.stat-card, .food-card, .section-title').forEach(el => {
    observer.observe(el);
});

// ============================================================
// SMOOTH SCROLL & NAV EFFECTS
// ============================================================

document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', (e) => {
        const href = link.getAttribute('href');
        if (href.startsWith('#')) {
            e.preventDefault();
            scrollToElement(href.substring(1));
        }
    });
});

// ============================================================
// ============================================================
// DARK MODE TOGGLE
// ============================================================

function toggleTheme() {
    const html = document.documentElement;
    const currentTheme = html.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    html.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    
    // Update icon
    const themeIcon = document.querySelector('.theme-toggle i');
    if (newTheme === 'dark') {
        themeIcon.classList.remove('fa-moon');
        themeIcon.classList.add('fa-sun');
    } else {
        themeIcon.classList.remove('fa-sun');
        themeIcon.classList.add('fa-moon');
    }
    
    // Show toast notification
    showToast(`Switched to ${newTheme} mode! 🌙`, 'success');
}

function initializeTheme() {
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
    
    const themeIcon = document.querySelector('.theme-toggle i');
    if (savedTheme === 'dark') {
        themeIcon.classList.remove('fa-moon');
        themeIcon.classList.add('fa-sun');
    }
}

// ============================================================
// 3D CARD HOVER EFFECT
// ============================================================

document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.food-card, .stat-card');
    
    cards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;
            
            const rotateX = (y / rect.height) * 5;
            const rotateY = (x / rect.width) * -5;
            
            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.02)`;
        });
        
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) scale(1)';
        });
    });
});

// ============================================================
// PARALLAX BACKGROUND EFFECT
// ============================================================

window.addEventListener('mousemove', (e) => {
    const blobs = document.querySelectorAll('.blob');
    blobs.forEach((blob, index) => {
        const offsetX = (e.clientX / window.innerWidth) * (index + 1) * 10;
        const offsetY = (e.clientY / window.innerHeight) * (index + 1) * 10;
        blob.style.transform = `translate(${offsetX}px, ${offsetY}px)`;
    });
});

// ============================================================
// INITIALIZATION
// ============================================================

document.addEventListener('DOMContentLoaded', () => {
    console.log('🍽️ FoodAI Enhanced Website Initialized');
    
    // Initialize theme
    initializeTheme();
    
    // Load data
    loadIndianFoods();
    loadStatistics();
    
    // Add animation delay to stat cards
    document.querySelectorAll('.stat-card').forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
    });
    
    // Animate hero words
    const words = document.querySelectorAll('.hero-title .word');
    words.forEach((word, index) => {
        word.style.animationDelay = `${index * 0.2}s`;
    });
    
    // Smooth reveal on page load
    setTimeout(() => {
        document.body.classList.add('loaded');
    }, 100);
});

// ============================================================
// KEYBOARD SHORTCUTS
// ============================================================

document.addEventListener('keydown', (e) => {
    // Alt + R to focus on recommender
    if (e.altKey && e.key === 'r') {
        e.preventDefault();
        document.getElementById('preferencesForm')?.focus();
        showToast('📝 Recommender form focused (Alt+R)', 2000);
    }
    
    // Alt + I to scroll to Indian foods
    if (e.altKey && e.key === 'i') {
        e.preventDefault();
        scrollToElement('indian-foods');
        showToast('🍜 Scrolling to Indian foods (Alt+I)', 2000);
    }
    
    // Alt + S to scroll to stats
    if (e.altKey && e.key === 's') {
        e.preventDefault();
        scrollToElement('stats');
        showToast('📊 Scrolling to statistics (Alt+S)', 2000);
    }
});

// ============================================================
// WINDOW RESIZE HANDLER
// ============================================================

window.addEventListener('resize', () => {
    const canvas = document.getElementById('particle-canvas');
    if (canvas) {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
});

// ============================================================
// PERFORMANCE OPTIMIZATION
// ============================================================

window.addEventListener('load', () => {
    console.log('✅ Page fully loaded - all resources ready');
    
    // Preload images
    const images = document.querySelectorAll('img');
    images.forEach(img => {
        const imgCopy = new Image();
        imgCopy.src = img.src;
    });
});
