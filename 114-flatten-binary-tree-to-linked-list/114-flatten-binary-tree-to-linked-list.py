# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        curr = root
        while True:
            if curr.left and not curr.right:
                curr.right = curr.left
                curr.left = None
                curr = curr.right
            elif curr.left and curr.right:
                rightSubTree = curr.right
                curr.right = curr.left
                curr.left = None
                temp,curr = curr.right,curr.right
                while temp.right:
                    temp = temp.right
                temp.right = rightSubTree
            elif not curr.left and curr.right:
                curr = curr.right
            else:
                break