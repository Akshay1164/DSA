def twoSum(self, nums, target):
        hashmap = {}
        for i,num in enumerate(nums):
            compliment = target - num
            if compliment in hashmap:
                return [hashmap[compliment],i]
            hashmap[num] = i
        return None
result = twoSum(None,[2,7,11,15],9)
print(result)   