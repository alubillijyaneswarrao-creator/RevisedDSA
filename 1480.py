# 1480. Running Sum of 1d Array
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
class Solution(object):
    def runningSum(self, nums):
        output = 0
        arr=[]
        for i in nums:
            output +=i
            arr.append(output)
        return arr
        
