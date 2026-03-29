# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        if head is None or left == right:
            return head

        current = head
        position = 1
        ls = []
        
        left_node = None
        right_node = None
        
        while current:
            if position == left:
                left_node = current
            if left_node:
                ls.append(current.val)
            if position == right:
                right_node = current
                break
            current = current.next
            position += 1
        
        ls.reverse()
        
        current = left_node
        for val in ls:
            current.val = val
            current = current.next
        
        return head




















def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Example call
if __name__ == "__main__":
    # Linked list values
    list_values = [1, 2, 3, 4, 5]
    left = 2
    right = 4

    # Create linked list
    head = create_linked_list(list_values)
    # c = head
    # while c :
    #     print(c.val)
    #     c = c.next

    # Create Solution object and call the method
    solution = Solution()
    w = solution.reverseBetween(head, left, right)
    
    while w :
        print(w.val)
        w = w.next