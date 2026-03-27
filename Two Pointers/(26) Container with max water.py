''' This problem can be solved using the two-pointer technique. The idea is to use two pointers, 
one starting at the beginning of the array and the other at the end.
We calculate the area formed by the lines at these two pointers and update the maximum area found so far. 
Then, we move the pointer pointing to the shorter line inward, as moving the longer line inward cannot increase the area. 
We repeat this process until the two pointers meet. '''

def maxArea(height):
        max_area = 0
        l,r = 0 ,len(height)-1
        while l < r:
            h = min(height[l],height[r])
            w = r - l
            area = h*w
            max_area = max(area,max_area)
            if height[l] > height[r]:
                r -= 1
                
            else:
                l += 1
        return max_area
result = maxArea([1,8,6,2,5,4,8,3,7])
print(result)