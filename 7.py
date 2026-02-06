# 7. Reverse Integer
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# Example 1:
# Input: x = 123
# Output: 321

# Constraints
# -231 <= x <= 231 - 1
# My solution
class Solution(object):
    def reverse(self, x):
        q=[]
        t=[]
        s=[]
        for i in str(x):
            if i != '-':
                q.append(int(i))

        for val in reversed(q):
            t.append(val)
        
        for val in t:
            s.append(str(val))
        
        string = ''
        for val in t:
            string = string + str(val)

        surya = -int(string)
        rashmitha = int(string)
        min_value = -2 ** 31
        max_value = 2 ** 31 - 1
        if (min_value <= surya <= max_value) or (min_value <= rashmitha <= max_value):
            if x < 0:
                return surya
            else:
                return rashmitha
        else:
            return 0
            

#chatgpt
x = -1123

# Convert to string, strip '-', reverse digits
rev_str = str(abs(x))[::-1]

# Convert back to integer with sign
rev_num = int(rev_str) * (-1 if x < 0 else 1)

print(rev_num)


    
        
