import sys
from recipe_transformer import make_recipe

def usage():
    print "python main.py url"

def main():
    url = ""
    function = ""
    function_param = ""

    try:
        url = sys.argv[1]
    except:
        pass
    try:
        function = sys.argv[2]
    except:
        pass
    try:
        function_param = sys.argv[3]
    except:
        pass


    recipe = make_recipe(url)

    if function == "make_vegan":
        print "reaches here"
        recipe.make_vegan().display_recipe()
    elif function == "make_non_vegan":
        recipe.make_non_vegan().display_recipe()
    elif function == "make_healthy":
        recipe.make_healthy().display_recipe()
    elif function == "make_unhealthy":
        recipe.make_unhealthy().display_recipe()
    elif function == "change_style":
        recipe.change_style(function_param).display_recipe()
    elif function == "DIY_to_easy":
        recipe.DIY_to_easy().display_recipe()
    elif function == "change_cooking_method":
        recipe.change_cooking_method(function_param).display_recipe()

    return

main()