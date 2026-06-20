 # now we need to genereate word set instead of many looks ups

from collections import deque


class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        queue = deque([beginWord])

        visited = set([beginWord])

        steps = 1


        while queue:

            queueLength = len(queue)


            for _ in range(queueLength):

                currentWord = queue.popleft()


                if currentWord == endWord:
                    return steps


                for i in range(len(currentWord)):


                    for ch in "abcdefghijklmnopqrstuvwxyz":


                        newWord = currentWord[:i] + ch + currentWord[i + 1:]


                        if newWord in wordSet and newWord not in visited:

                            visited.add(newWord)

                            queue.append(newWord)


            steps += 1


        return 0