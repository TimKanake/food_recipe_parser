# The PP (Pretty Print) class to concatenate the lists of ingredients,
# steps, tools, methods.

def vertical_list_to_str(list_in, list_name):
    str_out = "\n"
    count = 0
    for x in list_in:
        if list_name == "ingredients":
            str_out += "\t" + str(x) + "\n"
        if list_name == "steps":
            str_out += "\t" + str(x) + "\n"
            count += 1
    str_out = str_out[:-1] # remove the last \n character
    return str_out

def horz_list_to_str(list_in, list_name=None):
    str_out = ""

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

    elif list_name == "ingredients":
        length_limit = 79
        for x in list_in:
            if len(str_out) + len(x) > length_limit:
                length_limit *= 2
                str_out += "\n\t\t"
            str_out += x + ", "
        str_out = str_out[:-2].capitalize()
        return str_out

    elif list_name == "times":
        hours = []
        minutes = []
        seconds = []
        for x in list_in:
            x_split = x.split(" ")
            if "hour" in x_split[1]:
                if not x_split[0].isdigit():
                    hours.append(1)
                else:
                    hours.append(int(x_split[0]))
            if "minute" in x_split[1]:
                if not x_split[0].isdigit():
                    minutes.append(1)
                else:
                    minutes.append(int(x_split[0]))
            if "second" in x_split[1]:
                if not x_split[0].isdigit():
                    seconds.append(1)
                else:
                    seconds.append(int(x_split[0]))

        total_min = sum(minutes)
        total_hr = sum(hours)
        total_s = sum(seconds)
        return str(total_hr) + " hr(s) " + str(total_min) + " minute(s) " + str(total_s) + " seconds"


def pretty_string(list_in, list_name, direction):
    if direction is "horizontal":
        return horz_list_to_str(list_in, list_name)
    elif direction in "vertical":
        return vertical_list_to_str(list_in, list_name)
    else:
        return "Error: PP.pretty_string given invalid direction arg: " + str(list_name) + ". Should be 'horizontal' or 'vertical'"
