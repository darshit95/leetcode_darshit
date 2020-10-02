class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # e.g. array = [2, 7, 11, 15]
        hash_map = {}
        for i, x in enumerate(nums): # [i=0,x=2, i=1,x=7 ......]
            
            # Search if no is already a key in dict
            # If found, return [previous_index, current_index]
            if x in hash_map:
                return [hash_map[x], i]
            
            # store in dictionary with key as DIFFERENCE between target & no
            # and value as index
            else:
                hash_map[target - x] = i