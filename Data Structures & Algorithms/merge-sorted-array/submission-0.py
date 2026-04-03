class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = nums1[:m]

        k = 0
        i = 0
        j = 0

        while i < len(left) and j < len(nums2):
            if left[i] <= nums2[j]:
                nums1[k] = left[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            
            k += 1

        while i < len(left):
            nums1[k] = left[i]
            i += 1
            k += 1
        
        while j < len(nums2):
            nums1[k] = nums2[j]
            j += 1
            k += 1