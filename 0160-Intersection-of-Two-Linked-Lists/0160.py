# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]: # type: ignore
        link1 = headA
        link2 = headB

        while link1 != link2:
            
            if link1:
                link1 = link1.next
            else:
                link1 = headB
            
            if link2:
                link2 = link2.next
            else:
                link2 = headA

        return link1
            


        