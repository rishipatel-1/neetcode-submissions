# these is a brute force solution to compare each word for oneWordDifference 
# if the words are  like 5000 then these bemoes heavy

from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        queue = deque()

        queue.append(beginWord)

        visited = set()

        visited.add(beginWord)

        steps = 1

        def oneWordDifference(word1, word2):

            difference = 0

            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    difference += 1

            return difference == 1 

        while queue:

            queueSize = len(queue)

            for _ in range(queueSize):

                currentWord = queue.popleft()

                if currentWord == endWord:
                    return steps

                for nextWord in wordList:

                    if nextWord not in visited and oneWordDifference(currentWord, nextWord):
                        visited.add(nextWord)
                        queue.append(nextWord)        

            steps +=1

        return 0    


        