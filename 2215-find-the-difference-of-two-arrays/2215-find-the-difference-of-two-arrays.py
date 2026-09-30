class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1 = set()
        set2 = set()
        res = [[],[]]

        for num in nums1:
            set1.add(num)

        for num in nums2:
            set2.add(num)

        for num in set1:
            if num not in set2:
                res[0].append(num)
        
        for num in set2:
            if num not in set1:
                res[1].append(num)

        return res