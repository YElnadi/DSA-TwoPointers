# # You are given two strings - pattern and source. The first string pattern contains only the symbols 0 and 1, and the second string source contains only lowercase English letters.

# # Let's say that pattern matches a substring source[l..r] of source if the following three conditions are met:

# # they have equal length,
# # for each 0 in pattern the corresponding letter in the substring is a vowel,
# # for each 1 in pattern the corresponding letter is a consonant.
# # Your task is to calculate the number of substrings of source that match pattern.

# # Note: In this task we define the vowels as 'a', 'e', 'i', 'o', 'u', and 'y'. All other letters are consonants.


#############################################################################
# def pattern_finder(pattern, source):
#     vowels = 'aeiouy'
#     l = 0
#     r = len(pattern)
#     count = 0
#     while r<=len(source):
#         substring = source[l:r]
#         is_matching = True
#         for i, char in enumerate(substring):
#             if pattern[i] == '0' and char not in vowels:
#                 is_matching = False
#                 break
#             if pattern[i] =='1' and char in vowels:
#                 is_matching = False
#                 break
#         if is_matching:
#             count += 1
#         l+=1
#         r+=1

#     return count
# print(pattern_finder('010', 'Yasmine'))
#############################################################################


# Given an array of integers a, your task is to find how many of its contiguous subarrays of length m contain a pair of integers with a sum equal to k.

# More formally, given the array a, your task is to count the number of indices 0 ≤ i ≤ a.length - m such that a subarray [a[i], a[i + 1], ..., a[i + m - 1]] contains at least one pair (a[s], a[t]), where:

# s ≠ t
# a[s] + a[t] = k
# Example

# For a = [2, 4, 7, 5, 3, 5, 8, 5, 1, 7], m = 4, and k = 10, the output should be solution(a, m, k) = 5.

# Let's consider all subarrays of length m = 4 and see which fit the description conditions:

# Subarray a[0..3] = [2, 4, 7, 5] doesn't contain any pair of integers with a sum of k = 10. Note that although the pair (a[3], a[3]) has the sum 5 + 5 = 10, it doesn't fit the requirement s ≠ t.
# Subarray a[1..4] = [4, 7, 5, 3] contains the pair (a[2], a[4]), where a[2] + a[4] = 7 + 3 = 10.
# Subarray a[2..5] = [7, 5, 3, 5] contains two pairs (a[2], a[4]) and (a[3], a[5]), both with a sum of k = 10.
# Subarray a[3..6] = [5, 3, 5, 8] contains the pair (a[3], a[5]), where a[3] + a[5] = 5 + 5 = 10.
# Subarray a[4..7] = [3, 5, 8, 5] contains the pair (a[5], a[7]), where a[5] + a[7] = 5 + 5 = 10.
# Subarray a[5..8] = [5, 8, 5, 1] contains the pair (a[5], a[7]), where a[5] + a[7] = 5 + 5 = 10.
# Subarray a[6..9] = [8, 5, 1, 7] doesn't contain any pair with a sum of k = 10.
# So the answer is 5, because there are 5 contiguous subarrays that contain a pair with a sum of k = 10.

# For a = [15, 8, 8, 2, 6, 4, 1, 7], m = 2, and k = 8, the output should be solution(a, m, k) = 2.

# There are 2 subarrays satisfying the description conditions:

# a[3..4] = [2, 6], where 2 + 6 = 8
# a[6..7] = [1, 7], where 1 + 7 = 8
# Input/Output

# [execution time limit] 4 seconds (py3)

# [memory limit] 1 GB

# [input] array.integer a

# The given array of integers.

# Guaranteed constraints:
# 2 ≤ a.length ≤ 105,
# 0 ≤ a[i] ≤ 109.

# [input] integer m

# An integer representing the length of the contiguous subarrays being considered.

# Guaranteed constraints:
# 2 ≤ m ≤ a.length.

# [input] integer k

# An non-negative integer value representing the sum of the pairs we're trying to find within each subarray.

# Guaranteed constraints:
# 0 ≤ k ≤ 109.

# [output] integer

# An integer representing the number of subarrays that contain a pair of integers with a sum of k.

###################################################

# def find_pair(a, m, k):
#     count = 0
#     for l in range(len(a) - m + 1):
#         subArr = a[l:l+m]
#         sorted_subArr = sorted(subArr)
#         right = m - 1
#         left = 0
#         while left < right:
#             total = sorted_subArr[right] + sorted_subArr[left]
#             if total > k:
#                 right -= 1
#             elif total < k:
#                 left += 1
#             else:
#                 count += 1
#                 break
#     return count

################################################

# def solution (a, size):
#     n = len(a)
#     count = 0
#     a_extended = a + a[:size - 1]

#     for l in range(n):
#         subArr = a_extended[l:l + size]
#         is_alternating = True
#         for i in range(size-1):
#             if subArr[i] == subArr[i+1]:
#                 is_alternating = False
#                 break
#             if is_alternating:
#                 count += 1
#     return count


# print(solution([0, 1, 0, 1, 1], 3))


# xs = [()]
# res = [False] * 2
# print(res)

# if xs:
#     res[0] = True
# if xs[0]:
#     res[1] = True


# print(find_pair([2, 4, 7, 5, 3, 5, 8, 5, 1, 7], 4, 10))
# print(find_pair([15, 8, 8, 2, 6, 4, 1, 7], 2, 8))
class Solution:
    def isValid(self, s: str) -> bool:
       stack = []
       brackets = {')':'(', ']':'[', '}':'{'}
        for char in s:
            if char in '({[':
                stack.append(char)
            if char in ')}]':
                if stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    return False
        return not stack
                    