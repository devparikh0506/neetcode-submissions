# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1_digit  = l1
        l2_digit  = l2
        res_head = ListNode() 
        res_node = res_head
        carry = 0
        while l1_digit is not None or l2_digit is not None:
            d1 = l1_digit.val if l1_digit else 0
            d2 = l2_digit.val if l2_digit else 0

            acc = d1+d2+carry

            res = acc % 10
            carry = acc // 10

            res_node.next = ListNode(res)
            res_node = res_node.next
            
            if l1_digit:
                l1_digit = l1_digit.next
            if l2_digit:
                l2_digit = l2_digit.next
        
        if carry > 0:
            res_node.next = ListNode(carry)
        return res_head.next
            


