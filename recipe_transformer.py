from ingredient import Ingredient
from recipe import Recipe
from scraper import scrapeRecipe, scrapeTools, scrapeMethods, scrapeMeasurements, scrapeTimeMeasuements
from steps import Step
import operator
from collections import OrderedDict


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


# (optional) Parse the directions into a series of steps that each consist of ingredients, tools, methods, and times
# By A) Checking in which steps are the ingredients, tools, methods in the recipe used.
# and B) Checking for numbers and time-related words like "minutes" "hours" "seconds"
def parse_steps2(steps, ingredients, tools, methods):
    print "parse_steps2\n"
    count = 0
    list_out = [] # List to hold the Step objects created from each step

    # For each step...
    for step in steps:
        step = step.lower()
        # Check which ingredients, tools, methods in the recipe are used.
        steps_obj = Step(number=count, ingredients = [], tools = [], methods = [], times = [], original_document=step)
        count +=1
        for i in ingredients:
            if i.name in step:
                steps_obj.ingredients.append(i.name)
            else:
                for x in i.name.split(" "):
                    if x in step:
                        steps_obj.ingredients.append(x)
        steps_obj.ingredients = list(OrderedDict.fromkeys(steps_obj.ingredients))
        for t in tools:
            if t[0] in step:
                steps_obj.tools.append(t)
        steps_obj.tools = list(OrderedDict.fromkeys(steps_obj.tools))
        for m in methods:
            if m[0] in step:
                steps_obj.methods.append(m)
        steps_obj.methods = list(OrderedDict.fromkeys(steps_obj.methods))

        # Then parse the step for numbers, time-related words like "5 minutes" TO DO
        s_steps = step.split(" ")
        time_words = scrapeTimeMeasuements()
        for word in time_words:
            for x in range(len(s_steps)):
                if word in s_steps[x]:
                    print s_steps[x-1:x+1]
                    if s_steps[x-1].isdigit() or s_steps[x-1] in "an":
                        steps_obj.times = s_steps[x-1] + " " + s_steps[x]


        list_out.append(steps_obj)
    return list_out

#given a url to an allrecipes page, will return Recipe object
def make_recipe(url):
    r_ingredients, r_steps, r_name = scrapeRecipe(url)

    ingredients = parse_ingredients(r_ingredients)
    refined_steps = parse_steps(r_steps)
    tools = parse_tools(r_steps)
    method = parse_method(r_steps)

    r = Recipe(r_name, ingredients, refined_steps, tools, method)

    return r

#### Tests ######

# Example run on 4 recipes
def test1():
    print make_recipe("https://www.allrecipes.com/recipe/43655/perfect-turkey/")
    print make_recipe("https://www.allrecipes.com/recipe/21174/bbq-pork-for-sandwiches/")
    print make_recipe("https://www.allrecipes.com/recipe/260463/italian-chicken-cacciatore/")
    print make_recipe("https://www.allrecipes.com/recipe/25333/vegan-black-bean-soup/")

# Test out parsing steps into what ingredients, tools, methods, and time is needed
def test2():
    r = make_recipe("https://www.allrecipes.com/recipe/25333/vegan-black-bean-soup/")
    print r
    list_of_steps = parse_steps2(r.steps, r.ingredients, r.tools, r.method)
    print "List of Steps:\n"
    for step in list_of_steps:
        print step
