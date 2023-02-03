# 0 <= num <= 99

def q2Func(num):

    calcNum = num
    count = 0
    while(1):
        a = calcNum // 10
        b = calcNum % 10

        newNum = b * 10 + ((a + b) % 10)
        count += 1

        if newNum == num:
            return count

        calcNum = newNum

print(q2Func(71))

