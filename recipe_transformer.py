from ingredient import Ingredient
from recipe import Recipe
from scraper import scrapeRecipe, scrapeTools, scrapeMethods
import operator

measurement_strings = ["cup", "pinch", "can", "tablespoon", "teaspoon", "clove", "rack", "pound", "bottle", "pinch"]

def parse_ingredients(r_ingredients):
    ingredients = []
    for ri in r_ingredients:
        descriptors = []
        split_words = ri.split(' ')
        if split_words[0][0].isnumeric():
            quantity = split_words[0]
            old = 1
        else:
            # this handles when there is no number at the start of an ungredient
            quantity = 1
            old = 0

        counter = old
        halt = False
        measurement = ""
        while counter < len(split_words) and not halt:
            for s in measurement_strings:
                if s in split_words[counter].lower():
                    measurement = ' '.join(split_words[1:counter + 1])
                    halt = True
            counter += 1
        if measurement != "" and measurement[-1] == 's':
            measurement = measurement[:-1]

        if halt == False:
            counter = old

        name = ' '.join(split_words[counter:])
        preparation = ""

        if ',' in name:
            preparation = name.split(',')[1]
            name = name.split(',')[0]

        ingredients.append(Ingredient(name, quantity, measurement, [], preparation))

    return ingredients

###DAN AND ANDRE DO THIS
def parse_tools(r_steps):
    tools = scrapeTools()
    used_tools = []
    for tool in tools:
        for step in r_steps:
            if tool in step:
                used_tools.append(tool)
                
    return used_tools

###DAN AND ANDRE DO THIS
def parse_method(r_steps):
    methods = scrapeMethods()
    method_frequency = {}
    maxx = -1
    maxmethod = ''
    for method in methods:
        for step in r_steps:
            if method in step:
                if method in method_frequency:
                    method_frequency[method] += 1
                else:
                    method_frequency[method] = 1
                if method_frequency[method] > maxx:
                    maxx = method_frequency[method]
                    maxmethod = method
                    
    sorted_methods = sorted(method_frequency.items(), key = operator.itemgetter(1))
    sorted_methods.reverse()
    return sorted_methods

# Take the scraped steps and split by periods
def parse_steps(r_steps):
    refined_steps = []
    for x in r_steps:
        x = x.split(".")
        if "" in x: x.remove("")
        for step in x:
            s = step
            if s[0] == ' ':
                s = s[1:]
            refined_steps.append(s)
    return refined_steps

def make_recipe(url="https://www.allrecipes.com/recipe/25333/vegan-black-bean-soup/"):
    r_ingredients, r_steps, r_name = scrapeRecipe(url)

    ingredients = parse_ingredients(r_ingredients)

    refined_steps = parse_steps(r_steps)

    tools = parse_tools(r_steps)

    method = parse_method(r_steps)

    #nothing for method right now
    r = Recipe(r_name, ingredients, refined_steps, tools, method)

    return r

print make_recipe()



