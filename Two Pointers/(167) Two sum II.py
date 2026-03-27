def twosumII(nums, target):
    l,r = 0, len(nums)-1
    
    while l < r:
        curSum = nums[l] + nums[r]
        if curSum > target:
            r -=1
        elif curSum < target:
            l +=1
        else: return [l,r]
    return[]
result = twosumII([1,2,4,7,8,11,15],9)
print(result)