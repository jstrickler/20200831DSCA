"""
Delightful utilities for the DSCA
"""
ANIMALS = ['wombat', 'pine marten']

def spam():
    """
    Can of fatty meat stuff

    :return: None
    """
    print("Hello from spam()")


# "private" function
def _ham():
    """Helper function"""
    print("    Hello from _ham()")


def toast():
    """
    Delicious browned bread

    :return: None
    """
    print("Hello from toast()")
    _ham()

