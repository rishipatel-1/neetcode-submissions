class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.word = ""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()

        for word in words:
            curr = root

            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]

            curr.isWord = True
            curr.word = word


        rows = len(board)
        cols = len(board[0])
        answer = []
        visited = set()

        def dfs(r, c, node):

            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visited or board[r][c] not in node.children:
                return

            visited.add((r, c))

            ch = board[r][c]

            node = node.children[ch]

            if node.isWord:
                answer.append(node.word)
                node.isWord = False

            dfs(r + 1, c, node)

            dfs(r - 1, c, node)

            dfs(r, c + 1, node)

            dfs(r, c - 1, node)

            visited.remove((r, c))


        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return answer