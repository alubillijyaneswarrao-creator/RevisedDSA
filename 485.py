# 485. Max Consecutive Ones
# Attempted
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2
# My solution but couldnt surpass Time limit exceed problem
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        if 1 <= len(nums) <= 10 ** 5:
            t=[]
            for i in range(len(nums)):
                for j in range(i+1,len(nums)+1):
                    t.append(nums[i:j])
            ones = [h for h in t if all(x == 1 for x in h)]
            if not ones:   
                return 0
            maxi = max(ones, key=len)  
            return len(maxi)
# Completed (Handled TLE problem)
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        c = 0
        d = 0
        for i in nums:
            if i == 1:
                c = c + 1 
                d = max(c,d)
            else:
                c = 0
        return d
            



        

        
        


        

        
        
