class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in operations:
            if i.isdigit() or (i[0] == '-' and i[1:].isdigit()):
                stack.append(int(i))
            else:
                if i=='C':
                    stack.pop()
                if i=="D":
                    stack.append(2 * stack[-1])
                if i=='+':
                    stack.append(stack[-1] + stack[-2]) 
            

       
        return sum(stack)
        
