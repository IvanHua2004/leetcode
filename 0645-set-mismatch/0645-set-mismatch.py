class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        dup = -1
        find = set()
        for num in nums:
            if num not in find:
                find.add(num)
            else:
                dup = num
                break
        
        expectedSum = (len(nums) * (len(nums)+1))//2
        actualSum = sum(nums)
        missing = expectedSum - actualSum + dup
        return [dup, missing]