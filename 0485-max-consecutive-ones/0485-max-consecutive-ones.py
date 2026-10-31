class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maximum = 0
        new = 0
        for i in range(len(nums)):
            if  nums[i] == 1:
                new += 1
                maximum = max(maximum, new)
            else:
                new = 0
        return maximum