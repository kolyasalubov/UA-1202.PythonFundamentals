def count_sheep(sheep):
    return sheep.count(True)


print(count_sheep([True, True, True, False,
                   True, True, True, True,
                   True, False, True, False,
                   True, False, False, True,
                   True, True, True, True,
                   False, False, True, True]))
