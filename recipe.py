class Recipe:
    def __init__(self, name = None, ingredients = [], steps = [], tools = [], nutrition = None):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        self.tools = tools
        self.nutrition = nutrition

    def make_vegetarion(self):
        pass

    def make_healthy(self):
        pass

    #Inputs:
    #style is the type of style we want to change the recipe to
    def change_style(self, style):
        pass

    def DIY_to_easy(self):
        pass

    #Inputs:
    #method is the method we want to change the cooking to.
    def change_cooking_method(self, method):
        pass





