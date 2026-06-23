# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        depx=[-1]
        depy=[-1]
        parx=[None]
        pary=[None]
        def check(root,parent,depth):
            if not root:
                return
            if root.val==x:
                depx[0],parx[0]=depth,parent
            if root.val==y:
                depy[0],pary[0]=depth,parent
            check(root.left,root,depth+1)
            check(root.right,root,depth+1)
        check(root,None,0)
        return depx[0]==depy[0] and parx[0]!=pary[0]