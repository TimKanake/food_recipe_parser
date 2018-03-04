# food_recipe_parser
eecs_337_final_project



to do list for parsing/ recipe generation
------------------------------------------
- regex to cleaner match results
- extend web scraping to cover we have hardcoded
- descriptors of food



--------------------------------------
Recipe Transformer Assignment Sheet
--------------------------------------
GIT: Every group is required to maintain a public git repo of their code from the start of the project. When you make a commit, please include the names of every group member who worked together on that part of the code. I will be viewing the commit log to see whether the work distribution of your group appears equal. Your grade will not be affected by having fewer or more commits than another member, but if you have very few or no commits, and/or your teammates express concern over limited contributions, we’ll have at least have a record to provide some context.

A note on plagiarism: GIT repos from this and previous years are accessible, being public. If you are tempted to look at them, be advised that the code in these repos is not necessarily of great quality. You wouldn’t want to copy from a past group who got a poor grade. Also note that we have seen and graded all the code in all these repos rather extensively. If we notice any copying from a past repo, consequences will be severe.

For your second project, you’ll be creating a recipe transformer. Your recipe transformer must complete the following tasks:

1.   (optional) Accept the URL of a recipe from AllRecipes.com, and programmatically fetch the page. If you choose to skip this step, you will be copying and pasting the text or HTML into your program.
2.  Parse it into the recipe data representation your group designs. Your parser should be able to recognize:
	•   Ingredients
		•   Ingredient name
		•   Quantity
		•   Measurement (cup, teaspoon, pinch, etc.)
		•   (optional) Descriptor (e.g. fresh, extra-virgin)
		•   (optional) Preparation (e.g. finely chopped)
	•   Tools – pans, graters, whisks, etc.
	•   Methods
		•   Primary cooking method (e.g. sauté, broil, boil, poach, etc.)
		•	(optional) Other cooking methods used (e.g. chop, grate, stir, shake, mince, crush, squeeze, etc.)
	•	(optional) Steps – parse the directions into a series of steps that each consist of ingredients, tools, methods, and times
3.  Ask the user what kind of transformation they want to do.
		•   To and from vegetarian and/or vegan (REQUIRED)
		•   To and from healthy (REQUIRED)
		•   Style of cuisine (AT LEAST ONE REQUIRED)
	Another Style of cuisine (OPTIONAL)
		•   DIY to easy (OPTIONAL)
		•   Cooking method (from bake to stir fry, for example) (OPTIONAL)
	If you come up with your own transformation idea, feel free to ask if it
	would be an acceptable substitute. We encourage innovation.
4.  Transform the recipe along the requested dimension, using your system’s internal representation for ingredients, cooking methods, etc.
5.  Display the transformed recipe in a human-friendly format.

As with the previous project, your system can run from the command line and/or from within the Python interpretive environment, if that is what you are using. Note that some of the things listed above are designated as optional. A group that does a truly fantastic job on all of the steps listed above, but omits the optional items, will probably be in the running for an B+ to B. Optional items will bolster your grade, although doing all of the optional items and a lousy job on the core items is not recommended.

With your completed project, you will hand in:

•	Table(s), diagram(s), and/or other visual representation(s) of your internal data representation for ingredients, tools, methods, and/or transformation dimensions. Note that this is a representation of the knowledge base that your system will be using to transform from your parse of the recipe to the new transformed recipe. A good design here can make all the difference.
•	The code for your system (via a URL to your public git repository). This should include a readme or comment header that lists the version of the programming language you used, and all dependencies. Any modules that are not part of the standard install of your programming language should be included in this list, along with information on the code repository from which it can be downloaded (e.g. for python, pip or easy_install). If you used code that you instead put in a file in your project’s working directory, then a copy of that file should be provided along with the code you wrote; the readme and/or comments in such files should clearly state that the code was not written by your team.

Please hand in your project by midnight Wednesday, March 14th. Presentations will be scheduled during the final week of classes. (Thursday, Friday March 15-16). If your group would like to make special arrangements to present the week of exams, please let me know ASAP.

Example of output:

{
               "ingredients":    [{
                                         "name":    "salt",
                                         "quantity":    1,
                                         "measurement":    "pinch",
                                         "descriptor":    "table",
                                         "preparation":    "none"
                           },
                           {
                                         "name":    "olive    oil",
                                         "quantity":    0.75,
                                         "measurement":    "teaspoon",
                                         "descriptor":    "extra-virgin",
                                         "preparation":    "none"
                           },
                           {
                                         "name":    "parsley",
                                         "quantity":    1,
                                         "measurement":    "cup",
                                         "descriptor":    "fresh",
                                         "preparation":    "finely   chopped"
                           }
               ],
               "cooking    method":    "primary   cooking    method    here",
               "cooking    tools":    ["knife",   "grater",    "dutch    oven"],
}
