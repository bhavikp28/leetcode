# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = ''
        str2 = ''
        str3 = ''
        dummy = l1
        while dummy:
            str1 += str(dummy.val)
            dummy = dummy.next
        while l2:
            str2 += str(l2.val)
            l2 = l2.next
        str1 = str1[::-1]
        str2 = str2[::-1]
        str3 = int(str1)+int(str2)
        str3 = str(str3)
        str3 = str3[::-1]
        print(l1)
        
        ans = ListNode()
        cur = ans
        for i in str3:
            cur.next = ListNode(int(i))
            cur = cur.next
        return ans.next