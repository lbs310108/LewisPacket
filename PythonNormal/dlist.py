# list duplicate remove
def dr_list(list_name):
    new_list = []
    for value in list_name:
        if value not in new_list:
            new_list.append(value)
    return new_list


# if value in value_list return true, else return false
def value_in_list(value, value_list):
    if value in value_list:
        return True
    else:
        return False

