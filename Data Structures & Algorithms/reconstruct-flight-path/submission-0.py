class Solution:

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = {}

        for start, end in tickets:
            if start not in graph:
                graph[start] = []
            graph[start].append(end)

        for airport in graph:
            graph[airport].sort()

        answer = []

        def dfs(airport):
            while airport in graph and graph[airport]:
                nextAirport = graph[airport].pop(0)
                dfs(nextAirport)

            answer.append(airport)

        dfs("JFK")

        return answer[::-1]