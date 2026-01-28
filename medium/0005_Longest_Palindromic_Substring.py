class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        n = len(s)
        best_r, best_l = 0, 0
        
        def expand(l: int, r: int):
            nonlocal best_r, best_l
            while l >=0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            if r - l > best_r - best_l:
                best_r, best_l = r, l
        
        for i in range(n):
            expand(i, i)
            expand(i, i +1)
        
        return s[best_l:best_r+1]
