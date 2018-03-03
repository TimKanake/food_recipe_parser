from pretty_string import pretty_string

# (optional) Parse the directions into a series of steps that each consist of ingredients, tools, methods, and times

class Step:
    def __init__(self, number=None, ingredients = [], tools = [], methods = [], times = [], original_document=None):
        self.number = number
        self.ingredients = ingredients
        self.tools = tools
        self.methods = methods
        self.times = times
        self.original_document = original_document

    def __str__(self):
        p_ingredients = pretty_string(self.ingredients, "ingredients", "horizontal")
        p_tools = pretty_string(self.tools, 'tools', "horizontal")
        p_methods = pretty_string(self.methods, 'methods', "horizontal")
        p_times = pretty_string(self.times, "times", "horizontal")
        return """\nStep {}: "{}"\nIngredients: {}\nTools: {}\nMethods: {}\nTime: {}""".format(self.number, self.original_document, p_ingredients, p_tools, p_methods, p_times)