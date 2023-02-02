#배열의 원소 수, 최댓값, 최솟값 입력받아 최댓값과 최솟값 안에서 배열을 구성하는 원소값은 난수로 결정하는

from random import randint
from max import max_of
max = int(input('최댓값:'))
min = int(input('최솟값:'))
arrNum = int(input('원소 개수:'))

x = list()

for i in range(arrNum):
    x.append(randint(min,max))

print(x)
print(f'{max_of(x)}')


