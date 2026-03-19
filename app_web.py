"""
Flask Web App for Food Recommendation System
Serves an interactive website with animations
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import sys
from pathlib import Path
import json

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from predict import recommend_food_hybrid
from food_database import get_indian_foods, get_cuisine_stats

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/api/recommend', methods=['POST'])
def get_recommendation():
    """API endpoint for food recommendations"""
    try:
        data = request.json
        
        result = recommend_food_hybrid(
            mood=data.get('mood', 'happy'),
            time_of_day=data.get('time_of_day', 'afternoon'),
            hunger=data.get('hunger', 'medium'),
            diet=data.get('diet', 'veg'),
            weather=data.get('weather', 'hot'),
            goal=data.get('goal', 'maintenance'),
            spice=data.get('spice', 'medium'),
            food_description=data.get('description', ''),
            return_details=True
        )
        
        return jsonify({
            'status': 'success',
            'recommendation': result
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

@app.route('/api/indian-foods', methods=['GET'])
def get_indian_foods_list():
    """Get list of all Indian foods"""
    try:
        indian_foods = get_indian_foods()
        return jsonify({
            'status': 'success',
            'foods': indian_foods,
            'count': len(indian_foods)
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

@app.route('/api/cuisine-stats', methods=['GET'])
def get_stats():
    """Get cuisine statistics"""
    try:
        stats = get_cuisine_stats()
        return jsonify({
            'status': 'success',
            'stats': stats
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

if __name__ == '__main__':
    print("🍽️  Food Recommendation Website Starting...")
    print("\n" + "="*60)
    print("LOCAL ACCESS:     http://localhost:5000")
    print("NETWORK ACCESS:   http://<your-ip>:5000")
    print("="*60)
    print("\nTo find your IP address:")
    print("  Windows: Open CMD and type: ipconfig")
    print("  Look for 'IPv4 Address' (usually 192.168.x.x or 10.x.x.x)")
    print("\nShare this link with others on your network!")
    print("="*60 + "\n")
    app.run(debug=True, host='0.0.0.0', port=5000)
