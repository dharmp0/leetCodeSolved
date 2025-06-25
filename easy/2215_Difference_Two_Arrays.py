class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_only = set(nums1) - set(nums2)
        nums2_only = set(nums2) - set(nums1)

        return [list(nums1_only), list(nums2_only)]
