from bs4 import BeautifulSoup
import urllib2

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
                raw_directions.append(link.string)
    headers = soup.findAll('h1')
    raw_title = ''
    for h in headers:
        if h.get('class') != None:
            if "recipe-summary__h1" in h['class']:
                raw_title = h.string
    return raw_ingredients, raw_directions, raw_title
