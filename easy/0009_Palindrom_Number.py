class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_int = str(x)

        if str_int == str_int[::-1]:
            return True
        else:
            return False
