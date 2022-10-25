from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    preMap = {i: [] for i in range(numCourses)}

    for course, prereq in prerequisites:
        preMap[course].append(prereq)

    visited = set()

    def dfs(course):
        if course in visited:
            return False
        if not preMap[course]:
            return True  # no prereq

        visited.add(course)

        for prereq in preMap[course]:
            if not dfs(prereq): return False

        visited.remove(course)
        preMap[course] = []

        return True

    for course in preMap:
        if not dfs(course): return False
    return True


# 1 input
print(canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]))
print(canFinish(numCourses=5, prerequisites=[[0, 3], [1, 4], [2, 4], [3, 1], [3, 2]]))
