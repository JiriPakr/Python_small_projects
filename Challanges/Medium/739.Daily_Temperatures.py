"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i]
is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible,
keep answer[i] == 0 instead.


Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]


Constraints:

    1 <= temperatures.length <= 105
    30 <= temperatures[i] <= 100
"""
####################################################
def dailyTemperatures1(temperatures: int):
    stack = []
    for i in range(len(temperatures)-1):
        
        stack.append(temperatures[i])
        j = i+1
        temperatures[i] = 1
        if not j >= len(temperatures)-1:
            while stack and stack[-1] >= temperatures[j]:
                temperatures[i] += 1
                j += 1
        else:
            if stack and stack[-1] > temperatures[j]:
                temperatures[i] = 0

        stack.pop()
    temperatures[-1] = 0
    return temperatures
####################################################        
def dailyTemperatures2(temperatures: int):
    res = [0] * len(temperatures)
    stack = [] # pair: [temp, index]
    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackIdx = stack.pop()
            res[stackIdx] = (i - stackIdx)
        stack.append([t,i])
    return res
####################################################

temp1 = [73,74,75,71,69,72,76,73]   # Output: [1,1,4,2,1,1,0,0]
temp2 = [30,40,50,60]               # Output: [1,1,1,0]
temp3 = [30,60,90]                  # Output: [1,1,0]

print("Solutions 1:")
print(dailyTemperatures1(temp1))
print(dailyTemperatures1(temp2))
print(dailyTemperatures1(temp3))

temp1 = [73,74,75,71,69,72,76,73]   # Output: [1,1,4,2,1,1,0,0]
temp2 = [30,40,50,60]               # Output: [1,1,1,0]
temp3 = [30,60,90]                  # Output: [1,1,0]

print("Solutions 2:")
print(dailyTemperatures2(temp1))
print(dailyTemperatures2(temp2))
print(dailyTemperatures2(temp3))
