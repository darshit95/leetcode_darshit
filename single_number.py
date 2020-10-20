class Solution:
    
#The most crucial trick here is to recognize that if you XOR any same number together, you #cancel it out (=0).
#For example:
#nums = [2,4,5,4,3,5,2]
#XORing everything together
#= 2 ^ 4 ^ 5 ^ 4 ^ 3 ^ 5 ^ 2
#= (2^2) ^ (4^4) ^ (5^5) ^ 3
#= 0 ^ 0 ^0 ^ 3
#= 3
    
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
                res ^= n
        return res
            
            
# Using lambda and reduce
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x,y:x^y,nums)
