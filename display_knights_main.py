"""
Display data about the knights.
"""

from knightlib import read_data, get_field_data, get_names_and_titles


def main():
    """
    Program entry point
    """
    knight_data = read_data()

    for knight in get_names_and_titles(knight_data):
        print(knight)
    print()

    print(get_field_data(knight_data, "Bedevere", "quest"))


# if this file run as script (not imported as module)
if __name__ == '__main__':
    main()

