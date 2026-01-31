# 724. Find Pivot Index
# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.

class Solution(object):
    def pivotIndex(self, nums):
        n = len(nums)
        
        for l in range(n):
            sumi = 0
            sumj = 0
            
            for i in range(l):
                sumi += nums[i]
            
            for j in range(l+1, n):
                sumj += nums[j]
            
            if sumi == sumj:
                print(l)
                return l   
        
        return -1  
#The aboce code will have higher complexity and incomplete algorith . So i tried a precise way of finding Pivot element.
class Solution(object):
    def pivotIndex(self, nums):
        total_sum  = sum(nums)
        l = 0

        for i,num in enumerate(nums):
            r = total_sum - l - num 
            if l == r:
                return i 
            l = l + num

        return -1
