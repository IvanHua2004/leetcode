class Solution:
    def completePrime(self, num: int) -> bool:
        s = str(num)
        for i in range(1, len(s) + 1):
            if not self.isPrime(int(s[:i])):
                return False
        for i in range(len(s)):
            if not self.isPrime(int(s[i:])):
                return False
        return True

    def isPrime(self, n: int) -> bool:
        if n <= 1:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True