def solution(number):
    if number < 0:
        return 0

    result = 0
    for i in range(1, number):
        if i % 3 == 0 and i % 5 == 0:
            result += i
        elif i % 3 == 0:
            result += i
        elif i % 5 == 0:
            result += i
    return result


print(solution(int(input("Enter a number: "))))
