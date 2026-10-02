class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for i in tokens:
            if i not in "+-*/":
                stack.append(i)
            else:
                first = int(stack.pop())
                second = int(stack.pop())

                match i:
                    case "+":
                        stack.append(first + second)
                    case "-":
                        stack.append(second - first)
                    case "*":
                        stack.append(first * second)
                    case "/":
                        stack.append(second / first)
        return int(stack.pop())