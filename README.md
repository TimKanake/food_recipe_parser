# food_recipe_parser
eecs_337_final_project

Recipe Transformation Project EECS-337 Winter 2018:
------------------------------------------
Jimmy Song, Timothy Kanake, Daniel Thomas, Andre Ehrlich


Requirements:
------------------------------------------
Python 2.7 and these packages:
operator
sys
urllib2
bs4
csv
pickle
collections
math
random
copy


Project:
--------------------------------------
Our project works out of main.py. Within this file there is a function called main which takes these arguments:
main(
	string url,
	boolean make_vegan,
	boolean make_non_vegan,
	boolean make_healthy,
	boolean make_unhealthy,
	boolean change_style,
	string style,
	boolean DIY_to_easy,
	boolean change_cooking_method,
	tuple<string> method)

When these parameters are set to True, the function will transform the recipe at the given AllRecipes.com URL. 

For the transformation change_style, the string parameter style is required. Accepted style examples include: Cajun & Creole, Caribbean, Chinese, Indian, Italian, Mediterranean, Mexican, Middle Eastern, North African, Spanish, Thai, Asian.

For the transformation change_method, the string tuple method is required. This should be of the form (old_method,new_method). An example is ("bake","fry").