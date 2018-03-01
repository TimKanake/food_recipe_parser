from bs4 import BeautifulSoup
import urllib2

def scrapeIngredients(url='https://www.allrecipes.com/recipe/25333/vegan-black-bean-soup/'):
    document = urllib2.urlopen(url).read()
    soup = BeautifulSoup(document, "html.parser")
    links = soup.findAll('span')
    raw_ingredients = []
    for link in links:
        if link.get('itemprop') != None:
            if "ingredients" in link['itemprop']:
                raw_ingredients.append(link.string)
    return raw_ingredients
