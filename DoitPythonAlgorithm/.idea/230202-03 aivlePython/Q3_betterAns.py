def solution(N):
    count = 0
    for i in range(1, int(N**(1/2)) + 1):
        if(N % i == 0):
            count +=1
            if(i != (N//i)):
                count += 1
    return count

left = 13
right = 17
sum =0
for i in range(left, right+1):
    c = solution(i)
    if c % 2 == 0 :
        sum += i
    else :
        sum -= i
print(sum)