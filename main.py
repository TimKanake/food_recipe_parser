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
        print recipe.make_unhealthy()
    elif function == "change_style":
        print recipe.change_style(function_param)
    elif function == "DIY_to_easy":
        print recipe.DIY_to_easy()
    elif function == "change_cooking_method":
        print recipe.change_cooking_method(function_param)

    return

main()