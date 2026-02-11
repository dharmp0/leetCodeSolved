class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()

        for j in range(len(nums)):
            
            if j > 0 and nums[j] == nums[j - 1]:
                continue

            l = j + 1
            r = len(nums) - 1

            while l < r:
                
                curr = nums[j] + nums[l] + nums[r]

                if curr == 0:
                    triplets.add(tuple([nums[l],nums[j],nums[r]]))
                    l += 1
                    r -= 1

                elif curr > 0:
                    r -= 1
                    
                else:
                    l += 1

        return [list(t) for t in triplets]
