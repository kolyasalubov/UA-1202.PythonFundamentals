def are_you_playing_banjo(name):
    if name[0] == "r" or name[0] == "R":
        return name + " plays banjo"
    return name + " does not play banjo"


print(are_you_playing_banjo(input("Input your name: ")))
