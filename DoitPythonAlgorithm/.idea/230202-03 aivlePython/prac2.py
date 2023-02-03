def printOperator(num):
    for i in range(num//2):
        print('+-', end='')
    if num % 2 == 1:
        print('+')




num = int(input('개수:'))
printOperator(num)

