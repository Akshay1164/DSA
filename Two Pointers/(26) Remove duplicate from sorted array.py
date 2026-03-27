def removeduplicate(nums):
    l = 0
    for r in range(1,len(nums)):
        if nums[r] != nums[l]:
            l += 1
            nums[l] = nums[r]
    return l+1
result = removeduplicate([0,0,1,1,1,2,2,3,3,4])
print(result)