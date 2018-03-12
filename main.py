import sys
from recipe_transformer import make_recipe

def usage():
    print "python main.py url"

def main(url="https://www.allrecipes.com/recipe/219963/",make_vegan=False,make_non_vegan=False,make_healthy=False,make_unhealthy=False,change_style=False,style="",DIY_to_easy=False,change_cooking_method=False,method=""):
    recipe = make_recipe(url)
    
    if make_vegan:
        recipe = recipe.make_vegan()
    elif make_non_vegan:
        recipe = recipe.make_non_vegan()
    elif make_healthy:
        recipe = recipe.make_healthy()
    elif make_unhealthy:
        recipe = recipe.make_unhealthy()
    elif change_style:
        recipe = recipe.change_style('chinese')
    elif DIY_to_easy:
        recipe.DIY_to_easy()
    elif change_cooking_method:
        recipe = recipe.change_cooking_method('bake')
        
    print recipe

    return

main(make_unhealthy=True)
