#1
    Define function removeInvalidParentheses, taking in s as a parameter
    which will be the string containing parentheses and a possible character

    if s is empty:
        return an empty string
       define and initialize an empty stack called stack
       define and initialize variables del_l and del_r to zero

       loop through each char in s:
        if the char equals an opening parenthesis:
            append it to the stack
        else if the char equals a closing parenthesis:
            if stack is not empty and the last element in the stack is an opening parenthesis:
                pop the last item from the stack
            else if stack is empty or the last element in the last is not an opening parenthesis:
                increment del_r by one
        after the loop, increment variable del_l by the length of the stack

        define a dfs function called dfs, taking as parameters i, curr, half, l, r, corresponding
        to the current index, an empty string, the number of excess half parenthesis, and
        left and right pointers:
            if l is less than zero or r is less than zero or half is less than zero:
                return nothing
             if i equals the length of the initial input string s:
                if l, r, and half equal zero:
                   add curr to result set called res
                return nothing
             if element in string s at index i equals an opening parentheses:
                recursive call to DFS passing in: i+1, curr, half, l - 1, r
                recursive call to DFS passing in: i + 1, curr, half + 1, l, r
             elif element in string s at index i equals a closing parenthesis:
                recursive call to DFS passing in: i+1, curr, half, l, r -1
                recursivew call to DFS passing in: i+1, curr + s[i], half-1, r
             else:
                dfs(i+1, curr + s[i], half, l, r)
        define a result set called res
        call on dfs function passing in: 0, '', 0, del_l, del_r
        return a list of res
        Time complexity is O(2*N)

#2
    This algorithm takes advantage of the condition that we are working with a
    binary search tree. We can iterate through the tree inorder and create a
    list that has all nodes of the array in order, and use this ordered list to find
    a minimum sum.

    Begin by defining the function, getMinimumDifference, taking root as a parameter
    where root is the root of a binary search tree.

    within this function we can define a nested method to perform the inorder traversal:
        define inorderTraversal, taking as parameters root and array, where root is the
        initial root of the BST passed into getMinimumDifference, and array is the
        empty array to hold the ordered nodes of the tree.
            if root is not null:
                recursive call to inorderTraversal() method, taking as parameters
                root.left, and array
                append the value of root to array
                recursive call to inorderTravesal() method, taking as parameters root.right,
                and array
        prepare to call on inorderTraversal method by creating and initializing
        an empty list called inorder_array
        call on inorderTraversal passing in root and inorder_array

        define and initialize a variable called minDiff to equal positive infinity
        iterate through the length of inorder_array - 1:
            reassign minDiff to equal the minimum between itself, and the absolute value of
            inorder_array[i] - inorder_array[i-1] and the absolute value of inorder_array[i]-
            inorder_array[i+1]
        return minDiff
        Since we know inorder_array will contain the sorted contents of the tree,
        we can compare values in a linear fashion instead of having to use two nested for loops

        Time complexity: the time complexity of this algorithm is O(N), as the inorder
        traversal of the tree is O(n), and the iteration through the newly created
        array is o(n), and finding the min using python's min() function is O(n),
        however we only ever compare 3 values at once using min(), instead of calling it
        on the entire array. So the time complexity would be O(N*3) or just O(N)

#3
    Determine if the length of the graph at index 0 is 0, if it is return 0

    define n to equal the length of the graph

    define and initialize an empty deque structure

    for each element at index i in range of n:
        append (i, and a frozenset of i)
    define and initialize set seen to equal set of q

    define and initialize steps to equal 0

    while q is not empty:
        define and initialize temp to equal a deque structure
        while q is not empty:
            variable cur and mask equal the left most element in q, pop it
            mask equals a list of itself
            for each node in graph at variable cur:
                append to mask the current node
                nextMask variable defined and initialized to equal frozenset of mask
                if length of nextMask equals n, simply return steps + 1
                if (node, nextMask) is not in seen set:
                    append to temp node and nextMask
                    add to set seen node and nextMask
                pop the last element from mask
        increment steps by 1
        q now equals temp
    return steps

    Time complexity is: O(nlogn)

#4
    #3
    In this algorithm, we will use recursion to calculate the max path sum of the left
    and right children of each root. We cannot sum the values of both left and right children
    as this is defined as not being a valid path. We can only travel to the left child, or right
    of each child of the first root.
    Define a function maxPathSum with root as a parameter. Root will be the tree provided.

        Define a global array outside the scope of the nested recursive function we will define later.
        Make this global array equal to the value of root.

        Now define the recursive function, dfs, taking the same root as a parameter.
            base case: if root is none, return 0

            define a leftMax variable to equal a call to dfs(root.left)
            define a rightMax variable to equal a call to dfs(root.right)

            to avoid negative numbers, redefine leftMax and rightMax to equal
            the maximum between itself and 0.

            Now update index 0 of the global array to equal the max between itself, and
            root.val + leftMax and rightMax

            return root.val + max(leftMax, rightMax) because we cannot use both leftMax and rightMax
        Make the recursive call to dfs passing in root as an argument.
        Return res at index 0
#5
    This algorithm utilizes dfs to achieve an O(N) complexity.

    Define the function LexigraphicalOrder, taking as a parameter n, which is an int

    define and initialize an empty result list

    define within LexigraphicalOrder method another method called dfs, taking as parameters
    temp, n, and result_list corresponding to an int, the first argument passed into lexigraphicalorder()
    method, and the result list initialize before the creation of the dfs function

        within dfs:
            if temp is greater than n, return

            append to the result list temp since it has not exceeded n
            recursive call to dfs, passing in temp*10, n, and result_list as arguments
                # this will allow us to maintain lexigraphical order for nums,
                # for example if we start with 1 and n greater than 10, the number
                # that should come after 1 to maintain lexicographical order should be
                # 10, so passing in 1*10 as an argument into dfs will give us this num
                # in the result list
            check if temp modulo 10 is not equal to 9 (if it is equal to 9, we need not go further
            because by this point we have already accounted for 10 as the second element in the list)
                if temp modulo 10 is not equal to 9 then we can simply call on DFS passing in
                temp + 1, n, and result_list as arguments.
                    This allows us to retrieve the next numbers after 19, 29, 39, etc.
                       2 will come after 19, 3 will come after 29, 4 will come after 39, etc.
    The time complexity of this algorithm is O(N), we utilize DFS to only ever have to visit
    each number once.