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

