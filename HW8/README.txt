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