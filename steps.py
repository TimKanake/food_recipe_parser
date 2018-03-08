from pretty_string import pretty_string

# (optional) Parse the directions into a series of steps that each consist of ingredients, tools, methods, and times

class Step:
    def __init__(self, number=None, ingredients = [], tools = [], methods = [], times = [], original_document=None):
        self.number = number                # int:  step number in list of ordered steps
        self.ingredients = ingredients      # list: ingredient names as strings
        self.tools = tools                  # list: tool names as strings
        self.methods = methods              # list: method names as strings
        self.times = times                  # list: two word strings about time e.g. ['5 minutes', '1 hour']
        self.original_document = original_document # string: original, scraped step/direction

    def __str__(self):
        p_doc = self.pretty_original_doc()
        p_ingredients = []
        for ingredient in self.ingredients:
            p_ingredients.append(ingredient.name)
        p_ingredients = pretty_string(p_ingredients, "ingredients", "horizontal")
        p_tools = pretty_string(self.tools, 'tools', "horizontal")
        p_methods = pretty_string(self.methods, 'methods', "horizontal")
        p_times = pretty_string(self.times, "times", "horizontal")
        dashed_line_str = "-"*79

        return """\n\
        Step {}:\n\t\t{}\n\
        \n\tIngredients:\n\t\t{}\n\
        \n\tTools:\n\t\t{}\n\
        \n\tMethods:\n\t\t{}\n\
        \n\tTime:\n\t\t{}\n\
        {}""".format(self.number, p_doc, p_ingredients, p_tools, p_methods, p_times, dashed_line_str)


    # Take the scraped step string, split by periods, and returns list of strings
    def step_to_sentences(self):
        refined_steps = []
        sentences = self.original_document.split(".")
        if "" in sentences: sentences.remove("")
        for s in sentences:
            s = s.strip()
            refined_steps.append(s)
        return refined_steps

    def pretty_original_doc(self):
        p_doc = ""
        for x in self.step_to_sentences():
            p_doc += x + ".\n\t\t"
        p_doc = p_doc[:-3]

        return p_doc

