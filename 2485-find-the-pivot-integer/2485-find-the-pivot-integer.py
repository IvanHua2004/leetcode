class Solution:
    def pivotInteger(self, n: int) -> int:
        left = 1
        right = n
        totalLeft = 1
        totalRight = n

        while left < right:
            if totalLeft < totalRight:
                left += 1
                totalLeft += left
            else:
                right -= 1
                totalRight += right
        
        return left if totalLeft == totalRight else -1
        

