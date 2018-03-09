# define vegan substitutes for non-vegan ingredients
# reference source is http://www.vegkitchen.com/tips/vegan-substitutions/

vegan_substitutes = {}
vegan_substitutes['chicken broth'] = 'vegetable broth'
vegan_substitutes['beef broth'] = 'vegetable broth'
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
vegan_substitutes['[pork'] = 'tofu'
vegan_substitutes['duck'] = 'tofu'
vegan_substitutes['goat'] = 'tofu'
vegan_substitutes['liver'] = 'tofu'
vegan_substitutes['steak'] = 'tofu'

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
non_vegan_substitutes['beans'] = 'beef'


# define healthy substitutes for a range of unhealthy ingredients in recipes
# most if not all substitute on a 1:1 ratio
healthy_protein = ['beans', 'peas', 'eggs', 'fish','chicken', 'tofu']
unhealthy_protein = ['ground beef', 'beef', 'pork', 'lamb']
healthy_fats = ['sesame oil', 'olive oil', 'sunflower oil']
unhealthy_fats = ['coconut oil', 'chicken fat', 'butter', 'canola oil', 'margarine', 'cream', 'palm oil']
healthy_dairy = ['fat free milk', 'low fat milk', 'low fat cheese']
unhealthy_dairy = ['cream cheese', 'sour cream', 'whipped cream', 'whole milk', 'butter', 'cheese']
healthy_sugars = ['brown sugar', 'cane sugar', 'fruit juice concentrates', 'molasses', 'honey', 'maple syrup']
unhealthy_sugars = ['white sugar', 'chocolate syrup', 'corn syrup', 'aspartame', 'sugar']
healthy_salts = ['low sodium soy sauce', 'sea salt']
unhealthy_salts = ['soy sauce', 'table salt','salt']
healthy_grains = ['brown rice', 'wild rice', 'whole wheat pasta', 'buckwheat', 'millet']
unhealthy_grains = ['white rice', 'pasta', 'macaroni', 'noodles', 'spaghetti']

healthy_substitutes = [healthy_protein, healthy_fats, healthy_dairy, healthy_sugars, healthy_salts, healthy_grains]
unhealthy_substitutes = [unhealthy_protein, unhealthy_fats, unhealthy_dairy, unhealthy_sugars, unhealthy_salts,
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
	reduction_substitutes.append(Ingredient_Substitute('sugar', 'mixed sugar and almond extract', 'almond extract', .5))
	reduction_substitutes.append(Ingredient_Substitute('salt', 'salt', None, .5))
	reduction_substitutes.append(Ingredient_Substitute('butter', 'mixed butter and unsweetened apple sauce', 'unsweetened apple sauce', .5))
	reduction_substitutes.append(Ingredient_Substitute('cheese', 'cheese', None, .5))
	reduction_substitutes.append(Ingredient_Substitute('olive oil', 'canola oil', None, 1))

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

def fix_step_2(step, old_ingredient, new_ingredient):
	if old_ingredient in step:
		return step.replace(old_ingredient, new_ingredient)
	else:
		old_ingredient_substrings = get_all_substrings(old_ingredient)
		for i in range(len(old_ingredient_substrings)):
			if old_ingredient_substrings[i] in step:
				return step.replace(old_ingredient_substrings[i], new_ingredient)
	return step
		# create window and get strings

def get_all_substrings(input_string):
	input_string = input_string.split()
	length = len(input_string)
	substrings_ar = [input_string[i:j + 1] for i in xrange(length) for j in xrange(i, length)]
	for i in range(len(substrings_ar)):
		substrings_ar[i] = " ".join(substrings_ar[i])
	substrings_ar.sort(lambda x, y: cmp(len(x), len(y)), reverse=True)
	return substrings_ar
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