"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

 

Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.

 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""

# Sol 1
def topKFrequent1(nums, k: int):
    res = {}

    for num in nums:
        res[num] = 1 + res.get(num, 0)

    return list(dict(sorted(res.items(), key=lambda x:x[1])).keys())[len(res)-k:]

# Sol 2
def topKFrequent2(nums, k: int):
    count = {}
    freq = [[] for i in range(len(nums)+1)]

    for num in nums:
        count[num] = 1 + count.get(num, 0)
    for num,c in count.items():
        freq[c].append(num)
        #print(freq)

    res = []
    for i in range(len(freq)-1,0,-1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
                
########################################################

nums = [1,1,1,2,2,3]
k = 2         
res = topKFrequent2(nums, k)
print(res)
