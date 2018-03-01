from ingredient import Ingredient
from recipe import Recipe
from scraper import scrapeRecipe

measurement_strings = ["cup","pinch","can","tablespoon","teaspoon","clove","rack","pound","bottle","pinch"]

def main():
    ingredients = []
    
    r_ingredients, r_steps = scrapeRecipe()
    for ri in r_ingredients:
        descriptors = []
        split_words = ri.split(' ')
        if split_words[0][0].isnumeric():
            quantity = split_words[0]
            old = 1
        else:
            #this handles when there is no number at the start of an ungredient
            quantity = 1
            old = 0
            
        counter = old
        halt = False
        measurement = None
        while counter < len(split_words) and not halt:
            for s in measurement_strings:
                if s in split_words[counter].lower():
                    measurement = ' '.join(split_words[1:counter+1])
                    halt = True
            counter += 1
        if measurement != None and measurement[-1] == 's':
            measurement = measurement[:-1]
            
        if halt == False:
            counter = old
            
        name = ' '.join(split_words[counter:])
        preparation = None

        if ',' in name:
            preparation = name.split(',')[1]
            name = name.split(',')[0]
        
        ingredients.append(Ingredient(name, quantity, measurement, [], preparation))
                                      
        print quantity, '|', measurement, '|', name, '|', preparation

main()


