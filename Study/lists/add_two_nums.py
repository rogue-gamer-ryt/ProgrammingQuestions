"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Link: https://leetcode.com/problems/add-two-numbers/
"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        carry, val = 0, 0
        dummy = ListNode()
        curr = dummy
        while curr1 or curr2 or carry:
            v1 = curr1.val if curr1 else 0
            v2 = curr2.val if curr2 else 0

            total = carry + v1 + v2
            carry = total // 10
            val = total % 10
            curr.next = ListNode(val)

            curr = curr.next
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None

        return dummy.next