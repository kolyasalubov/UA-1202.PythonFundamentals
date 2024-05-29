def filter_words(st):
    st = ' '.join(st.split())
    return st.capitalize()


print(filter_words(input("Input your string: ")))
