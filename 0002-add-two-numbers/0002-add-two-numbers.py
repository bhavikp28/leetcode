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
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        car = 0
        while l1 or l2 or car > 0:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            val = v1+v2+car
            car = val//10
            val = val % 10
            cur.next = ListNode(val)
            
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        print(dummy)
        return dummy.next
'''