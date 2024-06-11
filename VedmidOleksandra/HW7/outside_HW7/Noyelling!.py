# Write a function taking in a string like
# WOW this is REALLY      amazing and returning
# Wow this is really amazing.
# String should be capitalized and properly spaced. Using re and string is not allowed.

# EXAMPLES
# filter_words('HELLO CAN YOU HEAR ME') #=> Hello can you hear me
# filter_words('now THIS is REALLY interesting') #=> Now this is really interesting
# filter_words('THAT was EXTRAORDINARY!') #=> That was extraordinary!

# def filter_words(st):
#     print(st.split())
#     print(st[0].upper() + st[1:].lower())
#
#
# # Пример использования:
# filter_words("programiz is Lit")

def filter_words(st):
    # Split the string into words
    sentence = st.split()

    # Capitalize the first word and make the rest lowercase
    formatted_words = [sentence[0].capitalize()] + [word.lower() for word in sentence[1:]]

    # Join the words with a single space
    formatted_string = ' '.join(formatted_words)

    return formatted_string

# Example usage
# input_string = "WOW this is REALLY          amazing"
# input_string = "hELLO CAN YOU HEAR ME"
# formatted_string = filter_words(input_string)
# print(formatted_string)



