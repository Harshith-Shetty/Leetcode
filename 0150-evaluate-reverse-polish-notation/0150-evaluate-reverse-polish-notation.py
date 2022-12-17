class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []                                                     
        for s in tokens:                                        
            if s not in '/+-*':
                stack.append(int(s))
            else:
                num = stack.pop()
                if   s == '+':
                    stack[-1]+=  num
                elif s == '-':
                    stack[-1]-=  num
                elif s == '*':
                    stack[-1]*=  num
                else:
                    stack[-1]= int(stack[-1]/num)
        return stack[0]