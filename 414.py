# 414. Third Maximum Number
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

class Solution:
    def thirdMax(self, nums):
        nums = list(set(nums))
        nums.sort(reverse=True)
        return nums[2] if len(nums) >= 3 else nums[0]
