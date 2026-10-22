# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.thetruth = True
        def dfs(node):    
            if not node:
                return 0

            heightleft = dfs(node.left)
            heightright = dfs(node.right)
            if abs(heightleft - heightright) > 1:
                self.thetruth = False    

            return max(heightleft, heightright) + 1
 
        dfs(root)
        return self.thetruth