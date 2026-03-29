# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        one = head
        two = head

        while two and two.next:
            one = one.next
            two = two.next.next

            if one == two:
                return True

        return False























# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         if head == None or head.next == None :
#             return False

#         else :
#             lst = []

#             while head.next :
#                 if [head.val,head] in lst:
#                     return True
#                 lst.append([head.val,head])
#                 head = head.next

#             return False
