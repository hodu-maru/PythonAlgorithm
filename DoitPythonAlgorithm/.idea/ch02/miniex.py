area = int(input('직사각형 넓이:'))

for i in range(1,32 + 1):
    if 32 % i == 0:
        print(f'{i} x {32 // i}')