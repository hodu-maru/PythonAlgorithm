print('세 정수의 최댓값을 구합니다.')

a = int(input('정수 a:'))
b = int(input('정수 b:'))
c = int(input('정수 c:'))
#파이썬 input함수는 str을 반환. int로 형변한 해줘야 int형으로 들어가 대소비교 가능
max = a

if b > max:
    max = b

if c > max:
    max = c

print(f'최댓값은 {max}입니다.')
