class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: List[Optional[ListNode]]
        """
        # Step 1: Count total number of nodes
        total_length = 0
        current = head
        while current:
            total_length += 1
            current = current.next
        
        # Step 2: Determine the size of each part and the remainder
        part_size = total_length // k
        remainder = total_length % k
        
        result = []
        current = head
        
        for i in range(k):
            part_head = current
            size = part_size + (1 if remainder > 0 else 0)
            remainder -= 1 if remainder > 0 else 0
            
            # Traverse the current part to its end
            for j in range(size - 1):
                if current:
                    current = current.next
            
            # Cut the list and move to the next part
            if current:
                next_part = current.next
                current.next = None
                current = next_part
            
            result.append(part_head)
        
        return result
