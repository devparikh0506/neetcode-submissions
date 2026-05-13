# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow = head
        fast  = head

        if fast is None:
            return False
        if fast.next == slow :
            return True
        if fast.next is None:
            return False
        fast  = fast.next.next 

        while fast is not None and fast.next is not None and slow is not None:
            if fast==slow:
                return True
            fast = fast.next.next
            slow = slow.next
        
        return False