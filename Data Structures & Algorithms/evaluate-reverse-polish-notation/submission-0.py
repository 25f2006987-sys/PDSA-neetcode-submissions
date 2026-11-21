class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st1 = []
        for token in tokens:
            if token == '+':
                st1.append(st1.pop() + st1.pop())
            elif token == '-':
                b = st1.pop()
                a = st1.pop()
                st1.append(a - b)
            elif token == '*':
                st1.append(st1.pop() * st1.pop())
            elif token == '/':
                b = st1.pop()
                a = st1.pop()
                st1.append(int(a / b))
            else:
                st1.append(int(token))
        return st1[0]