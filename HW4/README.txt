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
        Time complexity: because we use binary search to find the number closest to x, followed by
        a while loop that runs k-1 times, the time complexity is O(logn + k-1) or just O(logn)
#3
    This algorithm takes an array (or heap) of nums and k, which will be the number of numbers
    to return.

    To begin, sort the array in place by calling python's sort() function, and sort it in reverse.
    This function has a time complexity of O(nlogn)

    Next, create an empty result list.

    Next, iterate through the sorted array up until k;
        append arr[i] to the result list
    return res

    overall this has a time complexity of O(nlogn) because we use the python sort() function to sort in place

#4
    This algorithm takes advantage of a deque data structure in python, which is a double ended queue

    Define and initialize the deque object, called deq

    initialize a variable cumSum to 0
    initialize a variable shortest to equal positive infinity

    loop through the length of the array:
        cumSum equals itself plus nums at i

        if cumSum >= k:
            reassign shortest to equal the minimum between itself and i + 1, or the current iterator value

        define and initialize a variable curr to equal a list of [-inf, +inf]

        while there are items in deq and ((cumSum - deq[-1][0]) >= k:
            curr equals the last item in deq
            pop the deq
        if curr at 0 does not equal -inf:
            shortest equals the minimum between itself and i - the element at position 1 in curr
        while there are items in deq and cumSum is less than or equal to element at [0][0] in deq:
            pop the deq from the left
        append left to the deq cumSum and the current iterator value as a list
        return -1 if shortest equals inf and was never reassigned, else return shortest


# 5
The solution provided for problem 5 is a brute force solution. It takes advantage of a dictionary
data structure to hold key:value pairs of list:result.

Define kThSmallestprimeFraction with parameters arr and k, where arr is an array of
increasing and sorted numbers, and k is the Kth smallest fraction to return.

Define and initialize an empty dictionary called dictionary

for num at i where i = 0 at first and goes until len(arr)
    for num at j where j = i + 1
        to the dictionary, add the numbers at arr[i] and arr[j] as a list to the dict's values,
        and assign the key to equal the result of arr[i]/arr[j]
Now define and initialize an array called sorted_results, and call on python's sorted(),
passing in the dictionary.keys() as an argument. This will create an array
of dictionary's keys in sorted order, in other words this will create an array
of sorted results for each nums[i]/nums[j], where the smallest result starts at the beginning
of the array.
From here, we can simply return the value (which will be a list of two nums: nums[i], nums[j])
at index sorted_results[k-1], because sorted_results[k-1] will give us the k'th smallest
result in the list, and we can use this result of division to retrieve the corresponding value
at that result's key in the dictionary.

This algorithm is not very efficient, and the more efficient algorithms are quite complex and
are not suitable for an interview. Therefore, the time complexity of this approach is
O(n^2 + nlog(n)), where n is the size of the array provided. O(n^2) because we use
a for loop within a for loop to calculate the result of arr[i]/arr[j] to add it to the dictionary
and nlog(n) because we call on python's sorted() function after calculating all fractions,
and that method has a complexity of nlog(n)