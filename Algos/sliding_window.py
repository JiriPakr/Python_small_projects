"""
Find the max sum subarray of a fixed size K

Example input:
[4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
"""
#
# Fixed Size

import sys

def maxSumSubarray(arr, k):
    maxSum = -sys.maxsize
    currentSum = 0
    
    for i in range(len(arr)):
        currentSum += arr[i]
    
        if i >= k-1:
            maxSum = max(maxSum, currentSum)
            currentSum -= arr[i - (k-1)]

    return maxSum

#####################################
arr1 = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
k1 = 4
print("Result 1:", maxSumSubarray(arr1,k1))

#
# Dynamic size

def SmallestSubarrayGivenSum(arr, targetSum):
    minWindowSize = sys.maxsize
    windowStart = 0
    curSum = 0

    for windowEnd in range(len(arr)):
        curSum += arr[windowEnd]

        while curSum >= targetSum:
            minWindowSize= min(minWindowSize, windowEnd - windowStart + 1)
            curSum -= arr[windowStart]
            windowStart += 1
    return minWindowSize

#####################################
arr2 = [4, 2, 2, 7, 8, 1, 2, 8, 10]
targetSum1 = 8

#

print("Result 2:", SmallestSubarrayGivenSum(arr2, targetSum1))

# longest substring length with K distinct chars
def LongestSubStr(arr, k):
    hashSet = {}
    windowStart = 0
    maxLen = -sys.maxsize

    for windowEnd in range(len(arr)):
        hashSet[arr[windowEnd]] = 1 + hashSet.get(arr[windowEnd],0)

        while len(hashSet) > k:  
            if hashSet[arr[windowStart]] > 1:
                hashSet[arr[windowStart]] = hashSet.get(arr[windowStart],0) - 1
            else:
                hashSet.pop(arr[windowStart])
            windowStart += 1

        maxLen = max(maxLen, windowEnd - windowStart + 1)
    return maxLen


#####################################
arr3 = ["A", "A", "A", "H", "H", "I", "B", "C"]
k3 = 2

print("Result 3:", LongestSubStr(arr3, k3))


# https://leetcode.com/problems/longest-substring-without-repeating-characters/
def lengthOfLongestSubstring(s: str) -> int:
        hashSet = {}
        windowStart = 0
        maxLen = -sys.maxsize
        if len(s) < 1:
            return 0

        for windowEnd in range(len(s)):
            hashSet[s[windowEnd]] = 1 + hashSet.get(s[windowEnd],0)

            while hashSet[s[windowEnd]] > 1:  
                hashSet[s[windowStart]] = hashSet.get(s[windowStart],0) - 1
                windowStart += 1

            maxLen = max(maxLen, windowEnd - windowStart + 1)
        return maxLen
#####################################
s1 = "abcabcbb"
print("Result 3:", lengthOfLongestSubstring(s1))