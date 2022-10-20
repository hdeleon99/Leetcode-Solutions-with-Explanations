# 3
from typing import List

# 3 input
edges1 = [3,3,4,2,3]
edges2 = []
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
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

        # Iteratively traverse each node that currently
        # remains of the nodes.

        # We need a list to count backward for the
        # number of nodes in a circle.

        # If we no longer find the next node,
        # then break the while.

        # For every seen node, discard it from nodes.
