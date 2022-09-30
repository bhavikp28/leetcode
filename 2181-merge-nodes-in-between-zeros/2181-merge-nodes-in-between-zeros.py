# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        temp = head.next
        check = None
        total = 0
        while temp:
            if temp.val != 0:
                total += temp.val
                temp = temp.next
            elif temp.val == 0:
                curr.val = total
                curr.next = temp
                check = curr
                curr = curr.next
                temp = temp.next
                total = 0
        check.next = None
        return head