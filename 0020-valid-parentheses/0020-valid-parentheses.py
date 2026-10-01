class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if not stack:
                    return False
                res = stack.pop()

                if char != ")" and res == "(":
                    return False
                elif char != "}" and res == "{":
                    return False
                elif char != "]" and res == "]":
                    return False
        return len(stack) == 0