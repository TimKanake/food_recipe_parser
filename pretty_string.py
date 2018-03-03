# The PP (Pretty Print) class to concatenate the lists of ingredients,
# steps, tools, methods.

def vertical_list_to_str(list_in, list_name):
    str_out = "\n"
    count = 0
    for x in list_in:
        if list_name == "ingredients":
            str_out += "\t" + str(x) + "\n"
        if list_name == "steps":
            str_out += "\tStep " + str(count) + ". " + str(x) + "\n"
            count += 1
    str_out = str_out[:-1] # remove the last \n character
    return str_out

def horz_list_to_str(list_in, list_name=None):
    str_out = None
    if list_name == "methods":
        if len(list_in) > 0:
            str_out = list_in[0][0]
        if len(list_in) > 1:
            str_out += ', ' + list_in[1][0]
        return str_out
    elif list_name == "tools":
        if len(list_in) > 0:
            str_out = list_in[0][0]
            if len(list_in) > 1:
                for tool in list_in[1:]:
                    if tool[0] not in str_out:
                        str_out += ', ' + tool[0]
        return str_out

def pretty_string(list_in, list_name):
    if list_name in ["methods", "tools"]:
        return horz_list_to_str(list_in, list_name)
    elif list_name in ["ingredients", "steps"]:
        return vertical_list_to_str(list_in, list_name)
    else:
        return "Error: PP.pretty_string given invalid list_name arg: " + str(list_name)
