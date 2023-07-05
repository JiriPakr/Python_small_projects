"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

 
Constraints:

    1 <= nums.length <= 105
    nums[i] is either 0 or 1.
"""
import sys
##########################################################
def longestSubarray(nums) -> int:
    windowStart = 0
    zeroCount, maxLen = 0, -sys.maxsize

    for windowEnd in range(len(nums)):
        if nums[windowEnd] != 1:
            zeroCount += 1
        
        while zeroCount > 1:
            if nums[windowStart] != 1:
                zeroCount -= 1
            windowStart += 1
        
        maxLen = max(maxLen, windowEnd - windowStart)
    return maxLen
        

##########################################################
def longestSubarray2(nums) -> int:
    windowStart = 0
    maxLen = 0
    lastZero = -1

    for windowEnd in range(len(nums)):
        if nums[windowEnd] != 1:
            windowStart = lastZero + 1
            lastZero = windowEnd

        maxLen = max(maxLen, windowEnd - windowStart)
    return maxLen

##########################################################
nums1 = [0,1,1,1,0,1,1,0,1]     # Output: 5
nums2 = [1,1,1]                 # Output: 2

print(longestSubarray(nums1))
print(longestSubarray(nums2))
print(longestSubarray2(nums1))
print(longestSubarray2(nums2))