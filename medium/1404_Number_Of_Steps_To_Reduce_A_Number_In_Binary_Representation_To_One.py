class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        s = s[::-1]

        for i in s[:-1]:

            if (i == '0' and carry == 0) or (i == '1' and carry == 1):
                steps += 1

            elif i == '0' and carry == 1:
                steps += 2

            elif i == '1' and carry == 0:
                steps += 2
                carry = 1
        
        if carry == 1:
            steps += 1

        return steps
