class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        right = 0
        largest = 0
        substr = ""

        while right < len(s):

            if s[right] not in substr:
                substr += s[right]
            
            elif s[right] in substr:
                
                while s[right] in substr:

                    left += 1
                    substr = substr[1:]
                
                substr += s[right]
            
            right += 1

            if right - left > largest:

                largest = right - left

        return largest
