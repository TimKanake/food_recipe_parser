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
        toreturn = ''
        toreturn += str(self.quantity)
        if len(self.measurement) > 0:
            toreturn += ' '+self.measurement
        try:
            for descriptor in self.descriptors:
                toreturn += ' '+descriptor
                if ',' not in descriptor:
                    toreturn += ','
        except:
            print self.descriptors
        if len(self.descriptors) > 0:
            toreturn = toreturn[:-1]
        toreturn += ' '+self.name
        if len(self.preparation) > 0:
            toreturn += ' '+self.preparation
        return toreturn
