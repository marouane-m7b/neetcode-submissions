class Solution:
    def isValid(self, s: str) -> bool:
        sArray = s.split()
        stack = []
        for i in s:
            if (i == '('):
                stack.append(')')
            elif (i == '{'):
                stack.append('}')
            elif (i == '['):
                stack.append(']')
            elif(stack.pop() != i):
                return False


        return len(stack) == 0