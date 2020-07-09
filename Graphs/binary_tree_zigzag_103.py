# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [root]
        res = []
        while len(queue) and root:
            size = len(queue)
            res.append([node.val for node in queue])
            for _ in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        for i in range(len(res)):
            if i % 2 == 1:
                res[i] = res[i][::-1]
        return res
