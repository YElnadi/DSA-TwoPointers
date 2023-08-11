class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        
        if not p or not q or p.val != q.val:
            return False
        
        return (self.isSameTree(p.right, q.right) and 
                self.isSameTree(p.left, q.left))
    


# Create TreeNode instances for [1, 2, 3]
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

# Create TreeNode instances for [1, 2, 3]
tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)

# Create a Solution instance
solution = Solution()

print(solution.isSameTree(tree1, tree2))