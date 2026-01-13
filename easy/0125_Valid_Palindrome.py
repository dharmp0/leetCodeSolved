class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = ''.join(filter(str.isalnum, s)).lower()
        return cleaned_string == cleaned_string[::-1]
