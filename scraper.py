from bs4 import BeautifulSoup
import urllib2

def scrapeRecipe(url='https://www.allrecipes.com/recipe/25333/vegan-black-bean-soup/'):
    document = urllib2.urlopen(url).read()
    soup = BeautifulSoup(document, "html.parser")
    links = soup.findAll('span')
    raw_ingredients = []
    raw_directions = []
    for link in links:
        if link.get('itemprop') != None:
            if "ingredients" in link['itemprop']:
                raw_ingredients.append(link.string)
        if link.get('class') != None:
            if "recipe-directions__list--item" in link['class']:
                raw_directions.append(link.string)
    return raw_ingredients, raw_directions
