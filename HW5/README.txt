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
