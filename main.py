import sys
from recipe_transformer import make_recipe

def usage():
    print "python main.py url"

def main(url="https://www.allrecipes.com/recipe/219963/",make_vegan=True,make_non_vegan=True,make_healthy=True,make_unhealthy=True,change_style=True,style="asian",DIY_to_easy=True,change_cooking_method=True,method=("heat","fry")):
    recipe = make_recipe(url)
    
    if make_vegan:
        recipe = recipe.make_vegan()
    print recipe,'\n'
    if make_non_vegan:
        recipe = recipe.make_non_vegan()
    print recipe,'\n'
    if make_healthy:
        recipe = recipe.make_healthy()
    print recipe,'\n'
    if make_unhealthy:
        recipe = recipe.make_unhealthy()
    print recipe,'\n'
    if change_style:
        recipe = recipe.change_style(style)
    print recipe,'\n'
    if DIY_to_easy:
        recipe = recipe.DIY_to_easy()
    print recipe,'\n'
    if change_cooking_method:
        recipe = recipe.change_cooking_method(method[0],method[1])
    print recipe
