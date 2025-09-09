# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if head is None:
            return True
        
        ls = []
        current = head

        while current is not None:
            ls.append(current.val)
            current = current.next

        return ls == ls[::-1]