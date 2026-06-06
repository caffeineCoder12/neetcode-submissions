class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {')':'(', ']':'[', '}':'{'}
        for i in s:
            if i in d.keys():
                top = stack.pop() if stack else '#'
                if d[i] != top:
                    return False
            else:
                stack.append(i)
        return not stack