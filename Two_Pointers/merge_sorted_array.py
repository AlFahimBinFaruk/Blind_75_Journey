https://leetcode.com/problems/merge-sorted-array/
class Solution:
    # Time O(N)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # nums1[m:] = nums2[:n]
        # nums1.sort()
        last = len(nums1) - 1

        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]    
                n -= 1
            last -= 1    

        # check for leftovers in nums2
        while n > 0:
            nums1[last] = nums2[n-1]
            n -= 1      
            last -= 1    
