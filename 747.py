# 747. Largest Number At Least Twice of Others
# You are given an integer array nums where the largest integer is unique.

# Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

 

# Example 1:

# Input: nums = [3,6,1,0]
# Output: 1
# Explanation: 6 is the largest integer.
# For every other number in the array x, 6 is at least twice as big as x.
# The index of value 6 is 1, so we return 1.
#Today i have solved this problem without anu help but i've passed the test cases but here comes the actual problem when i submit the code , it will show me hidden test cases failed.
#So i learned ki we must not code according to the test cases but to the algorithm and function.
# -> The code i did 
class Solution(object):
    def dominantIndex(self, nums):
        max_number = max(nums)
        max_index = 0
        for i in range(len(nums)):
            if nums[i] == max_number:
                max_index = i
        a=[]
        b=[]
        for x in nums[0::2]:
            a.append(x)
        for y in nums[1::2]:
            b.append(y)
        found = False
        for val in a :
            if val * 2 == max_number and max_number not in a:
                return (max_index)
                found = True
                break
        for val in b :
            if val * 2 == max_number and max_number not in b:
                return (max_index)
                found = True
                break
        if not found:
            return (-1)
        for i in range(len(nums)):
            if i != max_index and max_number < 2 * nums[i]:
                return -1
            return max_index

#Actual working code for all test cases:
# method - 1 using index function to get the index value of highest number of array.
tgt = max(nums)
        idx = nums.index(tgt)
        for i in range(len(nums)):
            if i!=idx and tgt<2 * nums[i]:
                return -1
        return idx
#method - 2 without using index function to retrieve highest number index of array
n = [ 3,6,1,0]
max_index = 0
max_number = max(n)
for i in range(len(n)):
    if n[i] == max_number:
        max_index = i

for i in range(len(n)):
    if i!=max_index and max_number < n[i] * 2:
        print(-1)
print(max_index)
  
