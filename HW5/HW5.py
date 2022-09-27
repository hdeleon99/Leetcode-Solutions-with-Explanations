from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def removeInvalidParentheses(s):
    """"""
    # count the number of '(' and ')' needs to be removed
    if not s:
        return ['']
    stack = []
    del_l = del_r = 0
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                del_r += 1
    del_l += len(stack)

    # apply dfs
    def dfs(i, curr, half, l, r):  # half: number of excess half parenthesis '(' in curr
        if l < 0 or r < 0 or half < 0:
            return
        if i == len(s):
            if l == r == half == 0:  # push valid result
                res.add(curr)
            return
        if s[i] == '(':
            dfs(i + 1, curr, half, l - 1, r)  # del l
            dfs(i + 1, curr + s[i], half + 1, l, r)  # keep l
        elif s[i] == ')':
            dfs(i + 1, curr, half, l, r - 1)  # del r
            dfs(i + 1, curr + s[i], half - 1, l, r)  # keep r
        else:
            dfs(i + 1, curr + s[i], half, l, r)  # add letters

    res = set()
    dfs(0, '', 0, del_l, del_r)
    return list(res)


print("#1 Input and Outputs ====================================================")
q1i1 = "((a)))"
q1i2 = "()()((()"
print(removeInvalidParentheses(q1i1))
print(removeInvalidParentheses(q1i2))


def getMinimumDifference(root):
    def inorderTraversal(root, array):
        if root:
            inorderTraversal(root.left, array)
            array.append(root.val)
            inorderTraversal(root.right, array)

    inorder_array = []
    inorderTraversal(root, inorder_array)

    minDiff = float(inf)
    for i in range(len(inorder_array) - 1):
        minDiff = min(minDiff, abs(inorder_array[i] - inorder_array[i - 1]),
                      abs(inorder_array[i] - inorder_array[i + 1]))
    return minDiff


print("#1 Input and Outputs ====================================================")
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(6)
root.right.left = TreeNode(4)
root.right.right = TreeNode(7)
print("getMinimumDifference(root) returned: ", getMinimumDifference(root)) # --> should return 1

root2 = TreeNode(100)
root2.left = TreeNode(30)
root2.left.left = TreeNode(20)
root2.left.right = TreeNode(40)
root2.right = TreeNode(150)
root2.right.left = TreeNode(120)
print("getMinimumDifference(root2) returned: ", getMinimumDifference(root2)) # --> should return 10
