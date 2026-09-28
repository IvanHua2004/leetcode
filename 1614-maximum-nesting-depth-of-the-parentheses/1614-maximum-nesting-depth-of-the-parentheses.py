class Solution:
    def maxDepth(self, s: str) -> int:
        max1 = 0
        count = 0
        stack = []
        for char in s:
            if char == "(":
                stack.append("(")
                count += 1
                max1 = max(count, max1)
            elif char == ")":
                stack.pop()
                count -= 1
                if not stack:
                    count = 0
            
        return max1
            