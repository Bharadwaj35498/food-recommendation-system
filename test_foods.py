"""Quick test of the food recommendation system"""

from src.predict import recommend_food_hybrid

print("\n" + "=" * 70)
print("🍽️ TESTING FOOD RECOMMENDATION SYSTEM WITH SPECIFIC FOODS")
print("=" * 70)

# Test 1: Happy morning with light preference
print("\n📋 TEST 1: Happy Morning - Wants Light Food")
print("-" * 70)
result = recommend_food_hybrid(
    mood="happy",
    time_of_day="morning",
    hunger="medium",
    diet="veg",
    weather="hot",
    goal="weight_loss",
    spice="low",
    food_description="Something light and healthy"
)

print(f"\n🎯 TOP RECOMMENDATION: {result['top_food_name']}")
print(f"📝 {result['top_food_description']}")
print(f"💪 Confidence: {result['confidence']*100:.1f}%")

if result['foods_detailed']:
    print(f"\n📊 Food Details:")
    food = result['foods_detailed'][0]
    print(f"   • Category: {food['category']}")
    print(f"   • Prep Time: {food['prep_time']}")
    print(f"   • Calories: {food['calories']}")

print(f"\n🍽️ Other Options:")
for i, food in enumerate(result['foods_detailed'][1:], 1):
    print(f"   {i+1}. {food['food_name']} ({food['confidence_pct']})")
    print(f"      ⏱️  {food['prep_time']} | 🔥 {food['calories']} cal")

# Test 2: Stressed night with comfort preference
print("\n\n📋 TEST 2: Stressed Evening - Wants Comfort Food")
print("-" * 70)
result = recommend_food_hybrid(
    mood="stressed",
    time_of_day="night",
    hunger="high",
    diet="veg",
    weather="rainy",
    goal="maintenance",
    spice="high",
    food_description="Comfort food - something warm and filling"
)

print(f"\n🎯 TOP RECOMMENDATION: {result['top_food_name']}")
print(f"📝 {result['top_food_description']}")
print(f"💪 Confidence: {result['confidence']*100:.1f}%")

if result['foods_detailed']:
    print(f"\n📊 Food Details:")
    food = result['foods_detailed'][0]
    print(f"   • Category: {food['category']}")
    print(f"   • Prep Time: {food['prep_time']}")
    print(f"   • Calories: {food['calories']}")

# Test 3: Tired afternoon - no description
print("\n\n📋 TEST 3: Tired Afternoon - No Food Description")
print("-" * 70)
result = recommend_food_hybrid(
    mood="tired",
    time_of_day="afternoon",
    hunger="medium",
    diet="non-veg",
    weather="hot",
    goal="maintenance",
    spice="low"
)

print(f"\n🎯 TOP RECOMMENDATION: {result['top_food_name']}")
print(f"📝 {result['top_food_description']}")
print(f"💪 Confidence: {result['confidence']*100:.1f}%")

if result['foods_detailed']:
    print(f"\n📊 Food Details:")
    food = result['foods_detailed'][0]
    print(f"   • Category: {food['category']}")
    print(f"   • Prep Time: {food['prep_time']}")
    print(f"   • Calories: {food['calories']}")

# Test 4: Sad afternoon with snack
print("\n\n📋 TEST 4: Sad Afternoon - Wants Quick Snack")
print("-" * 70)
result = recommend_food_hybrid(
    mood="sad",
    time_of_day="afternoon",
    hunger="low",
    diet="veg",
    weather="rainy",
    goal="maintenance",
    spice="low",
    food_description="Quick pick-me-up snack",
    return_details=False
)

print(f"\n🎯 TOP RECOMMENDATION: {result['top_food_name']}")
print(f"📝 {result['top_food_description']}")
print(f"💪 Confidence: {result['confidence']*100:.1f}%")

print("\n" + "=" * 70)
print("✅ ALL TESTS COMPLETED SUCCESSFULLY!")
print("=" * 70)
print("\n🚀 System is ready! Try it with:")
print("   streamlit run app.py")
print("\n")
