from typing import List


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    preMap = {i: [] for i in range(numCourses)}
    for course, prereq in prerequisites:
        preMap[course].append(prereq)
    visited = set()
    result = []
    cycle = set()
    '''
    course | prereq
    0      | [2]
    1      | [3]
    2      | [1, 4]
    3      | []
    4      | [3]
    visited = (3, 1, 4, 2, 0)
    '''

    def dfs(course):
        if course in cycle:
            return False
        if course in visited:
            return True

        cycle.add(course)

        for prereq in preMap[course]:
            if not dfs(prereq):
                return False

        cycle.remove(course)
        visited.add(course)
        result.append(course)

        return True

    for course in preMap.keys():
        if not dfs(course):
            return []
    return result
print("#1 input")
print(findOrder(numCourses=5, prerequisites=[[0,2], [2,1], [2,4], [1,3], [4,3]])) # should return [3, 1, 4, 2, 0]
print(findOrder(numCourses=2, prerequisites=[[0,1], [1,0]])) # should return []
