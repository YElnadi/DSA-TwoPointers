from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root:TreeNode) -> int:
        if not root:
            return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        #BF
        # queue = deque([root])
        # level = 0

        # while queue:
        #     for i in range(len(queue)):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)

        #         if node.right:
        #             queue.append(node.right)
        #     level += 1

           

        # return level

        #DF

        stack = [[root, 1]]
        res = 1

        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.right, depth+1])
                stack.append([node.left, depth+1])

        return res



    
a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)

a.left = b
a.right = c 
c.left = d
c.right = e



# Create a Solution instance
solution = Solution()

print(solution.maxDepth(a))