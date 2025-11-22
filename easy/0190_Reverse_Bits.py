class Solution:
    def reverseBits(self, n: int) -> int:
        return int(str(format(n, '032b'))[::-1],2)
