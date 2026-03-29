# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head.next is None:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next

        return head

















































# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution(object):
#     def deleteMiddle(self, head):
#         """
#         :type head: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """

#         if head.next is None :
#             head = None
#             return head

#         if head.next.next is None :
#             head.next = None
#             return head
        

#         current = head
#         ls = []

#         while current is not None :
#             ls.append(current.val)
#             current = current.next

#         n = len(ls)
#         target = ( n // 2 ) + 1 

#         prev = head
#         current = head

#         for i in range(1,target):
#             prev = current
#             current = current.next

#         prev.next = current.next

#         return head
        