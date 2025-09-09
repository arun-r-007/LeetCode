# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0

        left_depth = 0
        left = root
        while left:
            left_depth += 1
            left = left.left

        right_depth = 0
        right = root
        while right:
            right_depth += 1
            right = right.right

        if left_depth == right_depth:
            return 2 ** left_depth - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        










# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#     def countNodes(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: int
#         """
#         if root is None:
#             return 0
#         count = [0]

#         def countN(node):
#             if node is not None:
#                 count[0] += 1
#                 countN(node.left)
#                 countN(node.right)
        
#         countN(root)
#         return count[0]