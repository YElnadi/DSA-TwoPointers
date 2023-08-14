from collections import deque


class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


a = TreeNode(4)
b = TreeNode(2)
c = TreeNode(7)
d = TreeNode(1)
e = TreeNode(3)
f = TreeNode(6)
g = TreeNode(9)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g


#        4
#      /   \
#     2     7
#   /  \    / \
#  1    3   6  9

class Solution:
    def invertTree(self, root):
        if not root:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.right)
                queue.append(node.left)

        return root


