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
