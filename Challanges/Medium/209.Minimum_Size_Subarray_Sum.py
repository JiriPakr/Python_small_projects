"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 
Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,4,4]
Output: 0


Constraints:

    1 <= target <= 109
    1 <= nums.length <= 105
    1 <= nums[i] <= 104

 
Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""
import sys
#######################################################
def minSubArrayLen(target: int, nums) -> int:
  windowStart = 0
  curSum, minLen = 0, sys.maxsize

  for windowEnd in range(len(nums)):
    curSum += nums[windowEnd]

    while curSum >= target:
      minLen = min(minLen, windowEnd - windowStart + 1)
      curSum -= nums[windowStart]
      windowStart += 1
        
  if minLen == sys.maxsize:
    return 0
  return minLen

#######################################################
nums1 = [2,3,1,2,4,3]
nums2 = [1,4,4]
nums3 = [1,4,4]
nums4 = [1,2,3,4,5]
target1 = 7
target2 = 4
target3 = 11
target4 = 11

print(minSubArrayLen(target1, nums1))
print(minSubArrayLen(target2, nums2))
print(minSubArrayLen(target3, nums3))
print(minSubArrayLen(target4, nums4))