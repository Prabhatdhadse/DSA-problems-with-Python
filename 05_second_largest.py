
nums = [55,32,97,-55,42,45,88,28]
largest = float("-inf")
S_largest = float("-inf")

n = len(nums)
for i in range(0,n):
    largest = max(largest,nums[i])
for i in range(0,n):
    if nums[i] > S_largest and nums[i] != largest:
        S_largest = nums[i]
print(S_largest)

