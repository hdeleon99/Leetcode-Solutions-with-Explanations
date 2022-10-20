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
Time complexity: The time complexity of this algorithm is O(N). No node is visited more than once.


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

