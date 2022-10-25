Number 1:
This approach will use BFS
Define the function validPath:
    Parameters: n -> the number of vertex, edges -> the bidirectional graph, source -> the starting vertex,
    destination -> the desired vertex

    Define and initialize a graph object to equal a defaultdict of type list, this will
    represent the 2d array of edges

    for each edge in edges,
        add to the dictionary the first vertex as the key, and the second vertex as the value
        add to the dictionary the second vertex as the key, and the first vertex as the value

    define and initialize an object named queue to equal a collections deque structure, passing in the source
    node inside a list as the first element in the queue

    create and initialize an empty set named visited, this will be used to track the nodes that
    have been visited to avoid an endless loop

    While the queue is not empty
        pop the leftmost element from the queue and initialize this to an object named node
        if node equals the destination node, return true

        add to visited the node

        for each neighbor in the current node's resulting value at key node in the dictionary
            if the current neighbor is in visited, continue
            add to the queue the current neighbor
    If true is never returned above, then there is no path to the destination node. Return false
    Time complexity: The time complexity of this approach is O(V + E), each vertex will be visited, and each
    path will be explored


Number 2:
Define the function longestCycle, with a parameter named edges that will be a
list of ints.
    define and initialize nodes and ans objects to equal a set from 0 to the length of edges, and 1 respectively.
    While nodes is not None:
        Iteratively traverse each node that currently
        remains of the nodes.

        We need a list to count backward for the
        number of nodes in a circle.

        If we no longer find the next node,
        then break the while.

        For every seen node, discard it from nodes.
Time complexity: The time complexity of this algorithm is O(V + E). No node is visited more than once.


Number 3:
Define the function minCost, taking as parameters n, the number of cities,
and connections, the list of lists representing the possible connections of these cities

    define and initialize a neighbor object to equal a default dict of type list
    for each city1, city2, and cost pair in connections:
        add to the dictionary the city1 as the key, and a list of the cost and city 2 as the value
        add to the dictionary the city2 as the key, and a list of the cost and city1 as the value

    define and initialize total_cost variable to equal 0
    define and initialize a priority queue to equal a list of a list of 0, and n at first
    define and initialize a visited set, empty at first
    while priority queue is not empty,
        define and initialize curr_cost and curr_city to equal the result
        of heappopping the priority queue to reflect the connection with the lowest cost
        if curr_city is not yet in visited set:
            add to the visited set the curr_city
            add the curr_cost to the total cost
        if we have visited all cities (length of visited set will equal n),
        return the total_cost

        while the curr_city is still in the dictionary:
            a list of this_cost and this_city will equal the value of curr_city in the dicitonary, popped off
            push to the priority queue the list of this_cost and this_city calculated above
    if the return statement above never executes, then it is not possible to return a minimum
    cost so return -1
The time complexity is: O(V+E), each vertex and edge will be visited at most once
