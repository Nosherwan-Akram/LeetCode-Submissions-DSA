class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        - var stack
        - loop over tokens
        - if number push in stack
        - if operand check last 2 items in stack, pop them, and apply it to them
        - push result in stack
        - return stack element (only 1 must remain)
        '''
        stack = []
        for ele in tokens:
            if ele == '+' or ele == '-' or ele == '*' or ele == '/':
                num2 = stack.pop()
                num1 = stack.pop()
                if ele == '+':
                    newNum = num1 + num2
                elif ele == '-':
                    newNum = num1 - num2
                elif ele == '*':
                    newNum = num1 * num2
                else:
                    newNum = num1 / num2
                stack.append(int(newNum))
            else:
                stack.append(int(ele))
        return stack.pop()