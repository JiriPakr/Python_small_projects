"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

    1 <= n <= 45
"""
###########################################################
# DP
def climbStairs1(n: int) -> int:
    one, two = 1,1
    
    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp

    return one
###########################################################
# Fibonacci
def climbStairs2(n: int) -> int:
    x = [0] * (n+2)
    x[1] = 1
    for i in range(2, n+2):
        x[i] = x[i-1] + x[i-2]
    return x[n+1]
###########################################################

n1 = 5
n2 = 12

print(climbStairs1(n1))
print(climbStairs1(n2))
print(climbStairs2(n1))
print(climbStairs2(n2))