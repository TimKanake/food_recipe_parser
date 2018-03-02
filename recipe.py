import copy
from ingredient import Ingredient

# define vegan substitutes for non-vegan ingredients
# reference source is http://www.vegkitchen.com/tips/vegan-substitutions/
vegan_substitutes = {}
vegan_substitutes['milk'] = 'soy milk'
vegan_substitutes['milk'] = 'soy milk'
vegan_substitutes['cheese'] = 'vegan cheese'
vegan_substitutes['eggs'] = 'tofu scramble'
vegan_substitutes['beef'] = 'vegetable bouillon cubes'
vegan_substitutes['chicken'] = 'vegetable bouillon cubes'
vegan_substitutes['butter'] = 'vegan butter'
vegan_substitutes['yogurt'] = 'vegan yogurt'
vegan_substitutes['sour cream'] = 'vegan sour cream'
vegan_substitutes['mayonnaise'] = 'mayonnaise'
vegan_substitutes['gelatin'] = 'agar flakes'
vegan_substitutes['honey'] = 'sweetener'
vegan_substitutes['sugar'] = 'beet sugar'
vegan_substitutes['chocolate'] = 'non-dairy vegan chocolate bar'
vegan_substitutes['ice cream'] = 'non-dairy vegan ice-cream'
vegan_substitutes['meat'] = 'beans'

healthy_substiutes = {}

unhealthy_ingredients = []
unhealthy_ingredients.append("butter")
unhealthy_ingredients.append("cheese")
unhealthy_ingredients.append("sugar")
unhealthy_ingredients.append("salt")
unhealthy_ingredients.append("shorteing")
unhealthy_ingredients.append("oil")

unnecessary_ingredients = {}

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

        if len(self.method) > 0:
            p_method = self.method[0][0]
        if len(self.method) > 1:
            p_method += ', ' + self.method[1][0]

        if len(self.tools) > 0:
            p_tools = self.tools[0][0]
            if len(self.tools) > 1:
                for tool in self.tools[1:]:
                    if tool[0] not in p_tools:
                        p_tools += ', ' + tool[0]

        return """\n\nRecipe Name: {0!s}\nIngredients: {1!s}\nSteps: {2!s}\nTools: {3!s}\nMethod: {4!s}\nNutrition {5!s}""".format(self.name, ingredients_ppstring, steps_ppstring, p_tools, p_method, self.nutrition)

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
    def make_healthy(self, percent_reduction = 0.5):
        healthy_recipe = copy.deepcopy(self)

        for i in range(len(self.ingredients)):
            ingredient = self.ingredients[i].name.lower()
            if ingredient in unhealthy_ingredients:
                self.ingredients[i].amount = float(self.ingredients.amount) * percent_reduction

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



