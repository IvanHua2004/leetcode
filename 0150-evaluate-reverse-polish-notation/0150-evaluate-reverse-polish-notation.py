class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                first = int(stack.pop())
                second = int(stack.pop())

                match token:
                    case "+":
                        stack.append(first + second)
                    case "-":
                        stack.append(second - first)
                    case "*":
                        stack.append(second * first)
                    case "/":
                        stack.append(second / first)
            else:
                stack.append(token)

        return int(stack[0])

