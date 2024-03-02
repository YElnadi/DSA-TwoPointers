class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #### sorting approach
        # for i in range(n):
        #     nums1[i+m] = nums2[i]

        # nums1.sort()

        ######
        nums1Copy = nums1[:m]
        p1 = m -1
        p2 = n -1
        p_merged = m + n -1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p_merged] = nums1[p1]
                p1 -= 1
            else:
                nums1[p_merged] = nums2[p2]
                p2 -= 1
            p_merged -= 1

        while p2>=0:
            nums1[p_merged] = nums2[p2]
            p2 -= 1
            p_merged  -= 1