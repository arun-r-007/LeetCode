# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if not head or not head.next:
            return head

        odd_dummy = ListNode(0)
        even_dummy = ListNode(0)
        
        odd_tail = odd_dummy
        even_tail = even_dummy
        
        current = head
        pos = 1
        
        while current:
            if pos % 2 != 0:
                odd_tail.next = current
                odd_tail = odd_tail.next
            else: 
                even_tail.next = current
                even_tail = even_tail.next
            current = current.next
            pos += 1
        
        even_tail.next = None 
        odd_tail.next = even_dummy.next 
        
        return odd_dummy.next