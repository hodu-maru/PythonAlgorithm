print('a부터 b까지 정수의 합을 구함')

a = int(input('a를 입력:'))
b = int(input('b를 입력:'))

if a > b:
    a, b = b, a

sum = 0

for i in range(a, b + 1):
    if i < b:
        print(f'{i} + ', end='')
    else:
        print(f'{i} = {sum}',end='')

    sum += i


