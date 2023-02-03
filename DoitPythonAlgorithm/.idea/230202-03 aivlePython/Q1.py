def solution(a, b):
    if a > b:
        b, a = a, b

    i = 1
    while(1):
        if i % a == 0 and i % b == 0:
            return i
        i += 1

print(solution(12,16))