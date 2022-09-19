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