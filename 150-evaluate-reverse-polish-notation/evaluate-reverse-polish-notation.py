class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                second, first = stack.pop(), stack.pop()
                stack.append(first - second)
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                second, first = stack.pop(), stack.pop()
                result = abs(first) // abs(second)

                if (first < 0) != (second < 0):
                    result = -result

                stack.append(result)
            else:
                stack.append(int(i))
        return stack[0]
