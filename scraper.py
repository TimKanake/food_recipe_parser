from bs4 import BeautifulSoup
import urllib2
def scrapeIngredients(url):
    if not url:
        url = 'https://www.allrecipes.com/recipe/25333/vegan-black-bean-soup/'
    document = urllib2.urlopen(url).read()
    soup = BeautifulSoup(document, "html.parser")
    links = soup.findAll('span')
    print links
    ingredients = []
    for link in links:
        print link    
        if "recipe-ingred_txt added" in link:
            ingredients.append(link.string)
    return ingredients

def main():

    print scrapeIngredients(False)
    

main()
