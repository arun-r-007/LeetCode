# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA: ListNode
        :type headB: ListNode
        :rtype: ListNode
        """

        a=headA 
        b=headB
        while a!=b:
            a=a.next if a else headB
            b=b.next if b else headA
        return a




















# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def getIntersectionNode(self, headA, headB):
#         """
#         :type headA: ListNode
#         :type headB: ListNode
#         :rtype: ListNode
#         """

#         if not headA or not headB:
#             return None

#         ptrA = headA
#         ptrB = headB

#         while ptrA != ptrB:
#             ptrA = ptrA.next if ptrA else headB
#             ptrB = ptrB.next if ptrB else headA

#         return ptrA