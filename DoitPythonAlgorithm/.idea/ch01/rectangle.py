
area = int(input('직사각형 넓이:'))

for i in range(1,(area // 2) + 1):
    if i * i > area:
        break
    if area % i == 0:
        print(f'{i} x {area // i} = {area}')