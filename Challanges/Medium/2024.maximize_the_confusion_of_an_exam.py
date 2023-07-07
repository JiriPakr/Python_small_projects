"""
A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. 
He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).

You are given a string answerKey, where answerKey[i] is the original answer to the ith question. 
In addition, you are given an integer k, the maximum number of times you may perform the following operation:

    Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').

Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.
 

Example 1:

Input: answerKey = "TTFF", k = 2
Output: 4
Explanation: We can replace both the 'F's with 'T's to make answerKey = "TTTT".
There are four consecutive 'T's.

Example 2:

Input: answerKey = "TFFT", k = 1
Output: 3
Explanation: We can replace the first 'T' with an 'F' to make answerKey = "FFFT".
Alternatively, we can replace the second 'T' with an 'F' to make answerKey = "TFFF".
In both cases, there are three consecutive 'F's.

Example 3:

Input: answerKey = "TTFTTFTT", k = 1
Output: 5
Explanation: We can replace the first 'F' to make answerKey = "TTTTTFTT"
Alternatively, we can replace the second 'F' to make answerKey = "TTFTTTTT". 
In both cases, there are five consecutive 'T's.

 
Constraints:

    n == answerKey.length
    1 <= n <= 5 * 104
    answerKey[i] is either 'T' or 'F'
    1 <= k <= n
"""
import sys, collections
###############################################################
def maxConsecutiveAnswers(answerKey: str, k: int) -> int:
  options = ["T", "F"]
  res = []

  for op in options:
    windowStart = 0
    curLen, maxLen = 0, -sys.maxsize
    curK = 0
    for windowEnd in range(len(answerKey)):
        if answerKey[windowEnd] == op:
          curLen += 1
        else:
          curLen += 1
          curK += 1

        while curK > k:
          
          if answerKey[windowStart] != op:
            curK -= 1
          windowStart += 1
          curLen -= 1
        maxLen = max(maxLen, curLen)
    res.append(maxLen)
  return max(res)
            
###############################################################
def maxConsecutiveAnswers2(answerKey: str, k: int) -> int:
  max_size = k
  count = collections.Counter(answerKey[:k])

  windowStart = 0
  for windowEnd in range(k, len(answerKey)):
    count[answerKey[windowEnd]] += 1

    while min(count["T"], count["F"]) > k:
      count[answerKey[windowStart]] -= 1
      windowStart += 1
    
    max_size = max(max_size, windowEnd - windowStart + 1)

  return max_size

###############################################################
def maxConsecutiveAnswers3(answerKey: str, k: int) -> int:
  n = len(answerKey)
  left, right = k, n
  
  def isValid(size):
    counter = collections.Counter(answerKey[:size])
    if min(counter["T"], counter["F"]) <= k:
      return True
    for i in range(size, n):
      counter[answerKey[i]] += 1
      counter[answerKey[i - size]] -= 1
      if min(counter["T"], counter["F"]) <= k:
        return True
    return False
  
  while left < right:
    mid = (left + right + 1) // 2

    if isValid(mid):
      left = mid
    else:
      right = mid - 1

  return left

###############################################################
answerKey1 = "TTFF"       # Output: 4
k1 = 2
answerKey3 = "TFFT"       # Output: 3
k2 = 1
answerKey2 = "TTFTTFTT"   # Output: 5
k3 = 1

print("Result 1:")
print(maxConsecutiveAnswers(answerKey1, k1))
print(maxConsecutiveAnswers(answerKey2, k2))
print(maxConsecutiveAnswers(answerKey3, k3))
print("Result 2:")
print(maxConsecutiveAnswers2(answerKey1, k1))
print(maxConsecutiveAnswers2(answerKey2, k2))
print(maxConsecutiveAnswers2(answerKey3, k3))
print("Result 3:")
print(maxConsecutiveAnswers3(answerKey1, k1))
print(maxConsecutiveAnswers3(answerKey2, k2))
print(maxConsecutiveAnswers3(answerKey3, k3))