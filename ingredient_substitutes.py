# define vegan substitutes for non-vegan ingredients
# reference source is http://www.vegkitchen.com/tips/vegan-substitutions/

vegan_substitutes = {}
vegan_substitutes['milk'] = 'soy milk'
vegan_substitutes['milk'] = 'soy milk'
vegan_substitutes['cheese'] = 'vegan cheese'
vegan_substitutes['eggs'] = 'tofu scramble'
vegan_substitutes['beef'] = 'vegetable bouillon cubes'
vegan_substitutes['chicken'] = 'vegetable bouillon cubes'
vegan_substitutes['butter'] = 'vegan butter'
vegan_substitutes['yogurt'] = 'vegan yogurt'
vegan_substitutes['sour cream'] = 'vegan sour cream'
vegan_substitutes['mayonnaise'] = 'mayonnaise'
vegan_substitutes['gelatin'] = 'agar flakes'
vegan_substitutes['honey'] = 'sweetener'
vegan_substitutes['sugar'] = 'beet sugar'
vegan_substitutes['chocolate'] = 'non-dairy vegan chocolate bar'
vegan_substitutes['ice cream'] = 'non-dairy vegan ice-cream'
vegan_substitutes['meat'] = 'beans'


# define healthy substitutes for a range of unhealthy ingredients in recipes
# most if not all substitute on a 1:1 ratio
healthy_protein = ['beans', 'peas', 'eggs', 'fish','chicken', 'tofu']
unhealthy_protein = ['ground beef', 'beef', 'pork', 'lamb']
healthy_fats = ['sesame oil', 'olive oil', 'sunflower oil']
unhealthy_fats = ['butter', 'chicken fat', 'coconut oil', 'canola oil', 'margarine', 'cream', 'palm oil']
healthy_dairy = ['fat free milk', 'low fat milk', 'low fat cheese']
unhealthy_dairy = ['cream cheese', 'sour cream', 'whipped cream', 'whole milk', 'butter', 'cheese']
healthy_sugars = ['brown sugar', 'cane sugar', 'fruit juice concentrates', 'molasses', 'honey', 'maple syrup']
unhealthy_sugars = ['white sugar', 'chocolate syrup', 'corn syrup', 'aspartame', 'sugar']
healthy_salts = ['low sodium soy sauce', 'sea salt']
unhealthy_salts = ['soy sauce', 'table salt','salt']
healthy_grains = ['brown rice', 'wild rice', 'whole wheat pasta', 'buckwheat', 'millet']
unhealthy_grains = ['white rice', 'pasta', 'macaroni', 'noodles', 'spaghetti']

healthy_substitutes = [healthy_protein, healthy_fats, healthy_dairy, healthy_sugars, healthy_salts, healthy_grains]
unhealthy_ingredients = [unhealthy_protein, unhealthy_fats, unhealthy_dairy, unhealthy_sugars, unhealthy_salts,
                         unhealthy_grains]

reduction_substitutes = []
class Ingredient_Substitute:
	def __init__(self, name, ratio, supplement, supplement_ratio):
		self.name = name
		self.ratio = ratio
		self.supplement = supplement
		self.supplement_ratio = supplement_ratio

def initialize_reduction_substitutes():
	global reduction_substitutes
	reduction_substitutes.append(Ingredient_Substitute('fat', .5, 'unsweetened apple sauce', .5))
	reduction_substitutes.append(Ingredient_Substitute('salt', .5))
	reduction_substitutes.append(Ingredient_Substitute('sugar', .5, 'almond extract'))
	reduction_substitutes.append(Ingredient_Substitute('butter', .5, 'unsweetened apple sauce', .5))

initialize_reduction_substitutes()