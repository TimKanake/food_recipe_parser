from ingredient import Ingredient
from recipe import Recipe
from scraper import scrapeRecipe, scrapeTools, scrapeMethods, scrapeMeasurements, scrapeTimeMeasuements
from steps import Step
import operator
from collections import OrderedDict


#takes list of raw ingredients and returns list of Ingredient objects
def parse_ingredients(r_ingredients):
    remove_words = ["to","taste","more","or", "and"] # maybe try to fork on 'and'
    ingredients = []
    measurements = scrapeMeasurements()
    for ri in r_ingredients:
        descriptors = []
        split_words = ri.split(' ')
        for word in remove_words:
            if word in split_words:
                split_words.remove(word)
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
        last = False
        measurement = ""
        while counter < len(split_words) and not halt:
            thiswordm = False
            for s in measurements:
                if s in split_words[counter].lower():
                    last = True
                    thiswordm = True
            if not thiswordm and last:
                measurement = ' '.join(split_words[old:counter])
                halt = True
            else:
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

# (optional) Parse the directions into a series of steps that each consist of ingredients, tools, methods, and times
# By A) Checking in which steps are the ingredients, tools, methods in the recipe used.
# and B) Checking for numbers and time-related words like "minutes" "hours" "seconds"
def parse_steps2(steps, ingredients, tools, methods):
    count = 0
    list_out = [] # List to hold the Step objects created from each step

    last_method = None
    ambiguous_terms = ["cook"]
    # For each step...
    for step in steps:
        # Initiate a Step object (see steps.py)
        steps_obj = Step(number=count, ingredients = [], tools = [], methods = [], times = [], original_document=step)
        step = step.lower() # edit the step string a little bit
        step = step[:-1]
        count +=1 # the step count to keep track of order

        # Ingredients
        for i in ingredients:
            if i.name in step:
                steps_obj.ingredients.append(i.name)
            else:
                for x in i.name.split(" "):
                    if x in step:
                        steps_obj.ingredients.append(i.name)

        # Remove duplicates from list while preserving order
        steps_obj.ingredients = list(OrderedDict.fromkeys(steps_obj.ingredients))

        # Tools
        for t in tools:
            if t[0] in step:
                steps_obj.tools.append(t)

        # Remove duplicates from list while preserving order
        steps_obj.tools = list(OrderedDict.fromkeys(steps_obj.tools))

        # Methods
        for m in methods:
            if m[0] in step:
                last_method = m
                steps_obj.methods.append(m)

        for x in ambiguous_terms:
            if x in step and last_method is not None:
                steps_obj.methods.append(last_method)

        # Remove duplicates from list while preserving order
        steps_obj.methods = list(OrderedDict.fromkeys(steps_obj.methods))

        # Times
        # Right now this only picks up things like "5 minutes", "an hour", "a minute"
        # but it ideally would get "5 to 10 minutes" or "an hour and a half" or "1 1/2 hours"
        s_steps = step.split(" ")
        time_words = scrapeTimeMeasuements()
        for word in time_words:
            for x in range(len(s_steps)):
                if word in s_steps[x]:
                    if s_steps[x-1].isdigit() or s_steps[x-1] in "an":
                        #if steps_obj.times[-1] in ".,":
                        #   steps_obj.times = steps_obj.times[:-1]
                        steps_obj.times.append(s_steps[x-1] + " " + s_steps[x])

        if steps_obj.times == []:
            steps_obj.times = ""


        list_out.append(steps_obj)
    return list_out

#given a url to an allrecipes page, will return Recipe object
def make_recipe(url):
    r_ingredients, r_steps, r_name = scrapeRecipe(url)

    ingredients = parse_ingredients(r_ingredients)
    tools = parse_tools(r_steps)
    method = parse_method(r_steps)
    step_objs = parse_steps2(r_steps, ingredients, tools, method)
    r = Recipe(r_name, ingredients, step_objs, tools, method)

    return r

#### Tests ######

# Example run on 4 recipes
def test1():
    print make_recipe("https://www.allrecipes.com/recipe/43655/perfect-turkey/")
    print make_recipe("https://www.allrecipes.com/recipe/21174/bbq-pork-for-sandwiches/")
    print make_recipe("https://www.allrecipes.com/recipe/260463/italian-chicken-cacciatore/")
    print make_recipe("https://www.allrecipes.com/recipe/25333/vegan-black-bean-soup/")

# Test out parsing steps into what ingredients, tools, methods, and time is needed
def test2_get_steps(url):
    r = make_recipe(url)
    print "List of Steps:\n"
    for step in r.steps:
        print step

def test3_make_recipes_from_list(urls):
    for x in urls:
        r = make_recipe(x)
        print r

# I tried to pick a good mix of recipes from the browsing section of the site: https://www.allrecipes.com/recipes/
# test3_make_recipes_from_list(["https://www.allrecipes.com/recipe/242314/browned-butter-banana-bread/",
#                                 "https://www.allrecipes.com/recipe/6788/amish-white-bread/",
#                                 "https://www.allrecipes.com/recipe/17644/german-chocolate-cake-iii/",
#                                 "https://www.allrecipes.com/recipe/223406/quick-savory-grilled-peaches/",
#                                 "https://www.allrecipes.com/recipe/148765/real-new-orleans-style-bbq-shrimp/",
#                                 "https://www.allrecipes.com/recipe/17837/four-seasons-enchiladas/",
#                                 "https://www.allrecipes.com/recipe/238261/chef-johns-classic-potato-pancakes/",
#                                 "https://www.allrecipes.com/recipe/14859/baba-ghanoush/",
#                                 "https://www.allrecipes.com/recipe/260837/coconut-milk-hot-chocolate/"])

#test2_get_steps("https://www.allrecipes.com/recipe/21174/bbq-pork-for-sandwiches/")
#print make_recipe("https://www.allrecipes.com/recipe/260463/italian-chicken-cacciatore/")
#test2_get_steps("https://www.allrecipes.com/recipe/260463/italian-chicken-cacciatore/")
#test1()
