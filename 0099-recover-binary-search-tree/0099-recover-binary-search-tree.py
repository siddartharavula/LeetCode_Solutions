# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first = [None]
        mid = [None]
        last = [None]
        prev = [None]
        def recover(root):
            if not root:
                return
            recover(root.left)
            if prev[0] and root.val<prev[0].val:
                if not first[0]:
                    first[0]=prev[0]
                    mid[0]=root
                else:
                    last[0]=root
            prev[0]=root
            recover(root.right)
        recover(root)
        if last[0]:
            first[0].val,last[0].val=last[0].val,first[0].val
        else:
            first[0].val,mid[0].val=mid[0].val,first[0].val

        """
        Do not return anything, modify root in-place instead.
        """
        