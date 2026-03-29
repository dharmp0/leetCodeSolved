class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(a) + len(b)
        half = total // 2

        if len(a) > len(b):
            a, b = b, a

        l,r = 0, len(a) - 1

        while True:

            m = (l+r)//2

            h = half - m - 2

            aleft = a[m] if m >= 0 else float("-infinity")
            aright = a[m+1] if (m+1) < len(a) else float("infinity")
            bleft = b[h] if h >= 0 else float("-infinity")
            bright = b[h+1] if (h+1) < len(b) else float("infinity")

            if aleft <= bright and bleft <= aright:

                if total % 2:
                    return min(aright, bright)
                return (max(aleft, bleft) + min(aright, bright)) / 2
            
            elif aleft > bright:
                r = m - 1
            
            else:
                l = m + 1
