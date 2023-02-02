
side = int(input('짧은 변의 길이:'))

for i in range(1,side + 1):
    for _ in range(i):
        print('*',end='')
    print()
