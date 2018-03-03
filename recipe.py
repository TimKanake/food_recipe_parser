import copy
import random
from ingredient import Ingredient
from ingredient_substitutes import vegan_substitutes, healthy_substitutes, unhealthy_ingredients, reduction_substitutes

def pretty_print_list(list_in):
    str_out = "\n"
    for x in list_in:
        str_out += str(x) + "\n"
    return str_out

class Recipe:
    def __init__(self, name = None, ingredients = [], steps = [], tools = [], method = None, nutrition = None):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        self.tools = tools
        self.method = method
        self.nutrition = nutrition

    #inputs: None
    #outputs: new Recipe Object
    def __str__(self):

        ingredients_ppstring = pretty_print_list(self.ingredients)
        steps_ppstring = pretty_print_list(self.steps)

        return """Recipe Name: {0!s}\nIngredients: {1!s}\nSteps: {2!s}\nTools: {3!s}\nMethod: {4!s}\nNutrition {5!s}""".format(self.name, ingredients_ppstring, steps_ppstring, self.tools, self.method, self.nutrition)

    def make_vegan(self):
        swapped_ingredients = {} #Keep track of swapped ingredients for substitution in steps
        vegan_recipe = copy.deepcopy(self) #deep copy our recipe object

        #swap out the ingredients for vegan substitutes
        for i in range(len(vegan_recipe.ingredients)):
            ingredient = vegan_recipe.ingredients[i].name.lower()
            if ingredient in vegan_substitutes.keys():
                vegan_recipe.ingredients[i].name = vegan_substitutes[ingredient]
                swapped_ingredients[ingredient] = vegan_substitutes[ingredient]

        #fix steps based on substitutions
        for i in range(len(vegan_recipe.steps)):
            step = vegan_recipe.steps[i]
            for replacement in swapped_ingredients.keys():
                step.replace(replacement, swapped_ingredients[replacement])


        return vegan_recipe

    #inputs: percent we want to reduce unhealthy ingredients (int)
    #outputs: new Recipe Object
    ###TIM DOES THIS
    def make_healthy(self):
        choice = input('Choose one of the following options to make your recipe healthier: (1) Substitute unhealthy\
         ingredients with healthier ingredients, (2) Reduce amount of secondary unhealthy ingredients, (3)\
          Change cooking method. Enter your choice by pressing 1, 2 or 3:  ')

        healthy_recipe = copy.deepcopy(self)
        if choice == 3:
            # choice 1
            # define method of choosing cooking method
            pass
        elif choice == 2:
            # choice 2
            reduced_ingredient = {}
            for i in range(len(healthy_recipe.ingredients)):
                ingredient = healthy_recipe.ingredients[i].name.lower()
                for j in reduction_substitutes:
                    if ingredient == reduction_substitutes[j].name:
                        ingredient.quantity = ingredient.quantity * reduction_substitutes[j].ratio
                        if reduction_substitutes[j].supplement is not None:
                            healthy_recipe.ingredients.append(Ingredient(reduction_substitutes[j].supplement))
                        reduced_ingredient[ingredient] = ingredient + reduction_substitutes[j].supplement

            for i in range(len(healthy_recipe.steps)):
                step = healthy_recipe[i].step
                for reduced in reduced_ingredient.keys():
                    step.replace(reduced, reduced_ingredient[reduced])
        else:
            #choice 1 and DEFAULT
            swapped_ingredients = {}
            for i in range(len(unhealthy_ingredients)):
                temp_unhealthy = unhealthy_ingredients[i]
                for j in range(len(healthy_recipe.ingredients)):
                    ingredient = healthy_recipe.ingredients[j].name.lower()
                    if ingredient in temp_unhealthy:
                        substitute = healthy_substitutes[i][random.randrange(0, len(healthy_substitutes[i]), 1)]
                        healthy_recipe.ingredients[j].name = substitute
                        swapped_ingredients[ingredient] = substitute

            for i in range(len(healthy_recipe.steps)):
                step = healthy_recipe.steps[i]
                for substitute in swapped_ingredients.keys():
                    step.replace(substitute, swapped_ingredients[substitute])

        return healthy_recipe


    ###JIMMY DOES THIS
    def change_style(self, style):
        pass

    def DIY_to_easy(self):
        pass

    def change_cooking_method(self, method):
        pass


    #inputs: none
    #outputs: none
    ###JIMMY DOES OUTPuTS
    def display_recipe(self):
        print "These are the ingredients you will need: "
        for ingredient in self.ingredients:
            print ingredient.get_ingredient_string()

        for step in self.steps:
            print step
            input("Press Enter to continue...")

        return None



