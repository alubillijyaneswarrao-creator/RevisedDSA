# You are given an array of integers nums of length n.

# The cost of an array is the value of its first element. For example, the cost of [1,2,3] is 1 while the cost of [3,4,1] is 3.

# You need to divide nums into 3 disjoint contiguous subarrays.

# Return the minimum possible sum of the cost of these subarrays.

#This literally gave me headace , but finally solved it on my own.
# ** 0ms 100% - Beats solution
class Solution(object):
    def minimumCost(self, nums):
        m = len(nums)
        t = sorted(nums)
        if m <= 3:
            min_arr = sum(nums)
        else:
            def is_ok():
                for val in [t[0],t[1],t[2]]:
                    if nums[0] == val:
                        return True
                return False
            if (m > 3) and (t[0] != nums[0] and not is_ok()):
                min_arr = nums[0] + t[0] + t[1]
            else:
                min_arr = t[0] + t[1] + t[2]
        return min_arr
# An ALternative but good code not better than above code but can be used 
class Solution(object):
    def minimumCost(self, nums):
        impv=nums[0]
        temp=nums[1:]
        temp.sort()
        sum = 0
        for i in range(0,2):
            sum += temp[i]
        total = impv+sum
        return total
        
        

        

        
