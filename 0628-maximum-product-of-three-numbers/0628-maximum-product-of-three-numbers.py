class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        arr = sorted(nums)
        first = arr[0]*arr[1]*arr[2]
        second = arr[0]*arr[1]*arr[-1]
        third = arr[0]*arr[-1]*arr[-2]
        fourth = arr[-1]*arr[-2]*arr[-3]

        return max([first, second, third, fourth])