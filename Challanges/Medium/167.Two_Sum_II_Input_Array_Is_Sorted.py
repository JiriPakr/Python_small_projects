"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.


Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].


Constraints:

    2 <= numbers.length <= 3 * 104
    -1000 <= numbers[i] <= 1000
    numbers is sorted in non-decreasing order.
    -1000 <= target <= 1000
    The tests are generated such that there is exactly one solution.
"""
####################################################################
def twoSum1(numbers, target: int):
    i,j = 0, len(numbers)-1
    while j>i:
        if numbers[i] + numbers[j] > target:
            j -= 1
        elif numbers[i] + numbers[j] < target:
            i +=1
        else:
            return [i+1,j+1]    
    return [0,0]

####################################################################
def twoSum1(numbers, target: int):
    i,j = 0, len(numbers)-1
    while j>i:
        if numbers[i] + numbers[j] == target:
            return [i+1,j+1]
        if numbers[i] + numbers[j] > target:
            j -= 1
        if numbers[i] + numbers[j] < target:
            i +=1
    return [0,0]

####################################################################
def twoSum3(numbers, target: int):
    l, r = 0, len(numbers) - 1

    while l < r:
        curSum = numbers[l]+numbers[r]

        if curSum > target:
            r -= 1
        elif curSum < target:
            l += 1
        else:
            return [l + 1, r + 1]
    return []

####################################################################
numbers1 = [2,7,11,15]
target1 = 9             # Output: [1,2]
numbers2 = [2,3,4]
target2 = 6             # Output: [1,3]
numbers3 = [-1,0]
target3 = -1            # Output: [1,2]
numbers4 = [1,3,4,5,7,10,11]
target4 = 9             # Output:

print(twoSum1(numbers1,target1))
print(twoSum1(numbers2,target2))
print(twoSum1(numbers3,target3))
print(twoSum1(numbers4,target4))