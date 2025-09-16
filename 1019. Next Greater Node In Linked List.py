# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        ls = []
        current = head
        while current:
            ls.append(current.val)
            current = current.next
        
        result = [0] * len(ls)
        stack = []  # stack holds indices
        
        for i, value in enumerate(ls):
            while stack and ls[stack[-1]] < value:
                index = stack.pop()
                result[index] = value
            stack.append(i)
        
        return result
    
    