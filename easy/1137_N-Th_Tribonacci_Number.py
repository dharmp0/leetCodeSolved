class Solution:
    def tribonacci(self, n: int) -> int:
        dic = {0: 0, 1: 1, 2: 1}
        
        def dp(n: int) -> int:
            if n in dic:
                return dic[n]
            
            dic[n] = dp(n-1) + dp(n-2) + dp(n-3)

            return dic[n]
        
        return dp(n)
