class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
        stack = []
        index = 0
        for push in pushed:
            stack.append(push)
            while len(stack) > 0 and popped[index] == stack[len(stack)-1]:
                stack.pop()
                index += 1
        return len(stack) == 0
