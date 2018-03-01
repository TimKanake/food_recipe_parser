class Ingredient:
    def __init__(self, name = "", quantity = "", measurement = "", descriptors = [], preparation = ""):
        self.name = name #string
        self.quantity = quantity #string
        self.measurement = measurement #string
        self.descriptors = descriptors #list of strings
        self.preparation = preparation #string

    def get_ingredient_string(self):
        return  self.quantity + " " + self.measurement + ", " + self.name + ", " + self.preparation

    def __str__(self):
    	return """{0} {1} {2} {3}""".format(self.quantity, self.measurement, self.name, self.preparation)