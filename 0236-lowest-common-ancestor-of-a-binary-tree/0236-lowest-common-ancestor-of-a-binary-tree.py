# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def LCA(root,p,q):
            if not root or root==p or root==q:
                return root # stoping recursive calls if we find either p or q
            left=LCA(root.left,p,q)
            right=LCA(root.right,p,q)
            if not left:
                return right
            elif not right:
                return left
            else:
                return root # if both left and right are there that means that's the LCA
        return LCA(root,p,q)
        