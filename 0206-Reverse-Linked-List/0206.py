# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        prev = None
        while head:
            temp_next = head.next
            head.next = prev
            prev = head
            head = temp_next
        
        return prev