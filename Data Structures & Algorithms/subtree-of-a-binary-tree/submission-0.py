class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False

            leftsame = isSameTree(p.left,q.left)
            rightsame = isSameTree(p.right,q.right)

            return leftsame and rightsame

        def dfs(node):
            if not node:
                return False

            if isSameTree(node, subRoot):
                return True
                
            return dfs(node.left) or dfs(node.right)

        return dfs(root)        




