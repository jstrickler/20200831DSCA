"""
Utilities for reading knight data
"""

FILE_NAME = 'DATA/knights.txt'


def read_data():
    """
    Read knight data from colon-separated fields.

    :return: dict of knight data
    """
    knight_data = {}

    with open(FILE_NAME) as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(':')
            knight_data[name] = {
                "title": title,
                "color": color,
                "quest": quest,
                "comment": comment,
            }

    return knight_data


def get_names_and_titles(data):
    """
    Create a list of strings where each string is in the format "TITLE NAME"

    :param data: dict of knight data
    :return: list of strings
    """

    name_list = []
    for name, fields in data.items():
        name_list.append(f"{fields['title']} {name}")
    return name_list


def get_field_data(data, knight_name, field_name):
    """
    Retrieve data from one field from a specified knight

    :param data: dict of knight data
    :param knight_name: name of knight as string
    :param field_name: field name
    :return: data field value
    """
    return data[knight_name][field_name]


if __name__ == '__main__':  # if I am run as a script, not imported as a module
    print("HI MOM!!")
    data = read_data()