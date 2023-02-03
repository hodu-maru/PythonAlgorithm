n = input('숫자:')

nums = list(str(n))

for i in range(len(nums)):
    nums[i] = int(nums[i])

left = 0
right = 0
for i in range(len(nums) // 2):
    left += nums[i]
    right += nums[len(nums) - i - 1]

if left == right:
    print('LUCKY')
else:
    print('READY')


