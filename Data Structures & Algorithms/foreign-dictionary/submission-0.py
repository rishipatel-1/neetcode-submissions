class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        graph = {}

        for word in words:
            for ch in word:
                graph[ch] = []

        for i in range(len(words)- 1):

            word1 = words[i]
            word2 = words[i+1]

            minLen = min(len(word1), len(word2))

            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ''

            for j in range(minLen):
                if word1[j] != word2[j]:
                    graph[word1[j]].append(word2[j])   
                    break  

        visited = set()
        path = set()

        answer = []

        def dfs(ch):
            if ch in path:
                return False

            if ch in visited:
                return True

            path.add(ch)

            for neighbour in graph[ch]:
                if dfs(neighbour) == False:
                    return False

            path.remove(ch)
            visited.add(ch)
            answer.append(ch)
            return True

        for ch in graph:
            if dfs(ch) == False:
                return ""

        return "".join(answer[::-1])                           




        