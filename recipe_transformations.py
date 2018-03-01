# define vegan substitutes for non-vegan ingredients
# reference source is http://www.vegkitchen.com/tips/vegan-substitutions/
ingredient_substitutes = {}
ingredient_substitutes['milk'] = 'soy milk'
ingredient_substitutes['milk'] = 'soy milk'
ingredient_substitutes['cheese'] = 'vegan cheese'
ingredient_substitutes['eggs'] = 'tofu scramble'
ingredient_substitutes['beef'] = 'vegetable bouillon cubes'
ingredient_substitutes['chicken'] = 'vegetable bouillon cubes'
ingredient_substitutes['butter'] = 'vegan butter'
ingredient_substitutes['yogurt'] = 'vegan yogurt'
ingredient_substitutes['sour cream'] = 'vegan sour cream'
ingredient_substitutes['mayonnaise'] = 'mayonnaise'
ingredient_substitutes['gelatin'] = 'agar flakes'
ingredient_substitutes['honey'] = 'sweetener'
ingredient_substitutes['sugar'] = 'beet sugar'
ingredient_substitutes['chocolate'] = 'non-dairy vegan chocolate bar'
ingredient_substitutes['ice cream'] = 'non-dairy vegan ice-cream'
ingredient_substitutes['meat'] = 'beans'



def substitute_ingredient(ingredient):
	if ingredient.lower() in ingredient_substitutes.keys():
		return ingredient_substitutes[ingredient.lower()]



