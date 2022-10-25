#1
The solution to this problem utilizes a DFS recursive approach.
Define the function canFinish, taking as parameters the number of courses and the list of lists
reflecting [a,b] where a is the course and b is the prereq for course a

Assign each course to a key in a dictionary with a value equal to all of its prereqs

create an empty visited set

define a nested funciton dfs, taking as a parameter the current course number
check if the course is in visited, if it is, then we have encountered
a loop and can return false because it is impossible to satisfy a looping requirement
if the course's value in the dictionary is an empty list, then it can be completed
and we can immediately return true

otherwise, we need to add the current course to the visited set

iterate through each prerequisite for this course,
    if a recursive call to dfs, passing in this current prereq, returns false,
    then the prereq can not be completed and we can immediately return false
remove the current course from visited as we have verified its requirements
assign the value of this current course in the dictionary to an empty list to signify
that this course can be completed with valid prereqs
return true once all of the above has run, the course and its prereqs are validated

now outside of the dfs function, iterate through each course:
for this course, call dfs on it. return false if dfs returns false, meaning the course cannot be completed
if the loop exits without returning false, then all courses have been validated
Time complexity: Each node (course) will need to be visited at least once (N), and
each edge will need to be traveled at most once (P, where P is the prerequisite reflected by a graph edge)
Therefore, the time complexity is O(N+P)