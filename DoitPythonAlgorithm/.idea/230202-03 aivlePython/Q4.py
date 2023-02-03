data = input('숫자로 이루어진 문자열:')

nums = list(data)

for i in range(len(nums)):
    nums[i] = int(nums[i])

answer = nums[0]
for i in range(1, len(nums)):
    #수열에서 하나씩 꺼내와서 계산해

    if answer == 0 or nums[i] == 0 or answer == 1 or nums[i] == 1 :
        answer = answer + nums[i]

    #앞이나 뒤 수가 0이면 더해야 하고
    else:
        answer = answer * nums[i]

    #둘 다 0이 아니면 곱하면 돼

print(answer)

#차례로 계산. 앞이나 뒤에 0이 있으면 더해야 하고, 아니면 곱하기를 해야 함.

