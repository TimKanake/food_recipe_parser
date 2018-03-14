import sys
from recipe_transformer import make_recipe

def usage():
    print "python main.py url"

def main(url="https://www.allrecipes.com/recipe/21736/",make_vegan=False,make_non_vegan=False,make_healthy=False,make_unhealthy=False,change_style=True,style="Mexican",DIY_to_easy=True,change_cooking_method=False,method=("heat","fry")):
    recipe = make_recipe(url)
    
    if make_vegan:
        print "\n\nMake Vegan\n"
        recipe = recipe.make_vegan()
        print recipe,'\n'
    if make_non_vegan:
        print "\n\nMake Non-Vegan\n"
        recipe = recipe.make_non_vegan()
        print recipe,'\n'
    if make_healthy:
        print "\n\nMake Healthy\n"
        recipe = recipe.make_healthy()
        print recipe,'\n'
    if make_unhealthy:
        print "\n\nMake Unealthy\n"
        recipe = recipe.make_unhealthy()
        print recipe,'\n'
    if change_style:
        print "\n\nChange Style "+style[0].upper()+style[1:]+'\n'
        recipe = recipe.change_style(style)
        print recipe,'\n'
    if DIY_to_easy:
        print "\n\nDIY to Easy\n"
        recipe = recipe.DIY_to_easy()
        print recipe,'\n'
    if change_cooking_method:
        print "\n\nChange Method From "+method[0][0].upper()+method[0][1:]+" to "+method[1][0].upper()+method[1][1:]+'\n'
        recipe = recipe.change_cooking_method(method[0],method[1])
        print recipe,'\n'

main()
