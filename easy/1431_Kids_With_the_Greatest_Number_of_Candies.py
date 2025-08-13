class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        ans = []
        
        for i in candies:
            
            if i + extraCandies >= greatest:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans
