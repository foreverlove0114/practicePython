from typing import List


def make_juice(recipes: List[str], fruits: str) -> int:
    # Parse recipes into a dictionary: {fruit: required_count}
    recipe_dict = {}
    for recipe in recipes:
        fruit, count = recipe.split()
        recipe_dict[fruit] = int(count)

    # Count available fruits
    fruit_counts = {}
    for fruit in fruits:
        if fruit in recipe_dict:  # Only count fruits that are in recipes
            fruit_counts[fruit] = fruit_counts.get(fruit, 0) + 1

    # Calculate maximum glasses per recipe
    total_glasses = 0
    for fruit, required in recipe_dict.items():
        available = fruit_counts.get(fruit, 0)
        total_glasses += available // required

    return total_glasses

print(make_juice(recipes=["A 3", "B 2"], fruits="AAABBB"))