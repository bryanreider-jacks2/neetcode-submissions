class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for char in tokens:
            if char in "+-*/":
                b = stack.pop() 
                a = stack.pop()

                if char == "+":
                    res = a + b 
                elif char == "-":
                    res = a - b
                elif char == "*":   
                    res = a * b
                elif char == "/":
                    res = int(a / b)
                
                stack.append(res)   
            else:
                stack.append(int(char))
        return stack[-1]


