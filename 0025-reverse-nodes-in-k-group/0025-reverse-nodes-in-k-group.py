# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def rev_node(node):
            prev=None
            while node:
                nxt=node.next
                node.next=prev
                prev=node
                node=nxt
            return prev
        
        def lastnode(node):
            tmp=node
            for _ in range(k-1):
                if not tmp:
                    return None 
                tmp=tmp.next
            return tmp
        prev_node=None
        temp=head
        while temp:
            last_node=lastnode(temp)
            if not last_node:
                break
            next_node=last_node.next
            last_node.next=None
            rev_node(temp)
            if temp==head:
                head=last_node
            if prev_node:
                prev_node.next=last_node
            temp.next=next_node
            prev_node=temp
            temp=next_node
        return head
        