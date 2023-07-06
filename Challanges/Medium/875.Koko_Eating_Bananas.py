"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas,
she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 
Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23


Constraints:

    1 <= piles.length <= 104
    piles.length <= h <= 109
    1 <= piles[i] <= 109
"""
import sys
import math
###########################################
# Brute force
def minEatingSpeed(piles, h: int) -> int:
  ks = range(1,max(piles)+1)
  minK = sys.maxsize

  for k in ks:
    hours = 0
    for i in range(len(piles)):
        hours += math.ceil(piles[i]/ k)

    if hours <= h: 
        minK = min(minK, k)
    
  return minK

###########################################
def minEatingSpeed2(piles, h: int) -> int:
  ks = range(1,max(piles)+1)
  minK = sys.maxsize
  l,r = 1, len(ks)-1
  if len(piles) == 1 and piles[0] <= h:
    return 1

  while l <= r:
    m = (l + r) // 2
    hours = 0
    for i in range(len(piles)):
      hours += math.ceil(piles[i]/ ks[m])

    if hours <= h: 
      r = m - 1
      minK = min(minK, ks[m])
    elif hours > h:
      l = m + 1
      
  return minK
###########################################
def minEatingSpeed3(piles, h: int) -> int:
  l ,r = 1, max(piles)
  res = r

  while l <= r:
    k = (l + r) // 2
    hours = 0
    for p in piles:
      hours += math.ceil(p / k)

    if hours <= h:
      res = min(res, k)
      r = k - 1
    else:
      l = k + 1
  return res

###########################################
piles1 = [3,6,7,11]
piles2 = [30,11,23,4,20]
piles3 = [30,11,23,4,20]
piles4 =[312884470]
h1 = 8
h2 = 5
h3 = 6
h4 = 968709470

print("Result 1:")
print(minEatingSpeed(piles1,h1))
print(minEatingSpeed(piles2,h2))
print(minEatingSpeed(piles3,h3))
#print(minEatingSpeed(piles4,h4))

print("Result 2:")
print(minEatingSpeed2(piles1,h1))
print(minEatingSpeed2(piles2,h2))
print(minEatingSpeed2(piles3,h3))
print(minEatingSpeed2(piles4,h4))

print("Result 3:")
print(minEatingSpeed3(piles1,h1))
print(minEatingSpeed3(piles2,h2))
print(minEatingSpeed3(piles3,h3))
print(minEatingSpeed3(piles4,h4))