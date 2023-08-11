# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

def isPalindrome(s):
        s_lst = ''.join(s.split()).lower()
        print(s_lst)
        new_str = ''
        print(s_lst)
        for char in s_lst:
                if char.isalnum():
                        new_str=new_str+char
        
        print()
        reversed_str = new_str[::-1]
        return new_str == reversed_str
                




print(isPalindrome("0P"))