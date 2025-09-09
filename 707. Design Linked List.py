class MyLinkedList(object):

    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next
        

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        current = self
        for i in range(index):
            current = current.next
        return current.val
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        current = self
        new_node = MyLinkedList(val)
        new_node.next = current
        self = new_node
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        while self.next:
            self = self.next
        self.next = MyLinkedList(val)
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)