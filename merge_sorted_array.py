class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # e.g. nums1 = [1,2,3,0,0,0] m =3 ------- nums2 = [2,5,6] n = 3
        
        # Start comparing from back of both arrays
        
        # j = m + n -1 ---- to track empty spaces
        # if nums1 > nums2, put nums1 at last j,  j-=1
        # if nums2 >= nums1, puts nums2 at last j, j-=1
        while n > 0 and m>0:
            if nums2[n-1] > nums1[m-1]:
                nums1[m+n-1] = nums2[n-1]
                n = n - 1
            else:
                nums1[m+n-1]=nums1[m-1]
                m = m - 1
        
        # For cases where we have reached at start of nums1 while tracing from back
        # e.g. nums1 = [4,5,6,0,0,0]    nums2 = [1,2,3]
        # You will compare 3 and 6, shift 6 at end,  m-=1, j-= 1
        # You will compare 3 and 5, shift 5 at end,  m-=1, j-= 1
        # You will compare 3 and 4, shift 5 at end,  m-=1, j-= 1
        
        # Now since nums2 elements are pending and no elements are remaining for nums1
        # we directly copy remaining elements of nums2 at nums1 starting from 0
        if n > 0:
            nums1[:n] = nums2[:n]