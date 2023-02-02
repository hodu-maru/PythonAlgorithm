print('1부터 n까지 정수합')
n = int(input('n을 입력:'))

sum = 0
for i in range(1, n + 1):
    sum += i

print(f'합은 {sum}')

# range()함수는 이터러블 객체를 생성
# range(n)은 0이상 n미만의 수를 차례로 나열하는 수열 객체를
# range(a, b)는 a이상 b미만의 수열 객체를
# range(a, b, step)는 a이상 b미만의 수를 step간격으로 나열하는 수열 객체를 반환
