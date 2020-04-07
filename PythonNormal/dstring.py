# input keywords and string, return the string after the keywords


def after_keywords(string, keywords):
    return string[string.rfind(keywords):]
