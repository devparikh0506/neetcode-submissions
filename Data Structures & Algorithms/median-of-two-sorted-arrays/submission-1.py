class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)

        total = m+n
        half = (total+1)//2

        low = 0
        high = m

        while low <= high:

            i = low + (high-low)//2
            j = half - i
            
            l1 = nums1[i-1] if i > 0 else float("-inf")
            r1 = nums1[i] if i < m else float("inf")
            l2 = nums2[j-1] if j > 0 else float("-inf")
            r2 = nums2[j] if j < n else float("inf")

            if l1 <= r2 and l2 <= r1:

                if total % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)
            
            if l1 > r2:
                high = i-1
            else:
                low = i + 1
        
