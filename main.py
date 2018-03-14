import sys
from recipe_transformer import make_recipe

def usage():
    print "python main.py url"

def main(url="https://www.allrecipes.com/recipe/43655/",make_vegan=False,make_non_vegan=False,make_healthy=False,make_unhealthy=False,change_style=True,style="Mexican",DIY_to_easy=True,change_cooking_method=False,method=("heat","fry")):
    recipe = make_recipe(url)
    
    if make_vegan:
        recipe = recipe.make_vegan()
        print "\nMake Vegan\n"
        print recipe,'\n'
    if make_non_vegan:
        recipe = recipe.make_non_vegan()
        print "\nMake Non-Vegan\n"
        print recipe,'\n'
    if make_healthy:
        recipe = recipe.make_healthy()
        print "\nMake Healthy\n"
        print recipe,'\n'
    if make_unhealthy:
        recipe = recipe.make_unhealthy()
        print "\nMake Unealthy\n"
        print recipe,'\n'
    if change_style:
        recipe = recipe.change_style(style)
        print "\nChange Style "+style[0].upper()+style[1:]+'\n'
        print recipe,'\n'
    if DIY_to_easy:
        recipe = recipe.DIY_to_easy()
        print "\nDIY to Easy\n"
        print recipe,'\n'
    if change_cooking_method:
        recipe = recipe.change_cooking_method(method[0],method[1])
        print "\nChange Method From "+method[0][0].upper()+method[0][1:]+" to "+method[1][0].upper()+method[1][1:]+'\n'
        print recipe,'\n'

main()
