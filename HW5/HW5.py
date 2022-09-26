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