import requests
import re
from builtins import input as inp


def get_user_input():
    """
    Get user input from the command line.
    :return: The user input as an username string.
    """
    user_input = inp("Enter a username:")
    try:
        match = re.fullmatch("^[a-zA-Z]*$", user_input)
        if match is not None:
            return user_input
        else:
            print("Invalid Username")
    except Exception as e:
        raise e
    finally:
        return "dummy"


def Find_nationality(username):
    """
    Find the probable nationality of the user.
    :param username: The username to find the nationality of.
    :return: The country dictionary.
    """
    res = requests.get("http://api.nationalize.io/?name="+username)
    countries = res.json()["country"]
    for country in countries:
        if country["probability"] == 0.100:
            return country


def print_country(country):
    """
    Print user's country name.
    :param username: The country dictionary.
    """
    if country["id"] == "US":
        print("The user is likely located in the United States.")
    elif country["id"] == "GB":
        print("The user is likely located in United Kingdom.")
    elif country["id"] == "SE":
        print("The user is likely located in Sweden.")
    elif country["id"] == "IT":
        print("The user is likely located in Italy.")
    elif country["id"] == "IS":
        print("The user is likely located in Iceland.")
    elif country["id"] == "FR":
        print("The user is likely located in France.")
    # elif country["id"] == "CA":
        # print("The user is likely located in Canada.")
    # TODO: Complete this for remaining countries.


def print_probability(country):
    """
    Print probability for each country.
    :param username: The country dictionary.
    """
    if country["id"] == "US":
        print("The probability is: "+country["probability"])
    elif country["id"] == "GB":
        print("The probability is: "+country["probability"])
    elif country["id"] == "SE":
        print("The probability is: "+country["probability"])
    elif country["id"] == "IT":
        print("The probability is: "+country["probability"])
    elif country["id"] == "IS":
        print("The probability is: "+country["probability"])
    elif country["id"] == "FR":
        print("The probability is: "+country["probability"])
    # elif country["id"] == "CA":
        # print("The user is likely located in Canada.")
    # TODO: Complete this for remaining countries.


def main(args=None):
    """
    The main function.
    """
    args = get_user_input()
    country = Find_nationality(args)
    print_country(country)
    print_probability(country)


if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(e)
