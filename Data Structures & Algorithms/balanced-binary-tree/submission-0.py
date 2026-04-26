# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(node: Optional[TreeNode]) -> Optional[int]:
            if node is None:
                return 0
            leftH = get_height(node.left)
            rightH = get_height(node.right)

            if leftH is None:
                return None
            elif rightH is None:
                return None
            elif abs(leftH - rightH) > 1:
                return None

            return 1 + max(leftH, rightH)

        return get_height(root) is not None