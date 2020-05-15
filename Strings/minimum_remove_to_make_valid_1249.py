class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        counter = 0
        s = list(s)
        for i, c in enumerate(s):
            if c == '(': counter += 1
            elif c == ')':
                if not counter: s[i] = ""
                else: counter -= 1
        for i in range(len(s)-1, -1, -1):
            if not counter: break
            if s[i] == '(': 
                s[i] = ""
                counter -= 1
        return "".join(s)
