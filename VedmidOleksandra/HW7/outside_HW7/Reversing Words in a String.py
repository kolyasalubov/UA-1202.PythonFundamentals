# You need to write a function that reverses the words in a given string. A word can also fit an empty string.
# If this is not clear enough, here are some examples:
# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.
# "Hello World" --> "World Hello"
# "Hi There." --> "There. Hi"
# Example (Input --> Output)

def reverse(st):
    words = st.split()  # Split the input string into words
    reversed_words = words[::-1]  # Reverse the order of the words
    # words[::-1] используется для создания среза (slice) списка words с шагом -1, что приводит к его реверсированию.

# Давайте разберём это:
#
# words - это список слов, полученных после разделения строки на слова.
# [::-1] - это срез списка. Обозначение [start:stop:step] используется для получения подсписка от индекса start
# до индекса stop с шагом step. Если start и stop не указаны, а только step, это означает, ч
    # то срез производится от начала
# до конца списка с шагом step, в данном случае -1.
# Поскольку start и stop не указаны, а только step равен -1,
# срез будет произведён от конца к началу списка, что приведёт к его реверсированию.
# Таким образом, words[::-1] возвращает список words, но в обратном порядке.

    reversed_string = ' '.join(reversed_words)  # Join the reversed words into a string
    print(reversed_string)  # Print the reversed string
    return reversed_string


# # Example usage:
# reverse("Hello World")
# reverse("Hi There.")
