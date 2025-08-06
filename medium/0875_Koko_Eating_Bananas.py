from math import ceil 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)


        while low <= high:
            time = 0
            k = (low + high) // 2
            
            for i in piles:

                time += ceil(i/k)

            if time>h:

                low = k + 1
            
            elif time<=h:

                high = k - 1
        
        return low
