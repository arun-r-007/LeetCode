# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        while curr and curr.next:
            g = self.gcd(curr.val, curr.next.val)

            new_node = ListNode(g)
            new_node.next = curr.next
            curr.next = new_node

            curr = new_node.next

        return head
















































# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution(object):

#     def gcd(self, a, b):
#         while b:
#             a, b = b, a % b
#         return a

#     def insertGreatestCommonDivisors(self, head):
#         """
#         :type head: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         if head.next is None:
#             return head

#         ls = []
#         ls1 = []
#         current = head
#         while current is not None :
#             ls.append(current.val)
#             current = current.next

#         n = len(ls)

#         for i in range(n-1):
#             g = self.gcd(ls[i], ls[i+1])
#             ls1.append(ls[i])
#             ls1.append(g)

#         ls1.append(ls[-1])

#         dummy = ListNode(0)
#         current = dummy
#         for val in ls1:
#             current.next = ListNode(val)
#             current = current.next

#         return dummy.next