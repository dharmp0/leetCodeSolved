class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
        
        return ''.join(result)
