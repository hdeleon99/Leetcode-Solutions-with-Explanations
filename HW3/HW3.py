class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.val),
        if self.right:
            self.right.PrintTree()


# 1 ==============================================
class Solution:
    def __init__(self):
        self.head = None

    def sortedListToBST(self, head):
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        self.head = head
        print("self ", self.head)
        print("head", head)

        def recursion(start, end):
            if start > end: return None
            middle = (start + end) // 2
            # left
            left = recursion(start, middle - 1)

            # root
            root = TreeNode(self.head.val)
            self.head = self.head.next
            print("self inside recursion: ", self.head)
            root.left = left

            # right
            root.right = recursion(middle + 1, end)
            return root

        return recursion(0, length - 1)


lList = ListNode(-10)
lList.next = ListNode(-3)
lList.next.next = ListNode(0)
lList.next.next.next = ListNode(5)
lList.next.next.next.next = ListNode(9)

curr = lList
res = []
while curr:
    res.append(curr.val)
    curr = curr.next

print("#1 INPUT --------------------------------------")
A = Solution()
tree = A.sortedListToBST(lList)
print(res)
tree.PrintTree()


# 2 ==============================================================
def buildTree(preorder, inorder):
    # base case
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])

    mid = inorder.index(preorder[0])
    #               m
    # preorder = [3,9,20,15,7]
    #               m
    # inorder =  [9,3,15,20,7]
    root.left = buildTree(preorder[1:mid + 1], inorder[:mid])

    root.right = buildTree(preorder[mid + 1:], inorder[mid + 1:])

    return root

print("#2 Input ----------------------------------------")
preorder_1 = [3, 9, 20, 15, 7]
inorder_1 = [9, 3, 15, 20, 7]
res1 = buildTree(preorder_1, inorder_1)
res1.PrintTree()

preorder_2 = [2, 4, 6, 5, 3]
inorder_2 = [4, 2, 5, 6, 3]
res2 = buildTree(preorder_2, inorder_2)
res2.PrintTree()


# 3 =============================================================================
def maxPathSum(root):
    res = [root.val]

    def dfs(root):
        if not root:
            return 0
        leftMax = dfs(root.left)
        rightMax = dfs(root.right)

        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)

        res[0] = max(res[0], root.val + leftMax + rightMax)

        # cant choose both or else this means we're splitting.
        # when we split we don't have a valid path

        return root.val + max(leftMax, rightMax)

    dfs(root)
    return res[0]


print("#3 Input ----------------------------------------")
num3Root1 = [1,2,3] # should return 6
num3Root2 = []
