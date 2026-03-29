'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteNode(self, head, x):
        # Empty list
        if head is None:
            return None
        
        # If first node is to be deleted
        if x == 1:
            return head.next
        
        current = head
        prev = None
        count = 1
        
        while current and count < x:
            prev = current
            current = current.next
            count += 1
        
        if current:
            prev.next = current.next
        
        return head