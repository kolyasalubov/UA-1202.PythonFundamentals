# Task3. Write a function that calculates the number of charactes in
# given string.
# input: "Hello"
# output: {"h":1, "e":1, "l":2, "o":1}

def character_count(s):
    s = s.lower()
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

input_string = 'Hello'
print(character_count(input_string))