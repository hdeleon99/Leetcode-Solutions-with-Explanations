import collections
import heapq
from typing import List

# 2 input
edges1 = [3, 3, 4, 2, 3]
edges2 = [2, -1, 3, 1]

# 3 input
connections1 = [[1, 2, 3], [3, 3, 4]]  # should return -1
connections2 = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]  # should return 6


class Solution:
    @staticmethod
    def longestCycle(edges: List[int]) -> int:
        nodes, ans = set(range(len(edges))), 1

        while nodes:
            node = nodes.pop()
            seen, path, count = set(), [], 1
            while True:
                seen.add(node)
                path.append(node)
                node = edges[node]

                if node in seen:
                    while path.pop() != node: count += 1
                    ans = max(ans, count)
                    break

                if node == -1 or node not in nodes: break

                nodes.discard(node)
        return ans if ans != 1 else -1

    @staticmethod
    def minCost(n: int, connections: List[List[int]]) -> int:
        neighbor = collections.defaultdict(list)
        for city1, city2, cost in connections:
            neighbor[city1].append([cost, city2])
            neighbor[city2].append([cost, city1])

        total_cost = 0

        pq = [[0, n]]

        visited = set()

        while pq:
            curr_cost, curr_city = heapq.heappop(pq)
            if curr_city not in visited:
                visited.add(curr_city)
                total_cost = total_cost + curr_cost
            if len(visited) == n:
                return total_cost
            while neighbor[curr_city]:
                [this_cost, this_city] = neighbor[curr_city].pop()
                heapq.heappush(pq, [this_cost, this_city])
        return -1

    @staticmethod
    def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # bfs approach
        # create a dictionary representation of the graph
        graph = collections.defaultdict(list)
        # example: edges = [[0,1], [2,0], [1,2]]
        for edge in edges:  # O(N)
            # bidirectional so we consider both vertex
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        # resulting dictionary: graph = {0:[1,2], 1:[0,2], 2:[0,1]}

        # create a queue for the bfs approach, with the source node added as the first element in the queue
        queue = collections.deque([source])  # O(1)

        # create a set to keep track of visited nodes
        visited = set()  # O(1)

        # do bfs
        while queue:  # O(V)
            node = queue.popleft()  # O(1)

            if node == destination:  # O(1)
                return True

            visited.add(node)  # O(1)

            # No vertex will have N number of neighbors
            for neighbor in graph[node]:  # O(
                if neighbor in visited:
                    continue
                queue.append(neighbor)
        return False


# 1
print("Solution.validPath(n = 3, [[1,0], [1,2], [2,0]], source = 1, destination = 2",
      Solution.validPath(n=3, edges=[[1, 0], [1, 2], [2, 0]], source=1, destination=2))
print("Solution.validPath(n=7, edges=[[0,1], [1,2], [2,0], [2,3], [3,4], [5,6]], source=0, destination=7",
      Solution.validPath(n=7, edges=[[0, 1], [1, 2], [2, 0], [2, 3], [3, 4], [5, 6]], source=0, destination=7))

# 2
print("Solution.longestCycle(edges1)", Solution.longestCycle(edges1))
print("Solution.longestCycle(edges2)", Solution.longestCycle(edges2))

# 3
print("Solution.minCost(connections1)", Solution.minCost(4, connections1))
print("Solution.minCost(connections2)", Solution.minCost(3, connections2))
