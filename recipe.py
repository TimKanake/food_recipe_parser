import copy
import random
from pretty_string import pretty_string
from ingredient import Ingredient
from ingredient_substitutes import vegan_substitutes, healthy_substitutes, unhealthy_ingredients, reduction_substitutes\
    , fix_step, non_vegan_substitutes, convert_quantity
from steps import Step

class Recipe:
    def __init__(self, name = None, ingredients = [], steps = [], tools = [], method = None, nutrition = None, is_vegan = False):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        self.tools = tools
        self.method = method
        self.nutrition = nutrition
        self.is_vegan = is_vegan

    #inputs: None
    #outputs: new Recipe Object
    def __str__(self):

        ingredients_ppstring = pretty_string(self.ingredients, "ingredients", "vertical")
        steps_ppstring = pretty_string(self.steps, "steps", "vertical")
        p_tools = pretty_string(self.tools, "tools", 'horizontal')
        p_methods = pretty_string(self.method, "methods", "horizontal")

        return """Recipe Name: {!s}\nIngredients: {!s}\nTools: {!s}\nMethod: {!s}\nSteps: {!s}\nNutrition {!s}""".format(self.name, ingredients_ppstring, p_tools, p_methods, steps_ppstring, self.nutrition)

    # inputs: None
    # outputs: new Vegan Recipe
    def make_vegan(self):
        if self.is_vegan:
            print 'There is already a vegan recipe.'
            return
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
        vegan_recipe.is_vegan = True
        return vegan_recipe

    # inputs: None
    # outputs: new non-vegan recipe
    def make_non_vegan(self):
        if not self.is_vegan:
            print 'This is already a non-vegan recipe.'
            return

        swapped_ingredients = {}
        non_vegan_recipe = copy.deepcopy(self)

        # swap out the ingredients for non-vegan substitutes
        for i in range(len(non_vegan_recipe.ingredients)):
            ingredient = non_vegan_recipe.ingredients[i].name.lower()
            if ingredient in non_vegan_substitutes.keys():
                non_vegan_recipe.ingredients[i].name = non_vegan_substitutes[ingredient]
                swapped_ingredients[ingredient] = non_vegan_substitutes[ingredient]

        # fix steps based on substitutions
        for i in range(len(non_vegan_recipe.steps)):
            step = non_vegan_recipe.steps[i]
            for replacement in swapped_ingredients.keys():
                step.replace(replacement, swapped_ingredients[replacement])
        non_vegan_recipe.is_vegan = False
        return non_vegan_recipe



    #inputs: percent we want to reduce unhealthy ingredients (int)
    #outputs: new healthier recipe
    ###TIM DOES THIS
    def make_healthy(self):
        choice = input('Choose one of the following options to make your recipe healthier: (1) Substitute unhealthy'
         'ingredients with healthier ingredients, (2) Reduce amount of secondary unhealthy ingredients, (3)'\
          'Change cooking method. Enter your choice by pressing 1, 2 or 3:  ')

        healthy_recipe = copy.deepcopy(self)
        preparation_steps = list()
        prepared_ingredients = []
        if choice == 3:
            # TO IMPLEMENT
            pass
        elif choice == 2:
            # choice 2: Reduce Quantity of Some Ingredients
            reduced_ingredients = {}
            for i in range(len(healthy_recipe.ingredients)):
                ingredient = healthy_recipe.ingredients[i].name.lower()
                for j in range(len(reduction_substitutes)):
                    if ingredient == reduction_substitutes[j].name:
                        if reduction_substitutes[j].additional_ingredient is None: #salt reduce by half
                            reduced_ingredients[ingredient] = [reduction_substitutes[j].substitute, False, reduction_substitutes[j].ratio]
                            healthy_recipe.ingredients[i].quantity = healthy_recipe.ingredients[i].quantity * reduction_substitutes[j].ratio
                        else:
                            healthy_recipe.ingredients[i].quantity = convert_quantity(healthy_recipe.ingredients[i].quantity) * reduction_substitutes[j].ratio
                            healthy_recipe.ingredients.append(Ingredient(reduction_substitutes[j].additional_ingredient, healthy_recipe.ingredients[i].quantity,
                                                                         healthy_recipe.ingredients[i].measurement, healthy_recipe.ingredients[i].descriptors))
                            reduced_ingredients[ingredient] = [reduction_substitutes[j].substitute, True, reduction_substitutes[j].ratio, reduction_substitutes[j].additional_ingredient]
                        break
            if len(reduced_ingredients) == 0:
                print 'There are no secondary ingredients to reduce, making recipe healthier by substituting' \
                      ' unhealthy ingredients \n \n'
                pass
            else:
                for i in range(len(healthy_recipe.steps)):
                    step = healthy_recipe.steps[i].original_document
                    for reduced in reduced_ingredients.keys():
                        if reduced_ingredients[reduced][1]:
                            step = step.replace(reduced, reduced_ingredients[reduced][0])
                            if reduced not in prepared_ingredients:
                                preparation_steps.append(Step(
                                    original_document='Mix the ' + reduced + ' with the ' + reduced_ingredients[reduced][
                                        3] + ' in a bowl.', tools=['bowl']))
                                prepared_ingredients.append(reduced)
                        else:
                            step = fix_step(step, reduced, reduced_ingredients[reduced[2]])
                    healthy_recipe.steps[i].original_document = step
                healthy_recipe.steps = preparation_steps + healthy_recipe.steps
                print self
                return healthy_recipe
        #choice 1 and DEFAULT: Substitute Ingredients
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

