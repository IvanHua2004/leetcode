class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = [0] * (2*n)
        index = 0
        for num in nums[:n]:
            res[index] = num
            index += 2

        index = 1
        for num in nums[n:2*n]:
            res[index] = num
            index += 2
        
        return res

