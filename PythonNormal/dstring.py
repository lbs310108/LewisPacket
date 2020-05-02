# input keywords and string, find from last, return the string after the keywords
def after_keywords_last(string, keywords):
    return string[string.rfind(keywords):]


# input keywords and string, find from first, return the string after the keywords
def after_keywords_first(string, keywords):
    return string[string.find(keywords):]


# input keywords and string,find from string. if find:return true;if not find:return false
def find_keywords_in_string(string, keywords):
    STR = string.find(keywords)
    if STR == -1:
        return False
    else:
        return True