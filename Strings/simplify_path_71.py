class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for val in [val for val in path.split("/") if val != ""]:
            if val == ".": continue
            elif val == "..":
                if len(stack): 
                    stack.pop()
            else: stack.append(val)
        return "/" + "/".join(stack)
