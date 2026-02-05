# 3379. Transformed Array
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array nums that represents a circular array. Your task is to create a new array result of the same size, following these rules:
# For each index i (where 0 <= i < nums.length), perform the following independent actions:
# If nums[i] > 0: Start at index i and move nums[i] steps to the right in the circular array. Set result[i] to the value of the index where you land.
# If nums[i] < 0: Start at index i and move abs(nums[i]) steps to the left in the circular array. Set result[i] to the value of the index where you land.
# If nums[i] == 0: Set result[i] to nums[i].
# Return the new array result.
# The approach i have used to get the result but couldnt get it done for negative numbers, as appending fails.
nums = [-10,-10,-4]
output = []
for i in range(len(nums)):
    if nums[i] > 0:
        s = (i + nums[i]) % len(nums)
        output.append(nums[s])
    else:
        s = (i - nums[i] ) % len(nums)
        output.append(nums[s])
print(output)
o1 = []
for i in output:
    if i < 0:
        i = i * -1
        o1.append(i)
    else:
        o1.append(i)
o2 = sorted(o1)
print(o2)
o3=[]
for i in o2:
    if i > 0:
        i = i * -1
        o3.append(i)
print(o3)
#Optimized code
class Solution(object):
    def constructTransformedArray(self, nums):
        n = len(nums)
        result = []
        for i in range(n):
            if nums[i] == 0:
                result.append(0)
            else:
                landing = (i + nums[i]) % n
                result.append(nums[landing])
        return result




    
