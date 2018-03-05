# define vegan substitutes for non-vegan ingredients
# reference source is http://www.vegkitchen.com/tips/vegan-substitutions/

vegan_substitutes = {}
vegan_substitutes['milk'] = 'soy milk'
vegan_substitutes['cheese'] = 'vegan cheese'
vegan_substitutes['eggs'] = 'tofu scramble'
vegan_substitutes['beef'] = 'vegetable bouillon cubes'
vegan_substitutes['chicken'] = 'vegetable bouillon cubes'
vegan_substitutes['butter'] = 'vegan butter'
vegan_substitutes['yogurt'] = 'vegan yogurt'
vegan_substitutes['sour cream'] = 'vegan sour cream'
vegan_substitutes['mayonnaise'] = 'vegan mayonnaise'
vegan_substitutes['gelatin'] = 'agar flakes'
vegan_substitutes['honey'] = 'sweetener'
vegan_substitutes['sugar'] = 'beet sugar'
vegan_substitutes['chocolate'] = 'non-dairy vegan chocolate bar'
vegan_substitutes['ice cream'] = 'non-dairy vegan ice-cream'
vegan_substitutes['meat'] = 'beans'

# define vegan to meat substitutes

non_vegan_substitutes = {}
non_vegan_substitutes['soy milk'] = 'milk'
non_vegan_substitutes['vegan cheese'] = 'cheese'
non_vegan_substitutes['tofu scramble'] = 'eggs'
non_vegan_substitutes['tofu'] = 'chicken'
non_vegan_substitutes['vegetable bullion cubes'] = 'beef'
non_vegan_substitutes['vegan butter'] = 'butter'
non_vegan_substitutes['vegan yogurt'] = 'yogurt'
non_vegan_substitutes['vegan sour cream'] = 'sour cream'
non_vegan_substitutes['vegan mayonnaise'] = 'mayonnaise'
non_vegan_substitutes['agar flakes'] = 'gelatin'
non_vegan_substitutes['sweetener'] = 'honey'
non_vegan_substitutes['beet sugar'] = 'sugar'
non_vegan_substitutes['non-dairy vegan chocolate bar'] = 'chocolate'
non_vegan_substitutes['non-dairy vegan ice-cream'] = 'ice cream'
non_vegan_substitutes['beans'] = 'meat'


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
	def __init__(self, name, substitute, additional_ingredient = None, ratio = None):
		self.name = name
		self.substitute = substitute
		self.additional_ingredient = additional_ingredient
		self.ratio = ratio

def initialize_reduction_substitutes():
	global reduction_substitutes
	reduction_substitutes.append(Ingredient_Substitute('fat', 'mixed fat and unsweetened apple sauce', 'unsweetened apple sauce', .5))
	reduction_substitutes.append(Ingredient_Substitute('salt', 'salt', None, .5))
	reduction_substitutes.append(Ingredient_Substitute('sugar', 'mixed sugar and almond extract', 'almond extract', .5))
	reduction_substitutes.append(Ingredient_Substitute('butter', 'mixed butter and unsweetened apple sauce', 'unsweetened apple sauce', .5))
	reduction_substitutes.append(Ingredient_Substitute('cheese', 'cheese', None, .5))

def fix_step(step, ingredient, ratio):
	step_words = step.split(' ')
	for i in range(len(step_words)):
		if step_words[i] == ingredient:
			for j in range(i, 0, -1):
				if check_int(step_words[j]):
					step_words[j] = str(int(step_words[j]) * ratio)
				elif check_fraction(step_words[j]):
					fraction = get_fraction(step_words[j]) * ratio
					step_words[j] = str(fraction)

	return " ".join(step_words)

def get_fraction(fraction):
	return float(fraction[0]) / float(fraction[2])

def check_fraction(number):
	if '/' not in number:
		return False
	return True

def check_int(number):
	try:
		int(number)
		return True
	except ValueError:
		return False

def convert_quantity(quantity):
	if check_int(quantity):
		return int(quantity)
	elif check_fraction(quantity):
		return get_fraction(quantity)


initialize_reduction_substitutes()