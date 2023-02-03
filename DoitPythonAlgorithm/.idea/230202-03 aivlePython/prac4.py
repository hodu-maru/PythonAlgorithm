def squarePair(num):
    for root in range(num + 1):
        for pwr in range(2,6):
            if num == root ** pwr:
                print(f'{root}**{pwr}={num}')
                return
    print('결과없음')
    return




num = int(input('정수 입력:'))

squarePair(num)