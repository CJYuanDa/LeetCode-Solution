# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool: # type: ignore
        val_list = []

        while head:
            val_list.append(head.val)
            head = head.next
        
        L = 0
        R = len(val_list) - 1

        while L < R:
            if val_list[L] != val_list[R]:
                return False
            L += 1
            R -= 1
        
        return True

    def isPalindrome1(self, head: Optional[ListNode]) -> bool: # type: ignore
        slow = head
        fast = head

        # to find the mid point of the linked list -> slow = mid point
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse the linked list start from the mid point
        # 5 -> 6 -> 7 -> null , null <- 5 <- 6 <- 7
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # prev -> the head (last) node of the reversed linked list
        L = head
        R = prev

        while R:
            if L.val != R.val:
                return False

            L = L.next
            R = R.next

        return True