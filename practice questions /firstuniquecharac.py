class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict = {}
        for index, char in enumerate(s):
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1

        # char_dict = {l:1, e:3, t:1, c:1, 0:1, d:1}
        print(char_dict)
        res = list(key for key, value in char_dict.items() if value == 1) 
        print(res)
        if res:
            return s.index(res[0])
        else:
            return -1


        # res = [l, t,c, o, d]
