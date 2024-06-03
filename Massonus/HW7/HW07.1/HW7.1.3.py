def characters_calculator(string):
    """function calculates the number of characters in a string"""

    string = string.lower()
    result = {}

    for i in string:
        if i in result:
            continue
        else:
            result.update({i: string.count(i)})

    return result


print("Result:", characters_calculator(input("Enter a string: ")))
