from pretty_string import pretty_string

# (optional) Parse the directions into a series of steps that each consist of ingredients, tools, methods, and times

class Step:
    def __init__(self, number=None, ingredients = [], tools = [], methods = [], times = []):
        self.number = number
        self.ingredients = ingredients
        self.tools = tools
        self.methods = methods
        self.times = times

    def __str__(self):
        pp_ingredients = pretty_string(self.ingredients)
        pp_tools = pretty_string(self.tools, 'tools')
        pp_methods = pretty_string(self.methods, 'methods')
        return """{0} {1} {2} {3} {4}""".format(self.number, pp_ingredients, pp_tools, pp_methods, self.times)

def parse_steps2(steps, ingredients, tools, methods):
    print "parse_steps2\n"
    count = 0
    for step in steps:
        steps_obj = Step()
        steps_obj.number = count
        count +=1
        print step
        for i in ingredients:
            if i.name in step:
                steps_obj.ingredients.append(i.name)
        for t in tools:
            if t in step:
                steps_obj.tools.append(t)
        for m in methods:
            if m in step:
                steps_obj.methods.append(m)
        print step_obj
        list_out.append(step_obj)
    return list_out