# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.out = []
        self.curr = 0
        self.total = 0
        self.stack = [root]
        while self.stack:
            node = self.stack.pop()
            if not node.right and not node.left:
                self.out.append(node.val)
                self.total += 1
            if node.right:
                self.stack.append(node.right)
            if node.right or node.left:
                self.stack.append(node)
            if node.left:
                self.stack.append(node.left)
            node.left = None
            node.right= None
    def next(self) -> int:
        self.curr += 1
        return self.out[self.curr - 1]
        

    def hasNext(self) -> bool:
        if self.curr < self.total:
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()