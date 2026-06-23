# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def check(root,count):
            if not root:
                return False
            count+=root.val
            if not root.left and not root.right:
                return count==targetSum
            return check(root.left,count) or check(root.right,count)
        return check(root,0)
        