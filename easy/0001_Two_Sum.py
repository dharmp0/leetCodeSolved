class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            checked = {}
            
            for idx, num in enumerate(nums):
                
                add = target - num
                

                if add in checked:
                    
                    return[idx, checked[add]]

                checked[num] = idx
