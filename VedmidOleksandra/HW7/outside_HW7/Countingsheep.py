# Consider an array/list of sheep where some sheep may be missing from their place.
# We need a function that counts the number of sheep present in the array (true means present).
#
# For example,
# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]
# The correct answer would be 17.
#
# Hint: Don't forget to check for bad values like null/undefined


def count_sheeps(sheep):
    return sum(1 for sheeps in sheep if sheeps is True)


sheep = [True, True, True, False,
         True, True, True, True,
         True, False, True, False,
         True, False, False, True,
         True, True, True, True,
         False, False, True, True]

print(count_sheeps(sheep))  # Output: 17


#########################################################
def count_sheeps(sheep):
    count = 0
    for sheeps in sheep:
        if sheeps:
            count += 1
    return count


sheep = [True, True, True, False,
         True, True, True, True,
         True, False, True, False,
         True, False, False, True,
         True, True, True, True,
         False, False, True, True]
print(count_sheeps(sheep))  # Output: 17

# In Python, boolean values True and False are implicitly understood in conditional statements.
# When you iterate through a list (or any iterable) in a for loop, each element of the iterable is evaluated
# in a boolean context.
#
# In the provided count_sheeps function:
#
# for sheeps in sheep: iterates over each element (sheeps) in the sheep list.
# In the if sheeps: condition, each element (sheeps) is evaluated in a boolean context.
# If sheeps is True, the condition is true, and count is incremented.
# If sheeps is False, the condition is false, and count remains unchanged.
# So, in this function, True values are counted as present sheep, and False values are not counted.
# This is because Python treats True as equivalent to 1 and False as equivalent to 0 in numerical contexts.
# Therefore, adding 1 to count when sheeps is True effectively counts the number of True values in the sheep list.
