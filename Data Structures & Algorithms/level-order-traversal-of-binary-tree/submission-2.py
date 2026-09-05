# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        c = 0
        queue = deque()
        queue.append(root);
        while (len(queue) != 0):
            tmp = []
            for i in range(len(queue)):
                temp = queue.popleft()
                if (temp != None):
                    queue.append(temp.left)
                    queue.append(temp.right)
                    tmp.append(temp.val)
            if tmp:
                res.append(tmp)
        return res