from max import max_of

print('배열의 최댓값을 구함')

num = 0
x = []

while True:
    s = input(f'x[{num}]값을 입력:')
    if s == 'End':
        break
    x.append(int(s))
    num += 1

print(f'{num} 개를 입력했습니다.')
print(f'최댓값은 {max_of(x)}입니다.')