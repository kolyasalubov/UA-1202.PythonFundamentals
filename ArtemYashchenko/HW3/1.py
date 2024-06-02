#Python philosophy
philosophy = """Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. 
Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality 
beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one-- 
and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is 
often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. 
Namespaces are one honking great idea -- let's do more of those!"""

#Find the number of the words "better", "never", and "is"
better_count = philosophy.count("better")
never_count = philosophy.count("never")
is_count = philosophy.count("is")

#Display all text in uppercase
uppercase_philosophy = philosophy.upper()

#Replace all occurrences of the symbol "i" with "&"
replaced_philosophy = philosophy.replace("i", "&")

#Results
print(f"Number of occurrences of 'better': {better_count}")
print(f"Number of occurrences of 'never': {never_count}")
print(f"Number of occurrences of 'is': {is_count}")
print("\nUppercase text:")
print(uppercase_philosophy)
print("\nText with 'i' replaced by '&':")
print(replaced_philosophy)