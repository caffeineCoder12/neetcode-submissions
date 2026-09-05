# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = None
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if (root == None):
            return None
        node = root.val
        if ((node <= p.val and node >= q.val) or (node >= p.val and node <= q.val)):
            self.res = root
            return self.res
        elif (p.val < node and q.val < node):
            self.lowestCommonAncestor(root.left, p, q)
        else: 
            self.lowestCommonAncestor(root.right, p, q)
        return self.res