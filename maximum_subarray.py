class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        sum_so_far = nums[0]
        for i in range(1,len(nums)):
            
            # If sum obtained till now is already less than = 0
            # Then no need to add more negative values to it
            if sum_so_far <= 0:
                sum_so_far = nums[i]
            
            # else we can add current num in sum_so_far
            else:
                sum_so_far += nums[i]
            max_so_far = max(sum_so_far, max_so_far)
        
        return max_so_far