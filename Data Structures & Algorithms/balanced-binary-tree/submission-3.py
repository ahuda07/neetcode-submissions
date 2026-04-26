# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # return a boolean
        # get height, so make a helper function
        # make a base case, if there is no root
        # level order traversal, root, left, right
        # use recursion to get height of a node

        def get_height(node: Optional[TreeNode]):
            if node == None:
                return 0
            
            leftH = get_height(node.left)
            rightH = get_height(node.right)
            # get the height of the nodes

            # case checking
            if leftH is None:
                return None
            if rightH is None:
                return None
            if abs(leftH - rightH) > 1: 
                return None
            
            height = max(leftH, rightH) + 1

            return height

        return get_height(root) is not None