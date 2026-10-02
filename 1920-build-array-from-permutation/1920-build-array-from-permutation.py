class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        arr = [nums[i] for i in range(len(nums))]
        res = []

        for i in arr:
            res.append(nums[i])

        return res 