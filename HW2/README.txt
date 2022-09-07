#1
    We will aim to achieve a O(1) space complexity by working with the array in-place.
    Initialize a count variable to 0, and a max variable to -1 to start the function call.
    Iterate through the number array:
        If count is equal to 0 (will always be true at first)
            set the current max variable to nums[i]
            increment count by 1
        Else if count != 0 and the current max variable equals nums[i]
            increment count by 1
        Else if count != 0 and the current max variable is not equal to nums[i]
            decrement count by 1
    Return current max variable
    This algorithm allows us to determine the max number in an array in-place, without using
    extra memory. It also has a time complexity of O(n), because we iterate through every
    element in the nums array.

#2
    In this algorithm we will take advantage of the quick select algorithm, utilizing partitions.
    Redefine k to equal the length of the nums array, minus k's initial value, so that k now
    corresponds to an index.
    Define a function to be used as the quickSort function, taking a left and a right variable as parameters.
    Initialize our pivot to equal the number at nums[right], and initialize a
    pointer variable to equal the left variable passed in as an argument.
    Iterate through our current window, from nums[left] to nums[right].
        If nums[i] is less than pivot
            we will swap the number at nums[pointer] with nums[i], ensuring that
            note: if we iterate over a number greater than the current pivot, we will move this variable over
            until it is located to the right of pivot.
            Increment pointer by 1
    Once our loop has ended, assign nums[pointer] to pivot, and nums[right] to nums[pointer]. This again ensures
    that a number larger than pivot will be placed to the right of pivot, or that pivot itself is the larget number
    If pointer is greater than k, we know we need to shrink our partition to the left
        So recursively call quickSort again, passing in the same left variable, and pointer - 1
    else if pointer is less than k, we know we need to shrink our partition to the right
        So recursively call quickSort passing in pointer + 1 as the first parameter and the same right variable as the second
        parameter
    Else if none of the above are true, we have found our Kth largest element, so return
    nums[pointer]

    This algorithm will have an average time complexity of O(N), but a worst case time complexity of O(N^2)
    in the event that our partitions are always greater than every other element, requiring our quick select
    algorithm to check the size of the array - 1 (excluding the previous pivot).
#3
    This algorithm takes advantage of the bucket sort technique.
    To begin, initialize a variable to the length of our input array, nums.
    If the length of nums is less than two, return 0 as instructed.
    Now initialize a low and a high variable, to the minimum and maximum numbers of
    the input array, respectively.
    Define and initialize an empty dictionary to be used as our bucket.
    Iterate through each number in the input array.
        if the current number equals high
            define and initialize a variable, index, to be length - 1
        else
            define index to be the absolute value of low - num, times the length - 1,
            divided by high minus low. This will provide us the bucket # (or index)
            to append our number into.
        Once if and else have been evaluated, appen the current num
        to buckets at index.
    Define and initialize an empty array.
    Iterate through our bucket:
        if the bucket at index i exists
            append to our array the minimum and maximum of the current bucket
    Define and initialize a variable output to zero
    Iterate through the recently created array
        Assign output a value that is the max between output's current value,
        and the absolute value of the last number in bucket i-1 minus the first value
        in bucket i. This will provide us our maximum difference
    Return output variable

    Time complexity: iterate through every num in nums, so O(N)

#4
    In this algorithm we will use a dictionary and a stack to achieve a linear solution.

    To begin, initialize an empty dictionary, let's call it lookup.
    Iterate through each letter in the input string, and assign the current index to the dictionary
    at the current char.
    So for an input of [abca] the dictionary will look like {"a": 3, "b": 1, "c": 2}. This ensures that the maximum possible
    index is assigned to the value of that character (the key of the dict). This will be used later to determine whether
    we can remove an unneeded character from our stack.
    Next, initialize an empty stack, let's call it stack.
    Now iterate len(input) number of times,
        if the current character at input[i] is in the stack, continue
        Now use a while loop to check if: the stack is not empty and the last character in the stack
        is greater than the current character (helps keep stack in order) and if the last character in the stack has a value
        in the previously filled dictionary greater than the current index (we know the letter appears
        again later on).
            If this is true, we know we can pop from our stack.
        Add the char at input[i] to the stack
    Once this last loop has finished iterating, we will have a stack that contains no duplicate letters
    and maintains lexicographical order

