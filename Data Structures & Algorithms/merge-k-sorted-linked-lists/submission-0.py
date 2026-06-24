# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeTwoLists(self, list1 : Optional[ListNode], list2 :Optional[ListNode]):
        dummy = ListNode(float('-inf'))
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)

        if n < 1:
            return None

        for i in range(1, n):
            lists[i] = self.mergeTwoLists(lists[i], lists[i-1])
        return lists[-1]