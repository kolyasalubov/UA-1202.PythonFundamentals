def reverse(st):
    st = ' '.join(st.split(' ')[::-1]).strip()
    while '  ' in st:
        st = st.replace('  ', ' ')
    return st


print(reverse(input("Enter a string: ")))
