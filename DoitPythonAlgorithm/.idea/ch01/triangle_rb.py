
side = int(input('변의 길이:'))

for i in range(side + 1):
    for _ in range(side - i):
        print(' ',end='')
    for _ in range(i):
        print('*',end='')
    print()
