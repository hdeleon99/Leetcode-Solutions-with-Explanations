from collections import defaultdict
from heapq import heappop, heappush
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
print("#1 =======================================")
print(canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]))
print(canFinish(numCourses=5, prerequisites=[[0, 3], [1, 4], [2, 4], [3, 1], [3, 2]]))


def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    adjDict = defaultdict(list)

    for u, v, w in times:
        adjDict[u].append([v, w])
    cost = 0
    # holds the path cost and the node in a list
    minHeap = [[cost, k]]  # at first, cost is 0 and starting node is k

    visited = set()
    res = 0
    while minHeap:
        cost, node = heappop(minHeap)
        if node in visited:
            continue
        visited.add(node)
        res = cost

        for neighbor, costToNei in adjDict[node]:
            # check if not in visited to avoid endless loops
            if neighbor not in visited:
                heappush(minHeap, [cost + costToNei, neighbor])
    if res == 0 or len(visited) != n:
        return -1
    return res


# O(ELog(V^2)) == O(E2Log(V)) == O(ELogV)

#2 input

# endless loop
print("#2 =======================================")
print(networkDelayTime(times=[[1,2,1], [2,1,3]], n=2, k=2))  # Should return 3
print(networkDelayTime(times=[[1,2,1],[2,3,2],[1,3,2]], n=3, k=1))  # should return 2
print(networkDelayTime(times=[[1,2,1],[2,3,2],[1,3,2], [4,5,1]], n=5, k=1))  # should return -1


