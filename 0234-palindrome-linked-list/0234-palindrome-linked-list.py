# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev=None
        slow,fast=head,head
        while fast and fast.next:
            #move fast pointer 1st becoz we are reversing connections
            fast=fast.next.next
            nxt=slow.next
            slow.next=prev
            prev=slow
            slow=nxt
        
        if fast: #if LL of odd length
            first=prev
            second=slow.next

        else: #if LL of even length
            first=prev
            second=slow
        while first:
            if first.val!=second.val:
                return False
            first=first.next
            second=second.next
        return True
        