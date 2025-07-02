class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        left = 0
        right = 0
        longest = 0

        while right < len(nums):

            if nums[right] == 1:
                right +=1
            
            elif nums[right] == 0:
                k -= 1
                if k >= 0:
                    right += 1
                
                else:

                    while k < 0:

                        if nums[left] == 0:
                            right+=1
                            k+=1
                        left+=1
            
            if longest < right - left:
                longest = right - left

        return longest
