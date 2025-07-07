# Write your solution here
def get_list_of_recipes(filename: str):
    splitted_recipes = []
    current_recipe = []

    with open(filename) as recipe_file:
        data = recipe_file.readlines()
        last_item = data[-1]
        for item in data:
            if item == "\n":
                if current_recipe:
                    splitted_recipes.append(current_recipe)
                    current_recipe = []
            elif item == last_item:
                if current_recipe:
                    current_recipe.append(item.strip())
                    splitted_recipes.append(current_recipe)
                    current_recipe = []
            else:
                current_recipe.append(item.strip())
    return splitted_recipes

def search_by_name(filename: str, word: str):
    list_recipes = []
    try:
        liste_recipes = get_list_of_recipes(f"src\\{filename}")
    except:
        liste_recipes = get_list_of_recipes(f"{filename}")      
    finally:
        for recipe in liste_recipes:
            if word.lower() in recipe[0].lower():
                list_recipes.append(recipe[0])                

    return list_recipes

def search_by_time(filename: str, prep_time: int):
    list_recipes = []
    try:
        liste_recipes = get_list_of_recipes(f"src\\{filename}")
    except:
        liste_recipes = get_list_of_recipes(f"{filename}")      
    finally:
        for recipe in liste_recipes:
            if prep_time >= int(recipe[1]):
                list_recipes.append(f"{recipe[0]}, preparation time {recipe[1]} min")
    return list_recipes

def search_by_ingredient(filename: str, ingredient: str):
    list_recipes = []
    try:
        liste_recipes = get_list_of_recipes(f"src\\{filename}")
    except:
        liste_recipes = get_list_of_recipes(f"{filename}")      
    finally:
        for recipe in liste_recipes:
            # print(recipe)
            ingredient_list = recipe[2:]
            if ingredient in ingredient_list:
                list_recipes.append(f"{recipe[0]}, preparation time {recipe[1]} min")
    return list_recipes

if __name__ == "__main__":
    # found_recipes = search_by_name("recipes1.txt", "cake")
    # found_recipes = search_by_name("recipes2.txt", "oat")
    # found_recipes = search_by_time("recipes1.txt", 20)
    # found_recipes = search_by_ingredient("recipes1.txt", "eggs")
    found_recipes = search_by_ingredient("recipes2.txt", "fish")
    print(found_recipes)