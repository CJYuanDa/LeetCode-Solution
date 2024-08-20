/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode(int x) {
 * val = x;
 * next = null;
 * }
 * }
 */

public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode link1 = headA;
        ListNode link2 = headB;

        while (link1 != link2) {
            link1 = link1 != null ? link1.next : headB;
            link2 = link2 != null ? link2.next : headA;
        }

        return link1;

    }

    public class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
            next = null;
        }
    }
}