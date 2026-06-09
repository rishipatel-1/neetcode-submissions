class Solution:
    def buildTree(self, preorder, inorder):

        if not preorder or not inorder:
            return None

        rootVal = preorder[0]
        root = TreeNode(rootVal)

        mid = inorder.index(rootVal)

        leftInorder = inorder[:mid]
        rightInorder = inorder[mid + 1:]

        leftSize = len(leftInorder)

        leftPreorder = preorder[1:1 + leftSize]
        rightPreorder = preorder[1 + leftSize:]

        root.left = self.buildTree(leftPreorder, leftInorder)
        root.right = self.buildTree(rightPreorder, rightInorder)

        return root