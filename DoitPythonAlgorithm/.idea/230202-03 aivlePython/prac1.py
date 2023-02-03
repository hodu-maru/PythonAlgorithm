def electricPay(usage):
    #기본요금 1600 + 전력량 요금 100k + 100이상k + 200k이상) 1.1
    elecPay = 0
    if usage > 200:
        elecPay += (usage-200) * 187.9
        usage = 200
    if usage > 100:
        elecPay += (usage - 100) * 125.9
        usage = 100
    elecPay += usage * 60.7

    return int((elecPay + 1600) * 1.137)

usage = int(input('전력 사용량:'))

print(electricPay(usage))
