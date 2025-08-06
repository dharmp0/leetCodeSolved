class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        potions.sort()
        pairs = []

        for n in spells:
            
            low = 0
            high = len(potions)-1

            while low <= high:

                mid = (low+high)//2

                if n*potions[mid] >= success:
                   
                    high = mid - 1

                elif n*potions[mid] < success:
                    low = mid + 1
                
            pairs.append(len(potions)-low)
        
        return pairs
