def class_name_changer(cls, new_name):
    if not new_name[0].isupper() or not new_name.isalnum():
        raise Exception("Name must start with uppercase and contain only letters and numbers")
    cls.__name__ = new_name
