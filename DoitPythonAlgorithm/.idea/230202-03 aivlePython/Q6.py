
def Q6Func(n):
    for i in range(n):
        if i * i == n:
            return (i + 1) ** 2
    return -1




n = 121
print(Q6Func(n))
