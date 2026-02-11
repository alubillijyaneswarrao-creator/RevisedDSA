# 448. Find All Numbers Disappeared in an Array
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:
# Input: nums = [1,1]
# Output: [2]

class Solution(object):
    def findDisappearedNumbers(self, nums):
        nums2 = set(nums)
        n = len(nums)
        k = []

        for i in range(1, n + 1):
            if i not in nums2:
                k.append(i)

        return k
