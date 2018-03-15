import sys
from recipe_transformer import make_recipe

def usage():
    print "python main.py url"

def main(url="https://www.allrecipes.com/recipe/21736/",make_vegan=True,make_non_vegan=False,make_healthy=False,make_unhealthy=False,change_style=True,style="Mexican",DIY_to_easy=True,change_cooking_method=False,method=("heat","fry")):
    recipe = make_recipe(url)
    
    if make_vegan:
        print "\n\nMake Vegan\n"
        print recipe.make_vegan(),'\n'
    if make_non_vegan:
        print "\n\nMake Non-Vegan\n"
        print recipe.make_non_vegan(),'\n'
    if make_healthy:
        print "\n\nMake Healthy\n"
        print recipe.make_healthy(),'\n'
    if make_unhealthy:
        print "\n\nMake Unealthy\n"
        print recipe.make_unhealthy(),'\n'
    if change_style:
        print "\n\nChange Style "+style[0].upper()+style[1:]+'\n'
        print recipe.change_style(style),'\n'
    if DIY_to_easy:
        print "\n\nDIY to Easy\n"
        print recipe.DIY_to_easy(),'\n'
    if change_cooking_method:
        print "\n\nChange Method From "+method[0][0].upper()+method[0][1:]+" to "+method[1][0].upper()+method[1][1:]+'\n'
        print recipe.change_cooking_method(method[0],method[1]),'\n'

main()
