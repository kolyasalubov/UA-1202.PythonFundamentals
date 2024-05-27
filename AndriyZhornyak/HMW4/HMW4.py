# #task 1
# a = float(input())
# F = 0
# if a >= -273.15:
#     F = (a *9.5)+32
#     print(F)
# else:
#     print("error")

x = 10

match x:
    case int(value):
        if value < 0:
              print("aasa")
        else:
            print("aaaa")
    case str(value):
             print("lll")
    case _:
        print(iiiew)