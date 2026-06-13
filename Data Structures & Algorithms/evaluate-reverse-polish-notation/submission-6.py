class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        op = ['+', '-', '*', '/']
        for c in tokens:
            if c in op:
                a = int(st[-1])
                st.pop()
                b = int(st[-1])
                st.pop()
                res = 0
                if c == '+':
                    res = a + b 
                elif c == '-':
                    res = b-a
                elif c == '*':
                    res= a * b
                elif c == '/':
                    res = b/a
                st.append(res)
            else:
                st.append(c)
        
        return int(st[-1])


