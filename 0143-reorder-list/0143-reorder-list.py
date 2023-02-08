# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        end = slow.next
        slow.next = None
        prev = None
        while end:
            temp = end.next
            end.next = prev
            prev = end
            end = temp
        
        first, second = head, prev
        while second:
            tmp,tmp2 = first.next,second.next
            first.next = second
            second.next = tmp
            first = tmp
            second = tmp2
        

