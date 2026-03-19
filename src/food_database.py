"""
Food Suggestions Database
Maps food categories to specific food recommendations with details
Includes Indian, Western, and fusion cuisines
"""

FOOD_SUGGESTIONS = {
    "light meal": {
        "foods": [
            {
                "name": "Fruit Salad with Yogurt",
                "description": "Fresh mixed berries, melons, grapes with creamy yogurt and granola topping",
                "prep_time": "5 min",
                "calories": "150-200",
                "veg": True,
                "cuisine": "Western",
                "best_for": ["morning", "weight_loss"]
            },
            {
                "name": "Idli with Sambar",
                "description": "Steamed rice cakes with spiced sambar and coconut chutney",
                "prep_time": "15 min",
                "calories": "150-180",
                "veg": True,
                "cuisine": "Indian",
                "best_for": ["morning", "weight_loss"]
            },
            {
                "name": "Masala Dosa",
                "description": "Crispy crepe with spiced potato filling, sambar and chutney",
                "prep_time": "20 min",
                "calories": "200-250",
                "veg": True,
                "cuisine": "Indian",
                "best_for": ["morning"]
            },
            {
                "name": "Berry Oatmeal",
                "description": "Warm oatmeal topped with fresh berries, honey, and almonds",
                "prep_time": "10 min",
                "calories": "200-250",
                "veg": True,
                "cuisine": "Western",
                "best_for": ["morning", "tired"]
            },
            {
                "name": "Green Smoothie",
                "description": "Spinach, banana, protein powder, almond milk blended smooth",
                "prep_time": "3 min",
                "calories": "150-180",
                "veg": True,
                "cuisine": "Western",
                "best_for": ["morning", "weight_loss", "sad"]
            },
            {
                "name": "Upma with Vegetables",
                "description": "Savory semolina porridge with vegetables and mild spices",
                "prep_time": "15 min",
                "calories": "180-220",
                "veg": True,
                "cuisine": "Indian",
                "best_for": ["morning", "tired"]
            },
            {
                "name": "Egg White Scramble",
                "description": "Light scrambled egg whites with toast and fresh vegetables",
                "prep_time": "8 min",
                "calories": "180-220",
                "veg": False,
                "cuisine": "Western",
                "best_for": ["morning", "weight_loss"]
            },
            {
                "name": "Green Salad",
                "description": "Mixed greens with light vinaigrette, veggies, and light dressing",
                "prep_time": "5 min",
                "calories": "120-150",
                "veg": True,
                "cuisine": "Western",
                "best_for": ["afternoon", "weight_loss"]
            },
            {
                "name": "Poha (Flattened Rice)",
                "description": "Light flattened rice with peanuts, potatoes and mild spices",
                "prep_time": "10 min",
                "calories": "160-200",
                "veg": True,
                "cuisine": "Indian",
                "best_for": ["morning"]
            },
            {
                "name": "Steamed Broccoli Rice",
                "description": "Steamed broccoli with brown rice, light seasonings",
                "prep_time": "15 min",
                "calories": "200-250",
                "veg": True,
                "cuisine": "Western",
                "best_for": ["evening", "weight_loss"]
            }
        ]
    },
    
    "heavy meal": {
        "foods": [
            {
                "name": "Butter Chicken with Naan",
                "description": "Tender chicken in creamy tomato sauce with soft butter naan",
                "prep_time": "30 min",
                "calories": "550-650",
                "veg": False,
                "cuisine": "Indian",
                "best_for": ["night", "muscle_gain"]
            },
            {
                "name": "Spicy Grilled Chicken Rice",
                "description": "Chargrilled chicken breast with spiced basmati rice and grilled vegetables",
                "prep_time": "25 min",
                "calories": "450-550",
                "veg": False,
                "cuisine": "Western",
                "best_for": ["afternoon", "muscle_gain"]
            },
            {
                "name": "Chicken Biryani",
                "description": "Aromatic rice cooked with spiced chicken, saffron, and fresh herbs",
                "prep_time": "45 min",
                "calories": "600-700",
                "veg": False,
                "cuisine": "Indian",
                "best_for": ["night", "muscle_gain"]
            },
            {
                "name": "Paneer Tikka Masala with Rice",
                "description": "Creamy tomato-based curry with marinated paneer cubes and basmati rice",
                "prep_time": "35 min",
                "calories": "500-600",
                "veg": True,
                "cuisine": "Indian",
                "best_for": ["night", "muscle_gain"]
            },
            {
                "name": "Beef Steak with Sides",
                "description": "Juicy steak cooked to perfection with mashed potatoes and asparagus",
                "prep_time": "30 min",
                "calories": "600-750",
                "veg": False,
                "cuisine": "Western",
                "best_for": ["night", "muscle_gain", "tired"]
            },
            {
                "name": "Chole Bhature (Chickpea Curry & Fried Bread)",
                "description": "Spiced chickpea curry with fluffy fried bhature bread",
                "prep_time": "40 min",
                "calories": "550-650",
                "veg": True,
                "cuisine": "Indian",
                "best_for": ["afternoon"]
            },
            {
                "name": "Pancakes with Sausage",
                "description": "Fluffy pancakes with turkey sausage links and maple syrup",
                "prep_time": "15 min",
                "calories": "500-600",
                "veg": False,
                "cuisine": "Western",
                "best_for": ["morning", "muscle_gain"]
            },
            {
                "name": "Tandoori Chicken Rice",
                "description": "Spiced tandoori chicken with basmati rice and raita",
                "prep_time": "30 min",
                "calories": "550-650",
                "veg": False,
                "cuisine": "Indian",
                "best_for": ["afternoon", "muscle_gain", "happy"]
            },
            {
                "name": "Sausage Pepper Breakfast",
                "description": "Sausage patties with sautéed peppers and onions, hash browns",
                "prep_time": "20 min",
                "calories": "600-700",
                "veg": False,
                "cuisine": "Western",
                "best_for": ["morning", "muscle_gain"]
            },
            {
                "name": "Rogan Josh (Lamb Curry) with Naan",
                "description": "Tender lamb in aromatic curry with herbs and soft naan bread",
                "prep_time": "45 min",
                "calories": "650-750",
                "veg": False,
                "cuisine": "Indian",
                "best_for": ["night", "muscle_gain"]
            },
            {
                "name": "Turkey Meatballs",
                "description": "Lean turkey meatballs in marinara sauce with pasta",
                "prep_time": "25 min",
                "calories": "500-600",
                "veg": False,
                "cuisine": "Western",
                "best_for": ["afternoon", "weight_loss", "tired"]
            },
            {
                "name": "Palak Paneer (Spinach Paneer) with Rice",
                "description": "Creamy spinach curry with cottage cheese and basmati rice",
                "prep_time": "30 min",
                "calories": "480-580",
                "veg": True,
                "cuisine": "Indian",
                "best_for": ["night", "muscle_gain"]
            }
        ]
    },
    
    "snack": {
        "foods": [
            {
                "name": "Samosa",
                "description": "Crispy fried triangular pastry filled with spiced potatoes and peas",
                "prep_time": "20 min",
                "calories": "150-180",
                "veg": True,
                "cuisine": "Indian",
                "best_for": ["afternoon"]
            },
            {
                "name": "Hummus and Pita",
                "description": "Creamy hummus with whole wheat pita chips and fresh vegetables",
                "prep_time": "2 min",
                "calories": "150-180",
                "veg": True,
                "cuisine": "Western",
                "best_for": ["evening", "happy"]
            },
            {
                "name": "Pakora (Vegetable Fritters)",
                "description": "Golden fried chickpea flour batter with vegetables, spiced and crispy",
                "prep_time": "15 min",
                "calories": "140-180",
                "veg": True,
                "cuisine": "Indian",
                "best_for": ["afternoon"]
            },
            {
                "name": "Cheese and Crackers",
                "description": "Aged cheddar with whole grain crackers and fresh grapes",
                "prep_time": "3 min",
                "calories": "180-220",
                "veg": True,
                "cuisine": "Western",
                "best_for": ["afternoon", "tired"]
            },
            {
                "name": "Bhel Puri (Puffed Rice Mix)",
                "description": "Light puffed rice with chickpeas, onions, and tangy chutney",
                "prep_time": "5 min",
                "calories": "120-150",
                "veg": True,
                "cuisine": "Indian",
                "best_for": ["afternoon"]
            },
            {
                "name": "Mixed Nuts",
                "description": "Roasted almonds, cashews, walnuts with dried fruits",
                "prep_time": "0 min",
                "calories": "160-200",
                "veg": True,
                "cuisine": "Western",
                "best_for": ["afternoon", "stressed"]
            },
            {
                "name": "Methi Fafda (Fenugreek Snack)",
                "description": "Crispy fried chickpea flour noodles with sweet jaggery",
                "prep_time": "20 min",
                "calories": "170-210",
                "veg": True,
                "cuisine": "Indian",
                "best_for": ["afternoon"]
            },
            {
                "name": "Dark Chocolate Almonds",
                "description": "Dark chocolate (70%+) with roasted almonds and sea salt",
                "prep_time": "0 min",
                "calories": "140-180",
                "veg": True,
                "cuisine": "Western",
                "best_for": ["evening", "happy"]
            },
            {
                "name": "Chakli (Spiral Snack)",
                "description": "Golden spiral-shaped snack made with rice flour and spices",
                "prep_time": "25 min",
                "calories": "150-190",
                "veg": True,
                "cuisine": "Indian",
                "best_for": ["afternoon"]
            },
            {
                "name": "Berries with Cream",
                "description": "Fresh seasonal berries topped with whipped cream",
                "prep_time": "3 min",
                "calories": "120-150",
                "veg": True,
                "cuisine": "Western",
                "best_for": ["afternoon", "happy"]
            },
            {
                "name": "Masala Peanuts",
                "description": "Roasted peanuts with Indian spices, chili, and salt",
                "prep_time": "0 min",
                "calories": "160-200",
                "veg": True,
                "cuisine": "Indian",
                "best_for": ["afternoon"]
            },
            {
                "name": "Greek Yogurt Granola",
                "description": "Creamy Greek yogurt with homemade granola and honey",
                "prep_time": "2 min",
                "calories": "180-220",
                "veg": True,
                "cuisine": "Western",
                "best_for": ["morning", "stressed"]
            }
        ]
    },
    
    "comfort food": {
        "foods": [
            {
                "name": "Creamy Pasta",
                "description": "Creamy Alfredo pasta with garlic bread and fresh parmesan",
                "prep_time": "20 min",
                "calories": "550-650",
                "veg": True,
                "cuisine": "Western",
                "best_for": ["night", "stressed"]
            },
            {
                "name": "Khichdi (Rice & Lentils)",
                "description": "Soft rice and lentils cooked together with mild spices and ghee",
                "prep_time": "25 min",
                "calories": "250-300",
                "veg": True,
                "cuisine": "Indian",
                "best_for": ["night", "sad", "tired"]
            },
            {
                "name": "Warm Chocolate Cookies",
                "description": "Homemade chocolate chip cookies with a cold glass of milk",
                "prep_time": "30 min",
                "calories": "280-350",
                "veg": True,
                "cuisine": "Western",
                "best_for": ["afternoon", "sad"]
            },
            {
                "name": "Dal Makhani (Creamy Lentils)",
                "description": "Rich creamy lentil curry cooked with butter and cream",
                "prep_time": "40 min",
                "calories": "300-350",
                "veg": True,
                "cuisine": "Indian",
                "best_for": ["night", "sad", "stressed"]
            },
            {
                "name": "Mac and Cheese",
                "description": "Creamy mac and cheese with bacon bits and breadcrumb topping",
                "prep_time": "20 min",
                "calories": "450-550",
                "veg": False,
                "cuisine": "Western",
                "best_for": ["night", "sad", "stressed"]
            },
            {
                "name": "Rajma Chawal (Kidney Beans & Rice)",
                "description": "Spiced kidney beans with soft rice and fresh cilantro",
                "prep_time": "30 min",
                "calories": "280-320",
                "veg": True,
                "cuisine": "Indian",
                "best_for": ["night", "tired"]
            },
            {
                "name": "Chicken Noodle Soup",
                "description": "Warm chicken soup with soft noodles, carrots, and celery",
                "prep_time": "25 min",
                "calories": "250-300",
                "veg": False,
                "cuisine": "Western",
                "best_for": ["night", "tired", "sad"]
            },
            {
                "name": "Aloo Parathas (Potato Bread)",
                "description": "Stuffed Indian flatbread with spiced potatoes, served with butter",
                "prep_time": "30 min",
                "calories": "320-380",
                "veg": True,
                "cuisine": "Indian",
                "best_for": ["night", "sad", "stressed"]
            },
            {
                "name": "Sweet Potato Cinnamon",
                "description": "Baked sweet potato topped with cinnamon, butter, and brown sugar",
                "prep_time": "45 min",
                "calories": "180-220",
                "veg": True,
                "cuisine": "Western",
                "best_for": ["night", "sad", "weight_loss"]
            },
            {
                "name": "Halwa (Indian Dessert)",
                "description": "Warm semolina or carrot halwa with ghee, nuts, and jaggery",
                "prep_time": "25 min",
                "calories": "300-350",
                "veg": True,
                "cuisine": "Indian",
                "best_for": ["night", "sad"]
            }
        ]
    }
}


def get_food_suggestion(category, mood=None, time_of_day=None, diet=None, cuisine_preference=None):
    """
    Get a specific food suggestion from the database
    
    Args:
        category: Food category (light meal, heavy meal, snack, comfort food)
        mood: Optional mood filter
        time_of_day: Optional time filter
        diet: Optional diet filter (veg/non-veg)
        cuisine_preference: Optional cuisine filter (Indian/Western)
        
    Returns:
        dict: Food suggestion with details
    """
    if category not in FOOD_SUGGESTIONS:
        return None
    
    foods = FOOD_SUGGESTIONS[category]["foods"]
    
    # Filter by preferences
    if mood:
        foods = [f for f in foods if mood in f.get("best_for", [])]
    
    if time_of_day:
        foods = [f for f in foods if time_of_day in f.get("best_for", [])]
    
    if diet == "veg" and foods:
        foods_veg = [f for f in foods if f.get("veg", False)]
        foods = foods_veg if foods_veg else foods
    elif diet == "non-veg" and foods:
        foods_non_veg = [f for f in foods if not f.get("veg", True)]
        foods = foods_non_veg if foods_non_veg else foods
    
    if cuisine_preference and foods:
        cuisine_foods = [f for f in foods if f.get("cuisine") == cuisine_preference]
        foods = cuisine_foods if cuisine_foods else foods
    
    # Return first matching food or random from category
    if foods:
        return foods[0]
    else:
        return FOOD_SUGGESTIONS[category]["foods"][0]


def get_all_foods_for_category(category):
    """Get all food options for a category"""
    if category in FOOD_SUGGESTIONS:
        return FOOD_SUGGESTIONS[category]["foods"]
    return []


def get_category_info(category):
    """Get all info about a food category"""
    return FOOD_SUGGESTIONS.get(category, None)


def get_foods_by_cuisine(category, cuisine):
    """Get all foods of a specific cuisine in a category"""
    if category not in FOOD_SUGGESTIONS:
        return []
    
    foods = FOOD_SUGGESTIONS[category]["foods"]
    return [f for f in foods if f.get("cuisine") == cuisine]


def get_indian_foods():
    """Get all Indian foods"""
    all_indian = []
    for category in FOOD_SUGGESTIONS:
        foods = FOOD_SUGGESTIONS[category]["foods"]
        indian_foods = [f for f in foods if f.get("cuisine") == "Indian"]
        all_indian.extend(indian_foods)
    return all_indian


def get_cuisine_stats():
    """Get statistics about cuisines"""
    stats = {"Indian": 0, "Western": 0}
    for category in FOOD_SUGGESTIONS:
        foods = FOOD_SUGGESTIONS[category]["foods"]
        for food in foods:
            cuisine = food.get("cuisine", "Other")
            if cuisine in stats:
                stats[cuisine] += 1
    return stats
