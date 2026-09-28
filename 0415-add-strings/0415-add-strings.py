class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        right = -1
        length1 = len(num1)
        length2 = len(num2)
        total = ""
        carry = 0
        while right >= -length1 or right >= -length2 or carry:
            digit1 = int(num1[right]) if right >= -length1 else 0
            digit2 = int(num2[right]) if right >= -length2 else 0
            value = digit1 + digit2 + carry
            carry = 0
            if value >= 10:
                carry = 1
                value -= 10
            total = str(value) + total
            right -= 1
        return total

                
