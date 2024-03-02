class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_x = str(x)
        reversed_x = string_x[::-1]
        return reversed_x == string_x