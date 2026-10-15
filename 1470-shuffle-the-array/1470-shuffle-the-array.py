class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = [0] * (n*2)
        for i, num in enumerate(nums[:n]):
            res[i*2] = num
        
        for i, num in enumerate(nums[n:n*2]):
            res[i*2+1] = num

        return res


