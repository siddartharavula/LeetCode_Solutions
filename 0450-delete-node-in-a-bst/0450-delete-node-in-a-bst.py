# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(root,key):
            if not root:
                return 
            if key<root.val:
                root.left=delete(root.left,key)
            elif key>root.val:
                root.right=delete(root.right,key)
            else: # if key found
                if not root.left:
                    return root.right # if left tree is absent then return right tree
                if not root.right:
                    return root.left # if right tree is absent then return left tree

                # if node have both left and right trees then find least node at right of note and
                # assin it to the node and eventually delete that least node at right side 
                temp=root.right
                while temp.left:
                    temp=temp.left
                root.val=temp.val
                root.right=delete(root.right,temp.val)
            return root
        return delete(root,key)