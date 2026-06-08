# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        def dfs(node):
            if not node:
                return (True, 0)

            leftbalance , leftheight = dfs(node.left) 
            rightbalance , rightheight = dfs(node.right)

            balanced = (leftbalance and rightbalance and abs(leftheight-rightheight) <=1 )

            height = 1 + max(leftheight, rightheight)


            return (balanced , height)




        dfs(root)

        return dfs(root)[0]




        