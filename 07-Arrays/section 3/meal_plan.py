meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
   ["Pancakes", "Sandwich", "Steak"],
   ["Smoothie", "Chicken Wrap", "Salmon"],
   ["Eggs", "Pasta", "Soup"],
   ["Toast", "Burrito", "Pizza"],
   ["Cereal", "Salad", "Fish Tacos"],
   ["Bagel", "Rice and Beans", "Stir-fry"]
]


def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday",
      "Thursday", "Friday", "Saturday", "Sunday"]
   return weekdays[n-1]

def day_meal_plan(meal_plan, day_number):
   return f"{weekday(day_number)} : {meal_plan[day_number-1]}"

print("WEEKLY MEAL PLAN")
print("Breakfast, Lunch, Dinner")
print("==========================")
print(day_meal_plan(meal_plan, 1))
print(day_meal_plan(meal_plan, 2))
print(day_meal_plan(meal_plan, 3))
print(day_meal_plan(meal_plan, 4))
print(day_meal_plan(meal_plan, 5))
print(day_meal_plan(meal_plan, 6))
print(day_meal_plan(meal_plan, 7))
