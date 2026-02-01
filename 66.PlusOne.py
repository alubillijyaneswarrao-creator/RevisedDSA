# 66. Plus One
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

#This is the answer I'v tried with step-step by understanding , but theres complexity issue but yet its working.
n = [4,3,2,1]
t = []
for val in n:
    t.append(val)
print(t)
q =[]
for i in range(len(t)):
    q.append(str(t[i]))
print(q)
concat = '' 
for i in range(len(q)):
    concat =concat + q[i]
print(concat)
final_sum = int(concat) + 1
print(final_sum)
digits = list(map(int,str(final_sum)))
print(digits)

#So reduce Complexity and other things like code length and using minimal functions, we can do this instead
class Solution(object):
    def plusOne(self, digits):
        # Convert list of digits to string
        num_str = ''.join(map(str, digits))
        
        # Convert to integer and add one
        num = int(num_str) + 1
        
        # Convert back to list of digits
        result = list(map(int, str(num)))
        return result






    
