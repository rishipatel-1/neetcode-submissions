class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr  = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()

            curr = curr.children[ch]

        curr.isWord = True        
        

    def search(self, word: str) -> bool:

        def dfs(i, node):
            if i == len(word):
                return node.isWord

            ch = word[i]

            if ch != ".":
                if ch not in node.children:
                    return False
                return dfs(i+1 , node.children[ch])
               
            for children in node.children.values():
                if dfs(i+1, children):
                    return True

            return False        
                        
        return dfs(0 , self.root)


        
