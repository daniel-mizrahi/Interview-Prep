class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = {i:0 for i in range(numCourses)} 
        graph = {i:[] for i in range(numCourses)}
        for req in prerequisites:
            indegree[req[0]] += 1
            graph[req[1]].append(req[0])
        queue = [i for i in range(numCourses) if not indegree[i]]
        if not len(queue):
            return False
        for course in queue:
            for c in graph[course]:
                indegree[c] -= 1
                if not indegree[c]:
                    queue.append(c)
        return len(queue) == numCourses
