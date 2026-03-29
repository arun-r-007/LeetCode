'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def removeLastNode(self, head):
        # code here
        current = head
        
        while current.next and current.next.next:
            current = current.next
            
        current.next = None
        
        return head