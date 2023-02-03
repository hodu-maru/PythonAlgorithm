def Q3Solution(a, b):

    answer = 0

    if a > b:
        b, a = a, b

    #특정 수의 약수들 구하기
    for num in range(a, b + 1):
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1

        if count % 2 == 0:
                answer += num
        elif count % 2 == 1:
                answer -= num

    return answer

a = int(input('a:'))
b = int(input('b:'))

print(Q3Solution(a, b))

