import sys
from recipe_transformer import make_recipe

def usage():
    print "python main.py url"

def main(url="https://www.allrecipes.com/recipe/219963/",make_vegan=False,make_non_vegan=False,make_healthy=False,make_unhealthy=False,change_style=True,style="middle eastern",DIY_to_easy=False,change_cooking_method=False,method=("heat","fry")):
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
        print recipe,'\n'
