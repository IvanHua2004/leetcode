class Solution:
    def isPalindrome(self, x: int) -> bool:
        value = str(x)
        for i in range(len(value)//2):
            if value[i] != value[-(i+1)]:
                return False
        return True