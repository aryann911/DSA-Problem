# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        temp=ListNode(0)
        curr=temp
        carr=0
        while l1 != None or l2 != None or carr>0:
            v1=l1.val if l1 is not None else 0
            v2=l2.val if l2 is not None else 0

            sums=v1+v2+carr
            digit=sums%10
            carr=sums//10

            curr.next=ListNode(digit)
            curr=curr.next

            if l1 is not None:
                l1=l1.next
            if l2 is not None:
                l2=l2.next
        return temp.next


        