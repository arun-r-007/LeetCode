class Solution(object):
    def numComponents(self, head, nums):
        nums_set = set(nums)
        freq = 0
        current = head
        in_component = False
        
        while current:
            if current.val in nums_set:
                if not in_component:
                    freq += 1
                    in_component = True
            else:
                in_component = False
            current = current.next
        
        return freq

































# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def numComponents(self, head, nums):
#         """
#         :type head: Optional[ListNode]
#         :type nums: List[int]
#         :rtype: int
#         """
#         if nums == []:
#             return 0

#         ls = []
#         freq = 0
#         current  = head
#         while current is not None:
#             ls.append(current.val)
#             # print("after append",ls)

#             if len(ls) == 2:
#                 # print("after len = 2 :",ls)
#                 if len(nums) == 1 :
#                     freq+=1
#                     return freq

#                 elif ls[0] in nums and ls[1] in nums:
#                     # print("Found in nums",ls,nums)
                    
#                     nums.remove(ls[0])
#                     nums.remove(ls[1])
#                     ls.clear()

#                     # print("after pop",ls)
#                     freq += 1
#                 else:
#                     # print("NotFound in nums",ls,nums)
#                     ls.pop(0)
#                     # print("after pop",ls)

#             current = current.next 

#         return freq


# def create_linked_list(values):
#     if not values:
#         return None
#     head = ListNode(values[0])
#     current = head
#     for val in values[1:]:
#         current.next = ListNode(val)
#         current = current.next
#     return head

# # Example call
# if __name__ == "__main__":
#     # Linked list values
#     list_values = [0, 1, 2, 3, 4]
#     nums = [0, 3, 1, 4]

#     # Create linked list
#     head = create_linked_list(list_values)
#     # c = head
#     # while c :
#     #     print(c.val)
#     #     c = c.next

#     # Create Solution object and call the method
#     solution = Solution()
#     result = solution.numComponents(head, nums)
    
#     print("Number of components:", result)