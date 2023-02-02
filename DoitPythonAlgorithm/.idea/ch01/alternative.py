
print('+와 -를 번갈아 출력')
n = int(input('출력 개수:'))

for _ in range(n // 2):
    print('+-',end='')
# // 연산자: 나눗셈의 몫을 반환하는 연산자.
# _ : for문에서 index를 사용할 필요가 없을 때 무시하는 값.

if n % 2:
    print('+',end='')

print()