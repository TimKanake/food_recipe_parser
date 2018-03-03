from ingredient import Ingredient
from recipe import Recipe
from scraper import scrapeRecipe, scrapeTools, scrapeMethods, scrapeMeasurements
import operator

#takes list of raw ingredients and returns list of Ingredient objects
def parse_ingredients(r_ingredients):
    ingredients = []
    measurements = scrapeMeasurements()
    for ri in r_ingredients:
        descriptors = []
        split_words = ri.split(' ')
        #quantity
        if split_words[0][0].isnumeric():
            quantity = split_words[0]
            old = 1
        else:
            quantity = 1
            old = 0

        #measurement
        counter = old
        halt = False
        measurement = ""
        while counter < len(split_words) and not halt:
            for s in measurements:
                if s in split_words[counter].lower():
                    measurement = ' '.join(split_words[1:counter + 1])
                    halt = True
            counter += 1
        if measurement != "" and measurement[-1] == 's':
            measurement = measurement[:-1]

        #name
        if halt == False:
            counter = old
        name = ' '.join(split_words[counter:])

        #preparation
        preparation = ""
        if ',' in name:
            preparation = name.split(',')[1]
            name = name.split(',')[0]
        ingredients.append(Ingredient(name, quantity, measurement, [], preparation))
    return ingredients

###DAN AND ANDRE DO THIS
def parse_tools(r_steps):
    tools = scrapeTools()
    used_tools = {}
    exc = {}
    exc['knife'] = ['carve','cut','slice','chop','dice','mince']
    exc['thermometer'] = ['temperature','degrees']
    exc['spoon'] = ['stir']
##    exc['tongs'] = ['turn']
    for step in r_steps:
        #check for tools
        for tool in tools:
            if tool in step.lower():
                if tool in used_tools:
                    used_tools[tool] += 1
                else:
                    used_tools[tool] = 1
        #check for words that are indicative of certain tools
        for t in exc:
            for word in exc[t]:
                if word in step.lower():
                    if tool in used_tools:
                        used_tools[t] += 1
                    else:
                        used_tools[t] = 1

    sorted_tools = sorted(used_tools.items(), key = operator.itemgetter(1))
    sorted_tools.reverse()
    return sorted_tools

    return used_tools

###DAN AND ANDRE DO THIS
def parse_method(r_steps):
    methods = scrapeMethods()
    method_frequency = {}
    for step in r_steps:
        for method in methods:
            if method in step.lower():
                if method in method_frequency:
                    method_frequency[method] += 1
                else:
                    method_frequency[method] = 1

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

#given a url to an allrecipes page, will return Recipe object
def make_recipe(url):
    r_ingredients, r_steps, r_name = scrapeRecipe(url)

    ingredients = parse_ingredients(r_ingredients)
    refined_steps = parse_steps(r_steps)
    tools = parse_tools(r_steps)
    method = parse_method(r_steps)

    r = Recipe(r_name, ingredients, refined_steps, tools, method)

    return r

#example run on 4 recipes
def test1():
    print make_recipe("https://www.allrecipes.com/recipe/43655/perfect-turkey/")
    print make_recipe("https://www.allrecipes.com/recipe/21174/bbq-pork-for-sandwiches/")
    print make_recipe("https://www.allrecipes.com/recipe/260463/italian-chicken-cacciatore/")
    print make_recipe("https://www.allrecipes.com/recipe/25333/vegan-black-bean-soup/")


