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