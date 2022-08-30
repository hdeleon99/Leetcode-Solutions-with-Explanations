Number 1: Two Sum
- For a brute force solution we can use two for loops, one nested within the other.
We will have two indexes for iterating, left and right. Start left off at 0, and start right off at 1.
Sum the values of nums[left] and nums[right] within the nested loop. If they equal target, return the indexes [left, right].
If they do not sum to the target, move right to the right by iterating the nested loop. Sum again.
Repeat until r index reaches the length of the nums array or until target has been found.
After right has reached the end of the array, move the left pointer to the right by iterating the first loop.
Sum the results of num[left] and nums[right] and compare to target, returning [left, right] if they are equal.
If not equal to target, iterate the first loop until sum is found, repeating until left has reached the length of the nums array - 1.
This has the worst case complexity of O(N^2)

Number 2: Find First and Last Position of Element in Sorted Array
- We will use a left and a right variable to slide the "window" of the array to the left or to the right,
and we will also utilize a boolean variable to determine in which direction to search after the first instance of target has been found.
Set the left variable to 0, and the right variable to the length of the array - 1.
Define and initialize an answer variable to -1, so that if the result is not found, -1 is returned.
We will execute the following so long as the left pointer is not greater than the right pointer: calculate the midpoint using the left and right variables, midpoint = (left+right)//2, ensuring the result is rounded down.
Compare nums[midpoint] to the target. If they are equal, assign the answer variable to the value of midpoint, and determine what the boolean leftSearch is.
If it is true, assign the right pointer to the left of midpoint by 1 to begin the process of searching for the second instance of the variable to the LEFT.
If leftSearch is false, we will search for the next instance of target to the right of the midpoint.
If the element at the midpoint does not equal the target to begin with, evaluate whether the element at midpoint is greater than or less than the target.
If it is less than, move the left pointer to the right of the midpoint by 1.
If the element at midpoint is greater than the target, move the right variable to the left of midpoint by 1. Repeat until left > right, and return the answer variable.
Because we are utilizing the Binary Search algorithm, this has a complexity of O(log n)

Number 3: Median of Two Sorted Arrays
 Two arrays, assign them to variables A and B
 We will determine what the smallest of the two arrays is, so we can run binary search on the smaller array.
 Utilize a total and half variable to represent the total number of elements in both arrays, and half of total, respectively.
 The half variable will tell us the total number of elements in the left partition.
 Repeat the following until the median has been found:
    Define a variable i to be the middle most element in array A
    Define a variable j to be the middle most element of B
    Initialize 4 variables: Aleft to the element at i, Aright to the element to the right of i, Bleft to the element at j, Bright to the element to the right of j.
    If Aleft is less than or equal to Bright and Bleft is less than or equal to Aright, then we have partitioned the two arrays correctly, and we can use this fact to determine the median.
        If the total number of elements in both arrays is odd, then we can return the minimum of Aright and Bright knowing that the minimum between the two corresponds to the median of the arrays merged together.
        If the total of the arrays is even, then we can return the maximum of Aleft and Bleft, plus the minimum of Aright and Bright, divided by 2.
    If Aleft is greater than Bright then we need to move our partition window in A to the left by 1.
    Else, we need to move our partition window to the right by 1.
 This algorithm runs in O(log(m+n)) time.

 Number 4: Remove Nth Node From End Of List
 In this problem we use two pointers, left and right. We will also use a dummy node.
 Point the dummy node to head, point left to the dummy node, and point right to head.
 We want to move right to the right n number of times. We then want to move both left and right
 to the right until right reaches null. This ensures there is a gap of size n between the left pointer and the right
 pointer. One right has reached null, left will be at the node one before the node to remove. So we
 will point left.next to left.next.next to "remove" the nth node from the back of the list. Worst case
 scenario this solution has a time complexity of O(n), where each node will need to be visited.
