class Solution:
    def maxPathSum(self, root):

        maxPath = root.val

        def dfs(node):
            nonlocal maxPath

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            left = max(left, 0)
            right = max(right, 0)

            currentPath = left + node.val + right

            maxPath = max(maxPath, currentPath)

            return node.val + max(left, right)

        dfs(root)

        return maxPath