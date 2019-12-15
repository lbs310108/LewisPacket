# insert file
# file_path is the file path;string is the insert string;keywords is that the string is insert the before


def insert(file_path, string, keywords):
    string = string + "\n"
    with open(file_path, 'r') as f:
        file_read = f.read()
        position = file_read.find(keywords)

    if position != -1:
        file_read = file_read[:position] + string + file_read[position:]
        with open(file_path, 'w') as f:
            f.write(file_read)
            f.close()

# modify the file
# file_path is the file path;old_string is the old string;new_string is the new string


def modify(file_path, old_string, new_string):
    new_file = ''
    with open(file_path) as f:
        for line in f:
            line = line.replace(old_string, new_string)
            new_file += line
        f.close()

    with open(file_path, 'w') as f:
        f.write(new_file)
        f.close()

# Determines if the string is in the file
# file_path is the file path;string is searched by the line


def bool_string(file_path, string):
    value_list = []
    with open(file_path) as f:
        for line in f:
            value = line.find(string)
            value_list.append(value)
        f.close()
    for v in value_list:
        if v == 0:
            return True

    return False

