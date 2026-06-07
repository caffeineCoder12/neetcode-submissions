class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        vals = []
        for c in tokens:
            if c == '+':
                vals.append(vals.pop()+vals.pop())
            elif c == '-':
                a,b = vals.pop(),vals.pop()
                vals.append(b-a)
            elif c == '*':
                vals.append(vals.pop()*vals.pop())
            elif c == '/':
                a,b = vals.pop(),vals.pop()
                vals.append(int(b/a))
            else:
                vals.append(int(c))
        return int(vals[0])