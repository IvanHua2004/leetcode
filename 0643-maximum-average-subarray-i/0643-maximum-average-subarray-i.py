class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        total = 0
        last = 0
        for i in range(k):
            total += nums[i]

        current = total
        for i in range(k, len(nums)):
            current = current - nums[last] + nums[i]
            total = max(total, current)
            last += 1

        return total/k

        