# 🍽️ FoodAI Website - Complete Guide

## Overview

A beautiful, animated web interface for the food recommendation system built with Flask, HTML5, CSS3, and JavaScript. Features smooth animations, interactive UI, and a modern design.

## Features

### 🎨 Visual Design
- **Animated Background**: Floating blobs and emoji animations
- **Beautiful Gradients**: Modern color gradients throughout
- **Smooth Transitions**: All interactions have smooth animations
- **Responsive Design**: Works perfectly on mobile, tablet, and desktop
- **Dark Mode Ready**: Can be extended with dark mode support

### 🎯 Core Functionality
- **Mood-Based Recommendations**: 4 mood options (Happy, Sad, Stressed, Tired)
- **Time-Based Filtering**: Morning, Afternoon, Night preferences
- **Hunger Level Slider**: Visual gradient slider for hunger selection
- **Dietary Preferences**: Vegetarian vs Non-Vegetarian options
- **Weather Awareness**: Hot, Cold, or Rainy weather selection
- **Health Goals**: Weight Loss, Muscle Gain, Maintenance
- **Spice Preference**: Mild, Medium, or Hot spice levels
- **Free-Form Text**: Optional food cravings description

### 📊 Data Visualization
- **Real-Time Recommendations**: Shows top recommendation with confidence scores
- **Alternative Options**: Display 2-3 backup recommendations
- **Cuisine Statistics**: Pie chart showing Indian vs Western cuisine distribution
- **Indian Foods Showcase**: Grid display of 30+ Indian dishes
- **Detailed Information**: Prep time, calories, description for each food

### ⚡ Advanced Interactions
- **Loading Animations**: Spinner while fetching recommendations
- **Toast Notifications**: Success/error messages
- **Parallax Effects**: Background moves with mouse movement
- **3D Card Effects**: Food cards react to mouse position
- **Keyboard Shortcuts**:
  - `Alt+R`: Focus recommender form
  - `Alt+I`: Scroll to Indian foods
  - `Alt+S`: Scroll to statistics
- **Intersection Observer**: Lazy-load animations as sections come into view

## File Structure

```
food_recommendation_system/
├── app_web.py                 # Flask web server
├── templates/
│   └── index.html            # Main webpage with interactive UI
├── static/
│   ├── style.css             # All styling and animations
│   └── script.js             # JavaScript interactions
└── src/
    ├── predict.py            # Recommendation engine
    ├── food_database.py      # Food data and helpers
    └── ...                   # Other ML modules
```

## Setup & Running

### 1. Install Dependencies
```bash
pip install flask flask-cors
```

### 2. Start the Web Server
```bash
python app_web.py
```

Server will start at `http://localhost:5000`

### 3. Open in Browser
Visit: **http://localhost:5000**

## API Endpoints

### GET `/` 
- Returns the main HTML page
- **Response**: HTML page

### POST `/api/recommend`
- Get food recommendation based on preferences
- **Request Body**:
```json
{
    "mood": "happy",
    "time_of_day": "afternoon",
    "hunger": "medium",
    "diet": "veg",
    "weather": "hot",
    "goal": "maintenance",
    "spice": "medium",
    "description": "Something light and healthy"
}
```
- **Response**:
```json
{
    "status": "success",
    "recommendation": {
        "top_food_name": "Butter Chicken with Naan",
        "top_food_description": "...",
        "foods_detailed": [...],
        "confidence": 0.78,
        "foods_detailed": [...]
    }
}
```

### GET `/api/indian-foods`
- Get list of all Indian foods in database
- **Response**:
```json
{
    "status": "success",
    "foods": [...],
    "count": 30
}
```

### GET `/api/cuisine-stats`
- Get cuisine distribution statistics
- **Response**:
```json
{
    "status": "success",
    "stats": {
        "Indian": 22,
        "Western": 22
    }
}
```

## UI Sections

### 1. **Navigation Bar**
- Fixed sticky navigation
- Logo with animated spinner
- Quick links to all sections
- Fade-in animation on load

### 2. **Hero Section**
- Full-screen welcome message
- Animated word-by-word text
- CTA button with hover effects
- Floating emoji background

### 3. **Recommender Section**
- Left Panel: Interactive form with all preference options
  - Radio buttons for mood, time, diet, weather, goal
  - Range slider for hunger level
  - Textarea for optional description
  - Submit button with loading state
  
- Right Panel: Results display
  - Empty state message initially
  - Loading spinner while fetching
  - Main recommendation with confidence bar
  - Alternative options listed below
  - Prep time and calorie information

### 4. **Indian Foods Section**
- Grid of food cards (4 columns responsive)
- Each card shows:
  - Emoji representing category
  - Food name and description
  - Vegetarian/Non-Veg tag
  - Cuisine type (Indian/Western)
  - Prep time and calories
  - Hover animations (lift effect, shadow)

### 5. **Statistics Section**
- 4 stat cards showing:
  - Total foods (48)
  - Indian dishes count
  - Categories count (4)
  - Cuisines count (2)
- Doughnut chart with cuisine breakdown
- Chart.js integration with custom colors and tooltips

### 6. **Footer**
- Multiple sections with information
- Links and descriptions
- Copyright notice

## CSS Animations

### Entrance Animations
- `fadeInUp`: Elements fade in while moving up
- `fadeInDown`: Elements fade in while moving down
- `slideInLeft`: Elements slide from left
- `slideInRight`: Elements slide from right

### Continuous Animations
- `float`: Smooth floating motion
- `pulse`: Gentle scaling pulse
- `glow`: Glowing effect for buttons
- `spin`: Rotation animation for logo

### Interactive Animations
- `blobAnimation`: Organic blob movements
- `wordFadeIn`: Word-by-word hero title
- Hover effects on all interactive elements
- 3D transform effects on cards

## JavaScript Features

### Form Handling
- Form submission with validation
- Data collection from radio buttons and inputs
- Loading state management
- Error handling with try-catch blocks

### API Integration
- `fetch()` calls to backend endpoints
- JSON request/response handling
- Error messages and user feedback
- Toast notifications

### DOM Manipulation
- Dynamic HTML insertion for results
- Element show/hide based on state
- CSS class manipulation for animations
- Event listener management

### User Experience
- Keyboard shortcuts for accessibility
- Smooth scrolling to sections
- Parallax background effects
- Mouse-tracking 3D card effects
- Intersection Observer for lazy animations

### Performance
- Efficient event handling
- Debounced resize events
- Minimal DOM reflows
- CSS-based animations (GPU accelerated)

## Customization Guide

### Change Colors
Edit `:root` variables in `style.css`:
```css
:root {
    --primary: #FF6B6B;      /* Main brand color */
    --secondary: #4ECDC4;    /* Secondary accent */
    --accent: #FFE66D;       /* Highlight color */
    --dark: #2C3E50;         /* Text color */
    --light: #F7F7F7;        /* Background */
}
```

### Adjust Animation Timing
Modify animation durations in CSS `@keyframes`:
```css
@keyframes fadeInUp {
    /* Change time in: animation: fadeInUp 1s ease; */
}
```

### Add New Sections
1. Add HTML section with id
2. Add CSS styling for `.new-section`
3. Update scroll nav to include link
4. Add animation classes

### Modify Food Card Design
Edit `.food-card` and `.food-card-content` classes in CSS

## Browser Compatibility

- **Chrome**: Full support
- **Firefox**: Full support
- **Safari**: Full support
- **Edge**: Full support
- **Mobile**: Optimized for iOS and Android

## Performance Optimization

- **CSS Animations**: GPU-accelerated with `transform` and `opacity`
- **Lazy Loading**: Intersection Observer for animations
- **Efficient Selectors**: Minimized DOM queries
- **Image Optimization**: Emoji used instead of image files
- **Responsive Design**: Mobile-first approach

## Accessibility Features

- **Semantic HTML**: Proper heading hierarchy
- **ARIA Labels**: (Can be added)
- **Keyboard Navigation**: Alt+ shortcuts
- **Color Contrast**: WCAG AA compliant
- **Focus States**: Visible focus indicators

## Future Enhancements

1. **Dark Mode**: Add theme toggle with CSS variables
2. **Favorites**: Save recommended foods
3. **History**: Track previous recommendations
4. **User Profiles**: Save preferences
5. **Ratings**: Let users rate recommendations
6. **Mobile App**: Convert to React Native
7. **Voice Input**: Use speech recognition for preferences
8. **Share Feature**: Share recommendations on social media
9. **Offline Mode**: Service worker caching
10. **Animations Library**: Use GSAP or Framer Motion for advanced animations

## Troubleshooting

### Flask Server Won't Start
- Check port 5000 is not in use
- Verify Flask/Flask-CORS installed: `pip list | grep flask`
- Try different port: Edit `app_web.py` and change `port=5000`

### Page Not Loading
- Clear browser cache (Ctrl+Shift+Del)
- Check browser console for errors (F12)
- Verify server is running on correct port
- Check static folder path in templates

### Recommendations Not Showing
- Check browser network tab for API errors
- Verify ML models are trained in `models/` folder
- Check Flask console for error messages
- Restart Flask server

### Animations Not Working
- Check browser CSS support (older browsers may not support all)
- Verify `style.css` is loaded (check Network tab)
- Clear browser cache
- Try different browser

## Performance Tips

1. **Reduce Animation Count**: Comment out floating emojis if slow
2. **Simplified Blobs**: Use fewer or simpler blobs
3. **Disable Parallax**: Comment out mousemove listeners
4. **Preload Data**: Load Indian foods on page load (already done)
5. **Lazy Load Charts**: Initialize chart only when section is visible

## Credits

- **Framework**: Flask
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Charts**: Chart.js
- **Icons**: Font Awesome
- **Design**: Custom CSS animations
- **Backend**: Python ML Models (NLP + Metadata Pipelines)

## License

MIT License - Feel free to modify and use!

---

**Built with 💖 for food lovers and animation enthusiasts!** 🍽️✨
