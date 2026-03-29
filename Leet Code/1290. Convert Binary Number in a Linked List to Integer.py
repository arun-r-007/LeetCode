# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        if head.next is None:
            return head.val

        current = head
        string = ""

        while current :
            string += str(current.val)
            current = current.next


        return int(string,2)