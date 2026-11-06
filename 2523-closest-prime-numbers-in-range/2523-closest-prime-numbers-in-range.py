import math

class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        prev = -1
        ans = [-1, -1]
        best = float('inf')

        for num in range(left, right + 1):
            if self.isPrime(num):
                if prev != -1 and num - prev < best:
                    best = num - prev
                    ans = [prev, num]
                    if best <= 2:    
                        return ans
                prev = num
        return ans

    def isPrime(self, number):
        if number <= 1:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for i in range(3, math.isqrt(number) + 1, 2):
            if number % i == 0:
                return False
        return True