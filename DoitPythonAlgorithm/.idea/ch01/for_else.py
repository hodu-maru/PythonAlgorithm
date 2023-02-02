import random

n = int(input('난수 개수 입력:'))

for _ in range(n):
    r = random.randint(10,99)
    print(r)
    if r == 13:
        break

print('\n난수 생성 종료')