from ingredient import Ingredient
from recipe import Recipe
from scraper import scrapeRecipe

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
    tools = []

    return tools

###DAN AND ANDRE DO THIS
def parse_method(r_steps):
    method = ''

    return method

# Take the scraped steps and split by periods
def parse_steps(r_steps):
    refined_steps = []
    for x in r_steps:
        if x is not None:
            x = x.split(". ")
            if "" in x: x.remove("")
            refined_steps += x
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



