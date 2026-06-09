class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        count = 0
        answer = 0

        def dfs(node):
            nonlocal answer, count

            if not node:
                return

            dfs(node.left)

            count += 1

            if count == k:
                answer = node.val
                return

            dfs(node.right)

        dfs(root)

        return answer            

            
        