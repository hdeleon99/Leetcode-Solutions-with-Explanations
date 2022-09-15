Hector Issiah Deleon
CS497-4
9/15/2022
NetID: YH2397

#1
    In this problem, we will use recursion to construct our binary search tree. To begin, define a
    variable called length, which will equal the length of the linked list provided.
    We require the use of a global variable before the definition of our recursion function
    Now define the recursive function, defining two parameters, start and end.
        if start is greater than end
            return none
        calculate the middle of start and end by adding start and end and dividing by 2
        define our left node by calling on recursion(start, middle - 1) to find our left children
        define a root node as the value contained in self.head
        move self.head to next
        root.left equals left
        root.right equals the call to recursion(middle + 1, end) to find our right children
        return root
    Call on recursion, passing in 0 for start and length - 1 for end.

#2
    The algorithm in this solution takes advantage of the fact that the first element
    in a preorder list of nums will always be the root of the tree, since preorder is root->left
    ->right.
    To begin, define base cases:
        if preorder array or inorder array is none:
            return none
        define a root variable, its value will equal the first element in preorder array
        define a mid variable which will be the index of the number at
        preorder[0] in array inorder
        Now we will recusrively call the buildTree function, passing in slices of
        preorder and inorder arrays.

        An example preorder array: [3,9,20,15,7]
        an example inorder array: [9,3,15,20,7]

        At first, root will equal preorder[0], which is 3.
        Mid will equal inorder.index(preorder[0]), which will equal 1 at first.
                 m
        pre = [3,9,20,15,7]
                m
        in = [9,3,15,20,7]
        We know that in inorder, everything to the left of m will be in the left subtree of root.
        We know that in inorder, everything to the right of m will be in the right subtree of root.

        In preorder, everything from index 1 to mid will be in the left subtree,
        and everything to the right of mid (from mid+1:end) will be in the right subtree of root

        So with the above stated:
            define the left node of root to equal buildTree(preorder[1:mid+1], inorder[:mid+1])
            define the right node of root to equal buildTree(preorder[mid+1:], inorder[mid+1:])

            where each recursive call to buildTree will pass in slices of preorder and inorder as arguments
        Time complexity: Because we have to call index() function in each recursive call to buildTree,
        we have to iterate through each sliced list passed in as an argument to find the index of preorder[0]
        in inorder. This will give a time complexity of O(N^2) because there are two different recursive calls

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

#4
    In this problem, we utilize the algorithm of BFS (breadth first search) because we know BFS
    will iterate row by row in a tree.
    To begin, define the function largestValues(), taking in root as a parameter. Root should be
    the root of a binary search tree.
    Next, define and initialize an empty result array to hold our answer, and
    define a variable called queue, and initialize it to equal an array holding the root param [root] as such,
    passing root into an array allows us to iterate through queue and look at each node at that row

    Now initialize a while loop, ending when queue is none:
        first, append to the result array the max of node.val for each node at the current row/level in queue

        next, initialize an empty array called next_row which we will use to go down a level in the tree

        Using a for loop, iterate through each node in queue:
            for each child in node.left and node.right:
                if child is not none, then we can add it to our next_row array
        Reassign queue to equal next_row, as it will now move queue down a level
    return result

    Time complexity: complexity of max is O(n*h) where n is the number
    of nodes and h is the height of the tree,
    because we will have to visit every node of the tree and compare it with
    other values in that same row. So for every row, call on max() with a time complexity of O(N)

#5
    This problem can be solved using a recursive approach. To begin, we will need to construct a list
    list that contains the values of each node in the tree. This will help us when we use
    a left and a right pointer to determine the midpoint within the list. Everything to the left
    of the midpoint will be used to construct the left subtree, and everything to the right of mid
    will be used to construct the right subtree. This process continues until left > right

    To create a list with the value of each node in the tree, we will traverse the tree
    inorder.
Define our main function, balanceBST, taking root as a parameter to signal the root of
a binary tree:


   Define an empty list, tree_to_list = []
        Define a function, createListInorder, taking root and tree_list as parameters. Root is the
             root provided by the parameter in the parent function, balanceBST, and tree_list should be
             any empty list.
                 if root is not None:
                     call createListInorder, passing in root.left and tree_list as parameters
                     append the value of root.val to tree_list
                     call createListInorder, passing in root.right and tree_list as parameters
             Before proceeding, call on the newly created function createListInorder, passing in
             the tree_to_list initialized at the beginning of the code.
        Define createBST function, taking left, right, and tree_list parameters.
            Left and right correspond to the beginning of the tree_list, and the end of tree_list,
            respectively.
            If left is greater than right, return None.

            calculate midpoint, which is (left + right) // 2

            calculate root.left by assigning it the function call of createBST, passing in left as left,
            and mid - 1 as right, so that all values to the left of midpoint are considered for the left subtree
            calculate root.right by assigning it to the function call of createBST, passing in mid + 1 as left,
            and right as right, this way everything to the right of midpoint is considered for the right subtree of root.

            return root
   Finally, finish the main balanceBST function by returning a call to createBST,
   passing in 0, and length of tree_to_list - 1, and tree_to_list itself, to correspond to
   left, right, and tree_list, respectively.

   Time complexity: this algorithm has a time complexity of O(N). It will take linear time
   to iterate through the tree to create the tree_to_list, and it will take linear time
   to recreate the tree in a balanced fashion, as we will look at each element in tree_to_list
   only once.

