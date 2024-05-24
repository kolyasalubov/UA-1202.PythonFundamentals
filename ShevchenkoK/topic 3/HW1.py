zen_of_python = ("The Zen of Python, by Tim Peters:\n\t"
                 "Beautiful is better than ugly.\n\t)"
                 "Explicit is better than implicit.\n\t"
                 "Simple is better than complex.\n\t"
                 "Complex is better than complicated.\n\t"
                 "Flat is better than nested.\n\t"
                 "Sparse is better than dense.\n\t"
                 "Readability counts.\n\t"
                 "Special cases aren't special enough to break the rules.\n\t"
                 "Although practicality beats purity.\n\t"
                 "Errors should never pass silently.\n\t"
                 "Unless explicitly silenced.\n\t"
                 "In the face of ambiguity, refuse the temptation to guess.\n\t"
                 "There should be one-- and preferably only one --obvious way to do it.\n\t"
                 "Although that way may not be obvious at first unless you're Dutch."
                 "Now is better than never.\n\t"
                 "Although never is often better than *right* now.\n\t"
                 "If the implementation is hard to explain, it's a bad idea.\n\t"
                 "If the implementation is easy to explain, it may be a good idea.\n\t"
                 "Namespaces are one honking great idea -- let's do more of those!")

# part 1
print("Number of 'better':",zen_of_python.count("better"))
print("Number of 'never':", zen_of_python.count("never"))
print("Number of 'is':", zen_of_python.count("is"))

# part 2
print(zen_of_python.upper())

# part 3
print(zen_of_python.replace("i", "&"))


