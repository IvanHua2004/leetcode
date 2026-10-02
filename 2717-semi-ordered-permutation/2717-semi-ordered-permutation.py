class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        maximum = None
        minimum = None
        for i in range(len(nums)):
            if nums[i] == len(nums):
                maximum = i
            elif nums[i] == 1:
                minimum = i
        
        value = minimum + (len(nums)-1 - maximum)
        return value if minimum < maximum else value - 1