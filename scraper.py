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

def addFoods():
    filepath = "foods.csv"
    foods = []
    reader = csv.reader(open(filepath))
    for row in reader:
        foods.append(row[0])
    url = 'http://eatingatoz.com/food-list/'
    document = getPage(url)
    soup = BeautifulSoup(document, "html.parser")
    potFoods = soup.findAll('li')
    for f in potFoods:
        if f.get('class') == None and f.string is not None:
            pfood = f.string.split('(')[0].lower()
            pfood = pfood.strip()
            if "guancamole" in pfood:
                pfood = 'guacamole'
            if len(pfood) > 2:
                if ' / ' in pfood:
                    s = pfood.split(' / ')
                    if s[0] not in foods:
                        foods.append(s[0])
                    if s[1] not in foods:
                        foods.append(s[1])
                elif pfood not in foods:
                    foods.append(pfood)
    for food in ["baking soda","tortilla","bell pepper"]:
        if food not in foods:
            foods.append(food)
    if 'mince' in foods:
        foods.remove("mince")
    writer = csv.writer(open(filepath,'wb'))
    for row in foods:
        try:
            writer.writerow([row])
        except:
            writer.writerow(['jalapeno'])

def getSpices():
    spices = {}
    spices['Cajun & Creole'] = 'Blackened Seasoning, Cajun Seasoning, Cajun Turkey Rub, Creole Seasoning and Cajun Rub (Hot), Allspice, basil, bay leaves , black pepper , caraway seeds , cardamom seed powder , cayenne , celery seed , chives , chile peppers , Korintje cinnamon , Vietnamese cinnamon , cloves , cumin , dill seed , dill weed , garlic , gumbo file , lemon , mace , marjoram , nutmeg , onion , oregano (Mediterranean) , paprika , parsley , saffron , savory , tarragon , thyme , white pepper, yellow mustard'
    spices['Caribbean'] = 'Adobo Lime Rub , Caribbean Spice , Caribbean Turkey Rub , Colombo Powder (Caribbean curry powder), Jamaican Jerk and Mojo Seasoning, Allspice , achiote seeds (annatto seeds) , black pepper , chile peppers , Korintje cinnamon , Vietnamese cinnamon , cloves , garlic , ginger , lime , mace , nutmeg , onion , thyme'
    spices['Chinese'] = 'Chinese Five Spice, Korintje Cinnamon , Vietnamese cinnamon , cloves , fennel seed , ginger , hot mustard , lemongrass , Sichuan peppercorns , star anise , Tien Tsin chiles , turmeric , white pepper'
    spices['Indian'] = 'Garam Masala , Panch Phoron , Madras Curry , Maharajah Curry , Vindaloo Curry, Tikka Masala, Anise seed , ajwain , asafoetida , bay leaf , black cardamom , black cumin, black mustard seed , black pepper , black salt, brown mustard seed , chile peppers , cinnamon , Vietnamese cinnamon , cloves , coriander , cubeb berries , cumin , dried mango , fennel seed , fenugreek leaves , fenugreek seeds , garlic , ginger , green cardamom , lemon , lime , long pepper , mace , mint , nigella , nutmeg , onion , poppy seeds , saffron , sesame seed , star anise , turmeric, white pepper'
    spices['Italian'] = 'Italian Seasoning , Pizza Seasoning , Spaghetti Seasoning, Tuscany Bread Dipping, Basil , garlic , onion , oregano (Mediterranean) , marjoram, parsley'
    spices['Mediterranean'] = 'Citrus Seasoning , Greek Seasoning , Herbs de Provence , Mediterranean Dry Rub, Basil , bay leaves , black caraway , black pepper , cardamom seed powder , chervil , chile peppers , chives , cilantro , cinnamon , Vietnamese cinnamon , cloves , coriander , cumin , fennel seed , fenugreek seeds , garlic , ginger , juniper , mace , marjoram , mint , nutmeg , onion , oregano (Mediterranean) , paprika , parsley , rosemary , saffron , sage , savory , tarragon , thyme , turmeric, white pepper'
    spices['Mexican'] = 'Adobo Seasoning , Habanero Mango , Manzanillo Seasoning , Mole Seasoning, Taco Seasoning , Yucatan Recado Rojo ,Allspice , achiote seeds (annatto seeds) , basil , Mexican cinnamon , cayenne , chile peppers , cilantro , coriander , cumin , epazote , mint , nutmeg , oregano (Mexican) , sage , thyme'
    spices['Middle Eastern'] = "Baharat , Lebanese 7 Spice , Shawarma , Za'atar , Aleppo pepper , anise seed , caraway , cardamom , cumin , maras pepper , nutmeg , sumac , turmeric"
    spices['North African'] = 'Baharat , Berbere , Harissa , Moroccan Chicken Spice Rub , Moroccan Vegetable Rub , Piri Piri Seasoning , Ras el Hanout , Tunisian Five Spice, Birds eye chiles , cilantro , cinnamon , Vietnamese cinnamon , cubeb berries , cumin , garlic , ginger , grains of paradise , long pepper , mint , onion , saffron'
    spices['Spanish'] = 'Paella Seasoning , Basil , bay leaf , cayenne , cinnamon , Vietnamese cinnamon , cloves , garlic , mint , nutmeg , oregano (Mediterranean) , paprika (Smoked Sweet) , parsley , rosemary , saffron , sage , tarragon , thyme , vanilla'
    spices['Thai'] = 'Spicy Thai Seasoning , Thai Curry Seasoning, Basil , black pepper , cardamom , chile peppers , cilantro , cinnamon , Vietnamese cinnamon , cloves , cumin , garlic , ginger , lemongrass , lime , mace , mint, nutmeg , shallots , turmeric, white pepper'
    for key in spices:
        s = spices[key].split(',')
        spices[key] = []
        for a in s:
            spices[key].append(a.split('(')[0].strip().lower())
    return spices
    
def loadFoods():
    foods = []
    reader = csv.reader(open("foods.csv"))
    for row in reader:
        foods.append(row[0])
    return foods

def addSpices():
    filepath = "foods.csv"
    foods = []
    reader = csv.reader(open(filepath))
    for row in reader:
        if row[0] not in foods:
            foods.append(row[0])
    spices = getSpices()
    for style in spices:
        for spice in spices[style]:
            if spice not in foods:
                foods.append(spice)
    writer = csv.writer(open(filepath,'wb'))
    for row in foods:
        try:
            writer.writerow([row])
        except:
            print row
        
        
    
    

