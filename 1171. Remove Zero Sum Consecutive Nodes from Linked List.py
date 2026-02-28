# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Step 1: Convert linked list to array
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        # Step 2: Remove zero sum subarrays using stack
        stack = []
        
        for num in arr:
            stack.append(num)
            
            # Check if any ending subarray sums to 0
            total = 0
            for i in range(len(stack) - 1, -1, -1):
                total += stack[i]
                if total == 0:
                    # Remove that zero sum part
                    stack = stack[:i]
                    break
        
        # Step 3: Convert stack back to linked list
        dummy = ListNode(0)
        curr = dummy
        
        for num in stack:
            curr.next = ListNode(num)
            curr = curr.next
        
        return dummy.next