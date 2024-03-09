class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        t1 = {}

        for char in s:
            if char not in s1:
                s1[char] = 0
            s1[char] += 1

        for char in t:
            if char not in t1:
                t1[char] = 0
            t1[char] += 1

        return s1 == t1 
