class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degree = {i:0 for i in range(numCourses)}
        graph = {i:[] for i in range(numCourses)}
        for course in prerequisites:
            degree[course[0]] += 1
            graph[course[1]].append(course[0])
        queue = [i for i in range(numCourses) if not degree[i]]
        res = []
        while len(queue):
            course = queue.pop(0)
            res.append(course)
            for c in graph[course]:
                degree[c] -= 1
                if not degree[c]:
                    queue.append(c)
        return res if len(res) == numCourses else []
