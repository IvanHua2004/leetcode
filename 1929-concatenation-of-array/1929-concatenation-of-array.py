class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        res = [0] * (len(nums)*2)
        for i, num in enumerate(nums):
            res[i] = nums[i]
            res[i+len(nums)] = nums[i]
        return res