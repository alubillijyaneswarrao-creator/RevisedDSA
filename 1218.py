# 1281. Subtract the Product and Sum of Digits of an Integer
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer number n, return the difference between the product of its digits and the sum of its digits.
# Example 1:

# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15

class Solution(object):
    def subtractProductAndSum(self, n):
        p =[]
        for i in str(n):
            p.append(i)
        mul = 1
        for i in (p):
            mul = mul * int(i) 
        s = 0
        for i in p:
            s = s + int(i)
        
        return (mul-s)

        
