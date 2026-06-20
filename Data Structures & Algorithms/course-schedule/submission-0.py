class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        visited = set()
        path = set()
        graph = {}

        for course in range(numCourses):
            graph[course] = []

        for courseMap , prerequisite in prerequisites:
            graph[courseMap].append(prerequisite)

        def dfs(course):

            if course in path:
                return False

            if course in visited:
                return True

            path.add(course)

            for prerequisite in graph[course]:
                if dfs(prerequisite) == False:
                    return False        

            path.remove(course)
            visited.add(course)

            return True        

        for course in range(numCourses):
            if dfs(course) == False:
                return False

        return True        



        