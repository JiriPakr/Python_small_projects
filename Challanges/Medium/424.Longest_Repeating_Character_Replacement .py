"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 
Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.

 
Constraints:

    1 <= s.length <= 105
    s consists of only uppercase English letters.
    0 <= k <= s.length
"""
import sys
###################################################
def characterReplacement(s: str, k: int) -> int:
    hashSet = {}
    windowStart = 0
    maxLen = -sys.maxsize

    for windowEnd in range(len(s)):
        hashSet[s[windowEnd]] = 1 + hashSet.get(s[windowEnd], 0)
    
        while windowEnd - windowStart - max(list(hashSet.values())) >= k:
            hashSet[s[windowStart]] = hashSet.get(s[windowStart], 0) - 1
            windowStart += 1

        maxLen = max(maxLen, windowEnd - windowStart + 1)

    return maxLen

###################################################
def characterReplacement2(s: str, k: int) -> int:
    count = {}
    res = 0

    l = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)

        while (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)
    return res

###################################################
def characterReplacement3(s: str, k: int) -> int:
    count = {}
    res = 0

    l = 0
    maxf = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])

        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)
    return res

###################################################
s1 = "ABAB" 
k1 = 2
s2 = "AABABBA"
k2 = 1

print(characterReplacement(s1, k1))
print(characterReplacement(s2, k2))
print(characterReplacement2(s1, k1))
print(characterReplacement2(s2, k2))
print(characterReplacement3(s1, k1))
print(characterReplacement3(s2, k2))