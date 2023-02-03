def solution(a, b):

    max = 0
    if a > b:
        b, a = a, b

    for i in range(1, b + 1):
        if (a % i == 0) and (b % i == 0):
            max = i

    answer = max
    return answer


a = 12
b = 16
c = solution(a,b)
print(c)
