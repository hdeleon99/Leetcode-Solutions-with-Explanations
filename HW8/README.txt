#1
This algorithm utilizes a DFS approach to traversing a graph representing course
prerequisites.
                                                                                           key  : value
Begin by creating an adjacency dict, signifying each courses prerequisite, called preMap (course: [prereqs])

Create and initialize two empty sets, visited and cycle, as well as an empty list, result

define the dfs function taking a course as a parameter:
    check if the course is in the cycle set, if it is this is a cycle and is invalid, return false
    check if course in visited, if it is return true to avoid repeat processing of already
    visited/validated course

    add the course to the cycle

    for each prerequisite of this current course:
        if a recursive call to dfs, passing in prereq returns false, end the recursive stack and return
        false
    if loop iterates without returning false, then each prereq is valid, and we can then
    remove the current course from cycle set

    add to visited the current course to signify that this course has been accounted for to avoid
    repeat evaluation of current course and repeat additions of this course to the result

    add to result the current course; since this is a recursive function, the first course encountered
    that has no prereqs will be added to the result, which means the courses will be added in order

    return True if all of the above completes successfully

for each course in the dictionary (for each key):
    check if dfs of this current course returns false, if yes return an empty list
otherwise, return the result list

Time complexity:
    The time complexity of this approach is O(P + N) where p is the number of prerequisites
    and N is the number of courses. Each course will need to have its prereqs validated,
    and each prereq will need to validate any prereqs that it has, so at most each node/edge will
    be visited twice

#2
This problem utilizes bit manipulation instead of using the division, multiplication, or
modulo operators.
Begin by initializing a positive variable to equal true if both the divisor and the dividend
are less than zero or both greater than zero, and false if one is less than zero while the other is
greater
initialize dividend and divisor to equal their absolute values
initialize result to equal zero
while dividend is greater than or equal to divisor:
    initialize a temp variable to equal divisor, and i to equal 1
    while dividend is greater than or equal to temp:
        decrement dividend by temp
        increment result variable by i
        bitshift i by 1
        bitshift temp by 1
if positive is false then we need to return a negative result, so res = -res
to avoid overflow errors or divisors of zero
Time complexity:
This algorithm runs in O(1) time

#3 This algorithm uses a bottom up DFS/DP approach to solve the problem
We will store our "DP" cases, or utilize memoization using a simple list called cache that holds
amount + 1 number of elements, initialized to positive infinity at first

Initialize the base case of DP:
    Cache at index 0 equals 0, because it takes 0 coins to sum to 0
For each number up to amount+1, starting at 1,
    for each coin in the list of coins,
        calculate the difference between the current number and the current coin
        if the difference is greater than or equal to 0, then this is possibly a valid combination of
        current coin values and previous coin values, and we can also access an element at index difference in cache,
        if difference was negative we could not access the element in cache
            so initialize the value of cache at index number to equal the minimum
            between itself, and (1 + cache[difference]). This will go through all
            coin values (assuming the difference is equal to or greater than zero), and determine\
            from which previous calculations can we achieve this sum with the minimum number
            of coins
    Once both loops have run, the element at index amount in cache will provide
    the minimum number of coins to hit that sum, amount, so return it but only
    if it is not equal to positive infinity, or else
    Time complexity:
    The time complexity is O(N*M) where N equals the amount, and M equals the number of coins

