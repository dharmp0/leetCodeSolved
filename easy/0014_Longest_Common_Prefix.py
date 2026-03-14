class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""

        shortest = min(len(s) for s in strs)

        for i in range(shortest):
            char = strs[0][i]

            for s in strs[1:]:
                if s[i] != char:
                    return strs[0][:i]

        return strs[0][:shortest]
