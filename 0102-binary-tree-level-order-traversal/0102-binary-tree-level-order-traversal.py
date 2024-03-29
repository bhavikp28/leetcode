# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        ans = []
        queue = deque()
        if root:
            queue.append(root)
        level = 0
        while len(queue) > 0:
            lvl = []
            for i in range(len(queue)):
                cur = queue.popleft()
                lvl.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            level += 1
            ans.append(lvl)
        return(ans)'''
    
        output =[]
        if not root:
            return output
        def helper(node,level):
            if len(output) == level:
                output.append([])
            output[level].append(node.val)
            if node.left:
                helper(node.left,level + 1)
            if node.right:
                helper(node.right,level +1)
        helper(root,0)
        return output
