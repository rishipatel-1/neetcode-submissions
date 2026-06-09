class Codec:
    
    def serialize(self, root: Optional[TreeNode]) -> str:

        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return

            res.append(str(node.val))

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ",".join(res)        

        
    def deserialize(self, data: str) -> Optional[TreeNode]:

        vals = data.split(",")

        i = 0

        def dfs():
            nonlocal i

            if vals[i] == "N":
                i += 1
                return 


            node = TreeNode(int(vals[i]))

            i += 1

            node.left = dfs()
            node.right = dfs()


            return node

        return dfs()        

















