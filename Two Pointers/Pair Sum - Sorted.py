'''
# brute force approach
nums = [1,2,3,4]
target = int(6)
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print([i,j])
            break
'''

# optimal approach
def pairsumsorted(nums,target):
    left = 0
    right = len(nums)-1

    while left<right:
        i = nums[left] + nums[right]
        if i == target:
            return [left, right]
        elif i < target:
            left += 1
        else:
            right -= 1
result = pairsumsorted([1,2,3,4,6],10)
print(result)