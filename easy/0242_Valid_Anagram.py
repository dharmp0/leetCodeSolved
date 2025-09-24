class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}

        for i in s:
            freq[i] = freq.get(i, 0) + 1
        
        for n in t:
            if n not in freq:
                return False
            freq[n] -= 1
            if freq[n] == 0:
                del freq[n]
        
        return len(freq) == 0
