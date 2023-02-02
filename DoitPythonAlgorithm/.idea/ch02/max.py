
from typing import Any, Sequence
# Any : 임의의 자료형. (Object)같은건가봄
# Sequence : 배열 형태의 상위 type인가 봄.
def max_of(a: Sequence) -> Any:
    #Sequence 타입의 변수 a를 인자로 받고, Any 타입의 값 반환....이거 굳이..?
    max = a[0]
    for i in range(1, len(a)):
        if a[i] > max:
            max = a[i]
    return max
#mutable한 리스트에서는 실제 인수를 넘겨주지만, immutable한 튜플에서는 실제 인수를 넘기지 않는다는게 뭔솔?

print(__name__)

#파이썬에서 하나의 스크립트 프로그램을 모듈이라 함. 확장자를 포함하지 않는 파일의 이름 자체를 모듈 이름으로 사용함.
#이 파이썬 프로그램 파일 이름이 max이므로 모듈 이름도 max임.
#이 파일이 다른 파일에서 import될때는 max지만, 이 파일에서 직접 실행될 때는 __main__ 임.

if __name__ == '__main__':
    #max.py를 직접 시작한 경우에만 실행
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수 입력:'))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요:'))

    print(f'최댓값은 {max_of(x)}입니다.')

