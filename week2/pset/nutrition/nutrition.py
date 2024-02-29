# Create a dictionary for the Raw Fruits Poster
CALORIES = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit":60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear":100,
    "pineapple": 50,
    "plums": 70,
    "strawberries":50,
    "sweet cherries":100,
    "tangerine": 50,
    "watermelon": 80,
}

# Prompt the user fot the fruit
fruit = input("Item: ")

# Remove any user error
fruit = fruit.strip().lower()

# Print the ans
if fruit in CALORIES:
    print("Calories:", CALORIES[fruit])
