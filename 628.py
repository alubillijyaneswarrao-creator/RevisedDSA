#mY solution which worked but failed hidden test cases
class Solution(object):
    def maximumProduct(self, nums):
        n = len(nums)
        t = sorted(nums)
        q = []
        for j in t:
            if j < 0 and len(t) > 3:
                j = j * (-1)
                q.append(j)
            else:
                q.append(j) 
                
        f = sorted(q)
        mul = 1
        for i in range(len(f) - 1 , len(f) - 4, -1):
            mul = mul * f[i]
        return (mul)
#optimized solution
class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3] , nums[0] * nums[1] * nums[-1])
        
        
