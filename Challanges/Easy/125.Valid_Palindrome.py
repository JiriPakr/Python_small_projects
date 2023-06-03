"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

 

Constraints:

    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.

"""
#######################################################
def isPalindrome1(s: str) -> bool:
    s = s.lower()
    aplhabet_ascii = range(97,123)
    nums_acsii = range(48,58)
    for c in s:
        if ord(c) not in aplhabet_ascii and ord(c) not in nums_acsii:
            s = s.replace(c,"")

    i,j = 0, len(s)-1
    while j>=0:
        print(s[j])
        print(s[i])
        if s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1
    return True


#######################################################
#result1 = isPalindrome1("A man, a plan, a canal: Panama")
result2 = isPalindrome1("0P")
#print(result1)
print(result2)