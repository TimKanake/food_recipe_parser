from bs4 import BeautifulSoup
import urllib2

#returns raw ingredients, steps, and recipe name from URL
def scrapeRecipe(url):
    document = urllib2.urlopen(url).read()
    soup = BeautifulSoup(document, "html.parser")
    links = soup.findAll('span')
    raw_ingredients = []
    raw_directions = []
    raw_title = ''
    for link in links:
        if link.get('itemprop') != None:
            if "ingredients" in link['itemprop']:
                raw_ingredients.append(link.string)
        if link.get('class') != None:
            if "recipe-directions__list--item" in link['class']:
                if link.string != None:
                    raw_directions.append(link.string)
    headers = soup.findAll('h1')
    raw_title = ''
    for h in headers:
        if h.get('class') != None:
            if "recipe-summary__h1" in h['class']:
                raw_title = h.string
    return raw_ingredients, raw_directions, raw_title

#returns a pretty good list of tools that Andre and I compiled from websites and hardcoding
def scrapeTools():
    url = "https://en.wikipedia.org/wiki/List_of_food_preparation_utensils"
    document = urllib2.urlopen(url).read()
    soup = BeautifulSoup(document, "html.parser")
    headers = soup.findAll('th')
    strings = ['knife','food processor','saute pan','stock pot','brush','roasting rack','roasting pan','loaf pan','pot','pan','slow cooker','fork','spoon','skillet','whisk', "oven"]
    for h in headers:
        if h.get('scope') == "row" and (h.get('class') == None or "navbox-group" not in h.get('class')):
            s = h.string
            if s == None:
                try:
                    s = h.a.string
                except:
                    pass
            if s != None:
                strings.append(s.lower())

    url2 = "https://www.mealime.com/kitchen-essentials-list"
    document = urllib2.urlopen(url2).read()
    soup = BeautifulSoup(document, "html.parser")
    headers = soup.findAll('h3')

    for h in headers:
        strings.append(h.string.lower())

    return strings

#returns a pretty good list of cooking methods, hardcoded completely for now
def scrapeMethods():
    methods = ["bake","fry","broil","boil","saute","grill","roast","steam","simmer","poach","pressure cook","barbecue","smoke","sear","braise","char","cure","glaze","stir fry", "season", "heat", "stir", "preheat", "slow cook"]
    return methods

#returns a pretty good list of cooking measurements, hardcoded completely for now
def scrapeMeasurements():
    measurements = ["cup","can","tablespoon","teaspoon","clove","rack","pound","bottle","pinch","ounce","oz.","dash","pint","quart","gallon","kilogram","gram","milliliter","liter","stick","peck","jigger","square"]
    return measurements

def scrapeTimeMeasuements():
    return ["hour", "minute", "second", "nanosecond"]

