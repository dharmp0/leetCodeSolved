class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if s[i] == '*':
                stack.pop()
            else:
                stack.append(s[i])
            i +=1
        return ''.join(stack)
