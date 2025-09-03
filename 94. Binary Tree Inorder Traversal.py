# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root is None:
            return
        
        res = []

        def inorderTraversal1(node):
            if node is None:
                return
            inorderTraversal1(node.left)
            res.append(node.val)
            inorderTraversal1(node.right)

        inorderTraversal1(root)

        return res
    
