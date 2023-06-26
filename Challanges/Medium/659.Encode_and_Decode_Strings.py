"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Example1

Input: ["leet","code","love","you"]
Output: ["leet","code","love","you"]
Explanation:
One possible encode method is: "leet:;code:;love:;you"

Example2

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"
"""

######################################################
"""
@param: strs: a list of strings
@return: encodes a list of strings to a single string.
"""
def encode(strs):
    res = ""
    for s in strs:
        res = res + str(len(s)) + "#" + s
    return res

"""
@param: str: A string
@return: decodes a single string to a list of strings
"""
def decode1(st: str):
    res = []
    for i in range(len(st)-2):
        if st[i].isnumeric() and st[i+1] == "#":
            res.append(st[(i+2):(i+2+int(st[i]))])
            i += 2 + int(st[i])
    return res

def decode2(st: str):
    res, i = [], 0 
    
    while i < len(st):
        j = i
        while st[j] != "#":
            j += 1
        length = int(st[i:j])
        res.append(st[j + 1 : j + 1 + length])
        i = j + 1 + length

######################################################

strs1 = ["leet","code","love","you"]
strs2 = ["we", "say", ":", "yes"]

en1 = encode(strs1)
en2 = encode(strs2)

print(en1)
print(en2)
print("solution 1:")
dec1 = decode1(en1)
dec2 = decode1(en2)
print(dec1)
print(dec2)
##
print("solution 2:")
dec3 = decode1(en1)
dec4 = decode1(en2)
print(dec3)
print(dec4)