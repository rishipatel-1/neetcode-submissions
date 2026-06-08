class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, currentMax):

            if not node:
                return 0

            good = 0

            if node.val >= currentMax:
                good += 1

            currentMax = max(currentMax , node.val)


            left = dfs(node.left, currentMax)
            right = dfs(node.right, currentMax)


            return good + left + right

        return dfs(root, root.val)            
