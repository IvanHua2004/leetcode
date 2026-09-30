class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hashmap1 = {}
        res = []
        for num in nums1:
            if num not in hashmap1:
                hashmap1[num] = 1
            else:
                hashmap1[num] += 1
        
        hashmap2 = {}
        for num in nums2:
            if num not in hashmap2:
                hashmap2[num] = 1
            else:
                hashmap2[num] += 1

        for key, value in hashmap1.items():
            if key in hashmap2:
                if hashmap2[key] == 0:
                    continue
                hashmap2[key] -= 1
                res.append(key)
        return res