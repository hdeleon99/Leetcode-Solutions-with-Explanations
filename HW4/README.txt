Hector Issiah Deleon
CS497-4
9/22/2022
NetID: YH2397

#1

    Define the function, topKFrequentElements(), with parameters nums being the list of
    nums to search through, and k being the k number of top frequent elements to find.

    initialize an empty defaultdict dictionary. We will use the dictionary to hold
    number:count pairs to determine the frequency of each unique number in nums

    initialize an array containing len(nums) number of subarrays + 1. The frequency array
    will hold each unique element at an index corresponding to the frequency of that number.
    So we essentially take the number and its count from the defaultdict, and put it into
    an array of arrays, where each subarray sits at an index from 0 - len(nums) + 1, and each index
    will reflect the count of a unique number.

    initialize an empty result list
    Once the dictionary and array of arrays have been filled, iterate through the frequency array
    starting from the end, and iterating until the beginning (reverse iteration).
    For each subarray at freq[i],
        for each num in subarray at freq[i]
            append to result list num
            check if length of result list is k, if true, return result

#2
    Algorithm for #2:
        Will use binary search to find the element closest to x
        define function findClosestElements(arr, k, x), where arr is the array
        to be used, k is the number of elements closest to x, and x is the number to find k closest
        elements of

        finding a value closest to or equal to x...
        define left and right pointers, and initialize them to the beginning and end of the array
        respectively
        define and initialize two variables val, and idx, to be equal to the beginning of the array
        and zero, respectively

        in a while loop that runs until left is less than or equal to right:
            define a mid variable (left + right) / 2

            define and initialize a currDiff variable to equal the absolute value of arr[mid] - x
            define a resDiff variable and initialize it to equal val - x
            these two variables, currDiff and resDiff will help us to determine...

            if currDiff is less than resDiff, or if currDiff equals resDiff and the value at
            midpoint in the array is less than val,
                val now equals value in arr at mid
                and idx now equals mid

            if element at mid in arr is less than x, then we know every value to the left
            of mid is too small to be "close to" or equal to x, so left will now equal
            mid + 1

            elif element at mid in arr is greater than x, then we know every value to the right of
            mid is too large to be close to or equal to x, so right will now equal
            mid - 1

            else if element at mid in arr equals x, then we have an ideal case and can break the while loop

        make left and right equal to idx once the while loop has terminated

        now we will find the slice of the array with our k number of values closest to x...
        run a for loop k - 1 times:
            if left == 0, then idx was never reassigned a value and right and left now sit on top of each other
                so move right over by +1
            elif right has reached the end of the array and the absolute value of absolute value of (x - the value to the left of left)
            <= absolute value of (x - the value to the right of right),
                then we do not want to go right because any value to the right will be too large, even if it is close to x
                we want the smaller of possible values
            else:
                move right over by +1
        now left and right pointers should be standing at the beginning and end of our desired slice
        so return values in array from left to right