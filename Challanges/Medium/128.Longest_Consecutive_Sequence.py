"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.


Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

 
Constraints:

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
"""
#################################################
def longestConsecutive1(nums) -> int:
    nums_set = set(nums)
    result = 0
    for num in nums:
        if (num-1) not in nums_set: # check if its sequence start
            length = 1
            next_num = num+1
            while next_num in nums_set:
                length +=1
                next_num +=1  
            if length > result:
                    result = length

    return result
#################################################
def longestConsecutive2(nums) -> int:
    numSet = set(nums)
    longest = 0
    for n in nums:
        # check if its sequence start
        if (n-1) not in numSet: 
            length = 0
            while (n + length) in numSet:
                length +=1
        longest = max(length, longest)

    return longest
#################################################

nums1 = [100,4,200,1,3,2]       # output = 4
nums2 = [0,3,7,2,5,8,4,6,0,1]   # output = 9
print(longestConsecutive1(nums1))
print(longestConsecutive1(nums2))
print(longestConsecutive2(nums1))
print(longestConsecutive2(nums2))