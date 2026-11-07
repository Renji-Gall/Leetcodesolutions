# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def isSame(root, subRoot):
            if root == None and subRoot == None:
                return True
            if root == None or subRoot == None:
                return False

            if root.val != subRoot.val:
                return False

            return isSame(root.left, subRoot.left) and isSame(root.right, subRoot.right)

        if root == None: 
            return False
        if subRoot == None:
            return True
        if isSame(root, subRoot):
             return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        