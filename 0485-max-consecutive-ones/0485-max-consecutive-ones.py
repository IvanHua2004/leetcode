class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maximum = 0
        currentCount = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                currentCount += 1
            else:
                currentCount = 0
            maximum = max(maximum, currentCount)
        return maximum