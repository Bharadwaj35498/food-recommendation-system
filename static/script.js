// ============================================================
// FOOD RECOMMENDATION WEBSITE - JAVASCRIPT
// ============================================================

// Utility: Show toast notification
function showToast(message, duration = 3000) {
    const toast = document.getElementById('toast');
    toast.textContent = message;
    toast.classList.add('show');
    
    setTimeout(() => {
        toast.classList.remove('show');
    }, duration);
}

// Utility: Scroll to element
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
// FORM SUBMISSION & RECOMMENDATIONS
// ============================================================

document.getElementById('preferencesForm').addEventListener('submit', async (e) => {
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
    
    // Show loading state
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
        
        const result = await response.json();
        
        if (result.status === 'success') {
            displayRecommendation(result.recommendation);
            showToast('🎉 Perfect recommendation found!');
        } else {
            showToast('Error: ' + result.message);
        }
    } catch (error) {
        showToast('Error fetching recommendation: ' + error.message);
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
    
    let html = `
        <div class="food-card-main">
            <h3>🎯 ${topFood.food_name}</h3>
            <p>${topFood.description}</p>
            
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
            
            <div class="detail-item" style="margin-top: 1.5rem;">
                <strong>Confidence:</strong> ${topFood.confidence_pct}
            </div>
            <div class="confidence-bar">
                <div class="confidence-fill" style="width: ${topFood.confidence_pct}"></div>
            </div>
        </div>
    `;
    
    if (alternatives.length > 0) {
        html += `
            <div class="alternatives">
                <h4><i class="fas fa-list"></i> Other Great Options</h4>
        `;
        
        alternatives.forEach((food, index) => {
            html += `
                <div class="alternative-item">
                    <div>
                        <div class="alternative-name">${index + 2}. ${food.food_name}</div>
                        <div style="font-size: 0.85rem; color: #666; margin-top: 0.3rem;">
                            ${food.prep_time} • ${food.calories}
                        </div>
                    </div>
                    <div class="alternative-confidence">${food.confidence_pct}</div>
                </div>
            `;
        });
        
        html += `</div>`;
    }
    
    resultDiv.innerHTML = html;
    resultDiv.style.display = 'block';
    emptyState.style.display = 'none';
}

// ============================================================
// LOAD INDIAN FOODS
// ============================================================

async function loadIndianFoods() {
    try {
        const response = await fetch('/api/indian-foods');
        const result = await response.json();
        
        if (result.status === 'success') {
            displayIndianFoods(result.foods);
            document.getElementById('indianCount').textContent = result.count;
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
            <div class="food-card" style="animation-delay: ${index * 0.05}s">
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
        const result = await response.json();
        
        if (result.status === 'success') {
            createCuisineChart(result.stats);
        }
    } catch (error) {
        console.error('Error loading statistics:', error);
    }
}

function createCuisineChart(stats) {
    const ctx = document.getElementById('cuisineChart').getContext('2d');
    
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
                        font: {
                            size: 14,
                            weight: 'bold'
                        },
                        padding: 20,
                        usePointStyle: true
                    }
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const total = context.dataset.data.reduce((a, b) => a + b, 0);
                            const percentage = ((context.parsed / total) * 100).toFixed(1);
                            return `${context.label}: ${context.parsed} dishes (${percentage}%)`;
                        }
                    }
                }
            }
        }
    });
}

// ============================================================
// DYNAMIC HUNGER LEVEL LABEL
// ============================================================

document.getElementById('hunger').addEventListener('input', function(e) {
    const labels = ['Light', 'Medium', 'Heavy'];
    const index = parseInt(e.target.value);
    const label = document.querySelector('.slider-labels span:nth-child(' + (index + 1) + ')');
    if (label) {
        label.style.fontWeight = 'bold';
        label.style.color = '#FF6B6B';
    }
});

// ============================================================
// SMOOTH SCROLL FOR NAV LINKS
// ============================================================

document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href.startsWith('#')) {
            e.preventDefault();
            scrollToElement(href.substring(1));
        }
    });
});

// ============================================================
// ENHANCE HOVER EFFECTS WITH MOUSE TRACKING
// ============================================================

const foodCards = document.querySelectorAll('.food-card');
foodCards.forEach(card => {
    card.addEventListener('mousemove', function(e) {
        const rect = this.getBoundingClientRect();
        const x = e.clientX - rect.left - rect.width / 2;
        const y = e.clientY - rect.top - rect.height / 2;
        const distance = Math.sqrt(x * x + y * y);
        
        if (distance < 150) {
            this.style.transform = `perspective(1000px) rotateX(${-y * 0.01}deg) rotateY(${x * 0.01}deg) scale(1.05)`;
        }
    });
    
    card.addEventListener('mouseleave', function() {
        this.style.transform = '';
    });
});

// ============================================================
// PARALLAX EFFECT FOR BACKGROUND
// ============================================================

window.addEventListener('mousemove', function(e) {
    const blobs = document.querySelectorAll('.blob');
    blobs.forEach((blob, index) => {
        const offsetX = (e.clientX / window.innerWidth) * (index + 1) * 10;
        const offsetY = (e.clientY / window.innerHeight) * (index + 1) * 10;
        blob.style.transform = `translate(${offsetX}px, ${offsetY}px)`;
    });
});

// ============================================================
// INTERSECTION OBSERVER FOR LAZY ANIMATIONS
// ============================================================

const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.animation = entry.target.style.animation || 'fadeInUp 0.6s ease forwards';
        }
    });
}, observerOptions);

document.querySelectorAll('.food-card, .stat-card, .alternative-item').forEach(el => {
    observer.observe(el);
});

// ============================================================
// INITIALIZE ON PAGE LOAD
// ============================================================

document.addEventListener('DOMContentLoaded', function() {
    console.log('🍽️ FoodAI Website Initialized');
    loadIndianFoods();
    loadStatistics();
    
    // Add staggered animation to word spans in hero
    const words = document.querySelectorAll('.hero-title .word');
    words.forEach((word, index) => {
        word.style.animationDelay = `${index * 0.2}s`;
    });
});

// ============================================================
// KEYBOARD SHORTCUTS
// ============================================================

document.addEventListener('keydown', function(e) {
    // Alt + R to focus on recommender
    if (e.altKey && e.key === 'r') {
        e.preventDefault();
        document.getElementById('preferencesForm').focus();
        showToast('📝 Recommender form focused (Alt+R)');
    }
    
    // Alt + I to scroll to Indian foods
    if (e.altKey && e.key === 'i') {
        e.preventDefault();
        scrollToElement('indian-foods');
        showToast('🍜 Scrolling to Indian foods (Alt+I)');
    }
    
    // Alt + S to scroll to stats
    if (e.altKey && e.key === 's') {
        e.preventDefault();
        scrollToElement('stats');
        showToast('📊 Scrolling to statistics (Alt+S)');
    }
});

// ============================================================
// PERFORMANCE OPTIMIZATION
// ============================================================

// Preload images
window.addEventListener('load', function() {
    console.log('✅ Page fully loaded - all resources ready');
});

// Handle window resize for responsive behavior
let resizeTimeout;
window.addEventListener('resize', function() {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(function() {
        console.log('Window resized');
    }, 250);
});
