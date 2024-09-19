# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]: # type: ignore
        new_head = ListNode() # type: ignore
        tail = new_head

        while head:
            if head.val != val:
                tail.next = head
                tail = tail.next 
            head = head.next
        
        # if the last node.val == val
        if tail.next and tail.next.val == val:
            tail.next = None

        return new_head.next