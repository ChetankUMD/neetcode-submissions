class Solution:
    def isValid(self, s: str) -> bool:
        if s == "" or len(s) % 2 != 0:
            return False
        st = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                st.append(c)
                continue
            if not st:
                return False
            if c == ')' and st[-1] == '(':
                st.pop()
            elif c == '}' and st[-1] == '{':
                st.pop()
            elif c == ']' and st[-1] == '[':
                st.pop()
            else:
                return False
        if not st:
            return True
        else:
            return False