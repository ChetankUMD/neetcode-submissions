class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        if s=="" or len(s)%2 !=0:
            return False

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                st.append(s[i])
            else:
                if not st:
                    return False
                if s[i] == ')' and '(' == st[-1]:
                    st.pop()
                elif s[i] == '}' and '{'== st[-1]:
                    st.pop()
                elif s[i] == ']' and '[' == st[-1]:
                    st.pop()
                else:
                    return False
        if not st:
            return True
        return False