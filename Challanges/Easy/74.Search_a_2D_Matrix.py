"""
You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.


Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -104 <= matrix[i][j], target <= 104
"""

####################################################################
def searchMatrix(matrix, target: int) -> bool:
    ROWS, COLS = len(matrix), len(matrix[0])
    top, bot = 0, ROWS-1

    while top <= bot:
        row = (top+bot) //2
        if matrix[row][COLS-1] < target:
            top = row + 1
        elif matrix[row][0] > target:
            bot = row - 1
        else:
            break

    if not (top <= bot):
        return False  
    row = (top + bot) //2
    l, r = 0, COLS-1
    while l <= r:
        m = (l+r) //2
        if matrix[row][m] < target:
            l = m + 1
        elif matrix[row][m] > target:
            r = m - 1
        else:
            return True
    return False
####################################################################
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target1 = 3     # Output: true
target2 = 13    # Output: false
print(searchMatrix(matrix, target2))

