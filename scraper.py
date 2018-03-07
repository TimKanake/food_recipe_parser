from bs4 import BeautifulSoup
import urllib2
import csv
import pickle

def getPage(url):
    address = url.replace('/','_').replace(':','_').replace('.','_').replace(',','_')
    try:
        return pickle.load(open("pickledURLs/"+address+".p","rb"))
    except:
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36')]
        page = opener.open(url).read()
        print "Saving ",url
        pickle.dump(page, open("pickledURLs/"+address+".p","wb"))
        return page

#returns raw ingredients, steps, and recipe name from URL
def scrapeRecipe(url):
##    document = urllib2.urlopen(url).read()
    document = getPage(url)
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
##    document = urllib2.urlopen(url).read()
    document = getPage(url)
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
##    document = urllib2.urlopen(url2).read()
    document = getPage(url2)
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

def scrapeDescriptors():
    return ["skinless","boneless","fresh","thin","thick","low-sodium"]

def scrapePreparations():
    return ["peeled","sliced","dried","ground","thinly sliced"]
    
def scrapeFoods():
    filepath = "foods.csv"
    baseurl = "https://www.bbc.co.uk/food/ingredients/by/letter/"
    foods = []
    for i in range(97,123):
        url = baseurl + chr(i)
        print url
##        document = urllib2.urlopen(url).read()
        document = getPage(url)
        soup = BeautifulSoup(document, "html.parser")
        links = soup.findAll('li')
        for link in links:
            if link.get("class") == [u'resource', u'food']:
                food = link.get("id").replace('_',' ')
                foods.append(food)
    writer = csv.writer(open(filepath,'wb'))
    for food in foods:
        writer.writerow([food])

def loadFoods():
    foods = []
    reader = csv.reader(open("foods.csv"))
    for row in reader:
        foods.append(row[0])
    foods += ["baking soda","tortilla","bell pepper"]
    foods.remove("mince")
    return foods
        
        
    
    

