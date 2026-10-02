import math
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        res = [nums[:]]

        for _ in range(math.factorial(len(nums))-1):
            i = len(nums) - 2
            while i >= 0 and nums[i] >= nums[i+1]:
                i -= 1
            
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            
            nums[i], nums[j] = nums[j], nums[i]
            nums[i+1:] = reversed(nums[i+1:])
            res.append(nums[:])
        return res