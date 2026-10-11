class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        res = []
        for i in range(len(nums)):
            if len(nums) % (i+1) == 0:
                res.append(nums[i])
        
        total = sum([x**2 for x in res])
        return total