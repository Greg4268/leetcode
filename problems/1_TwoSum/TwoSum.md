# 1. Two Sum

**Difficulty**: Easy  
**Topics**: Array, Hash Table
**LeetCode Link**: https://leetcode.com/problems/two-sum/description/

## Problem Statement

Given an array of integers `nums` and an integer `target`, return indiices of the two numbers such that they add up to `target`. 

You may assume that each input would have exactly one solution, and you may not use the same element twice. 

You can return the answer in any order.

**Example:**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Constraints:**
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists 

## Approach

There are two main approaches to take when solving Two Sum. The first method, brute force, typically being the most common. This approach uses a nested for loop to check each element combination to see if each index will sum to the target value. With a time complexity of O(n^2), it is a reasonable solution but we can do better. The second solution is a two-pass hashmap with a time and space complexity of O(n). The First pass will store the values of the array as keys within a hashmap and the value being it's index. The second pass will calculate the complement value which is then checked for within the hashmap. 

## Code Walkthrough - Brute Force

```python
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)): # outer loop i 
            for j in range(i + 1, len(nums)): # start index j = i + 1 to not go over duplicates 
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # return empty list if no solution found 
```
## Code Walkthrough - Two Pass Hashmap 

```python
class Solution2(object):
    def twoSum(self, nums, target):
        hashmap = {} # initialize hashmap to store key-value pairs 
        for i in range(len(nums)): 
            hashmap[nums[i]] = i # loop through array added each array value as key in hashmap 

        for i in range(len(nums)):
            complement = target - nums[i] # create compliment var to check for in hashmap 
            if complement in hashmap and hashmap[complement] != i: # is complement in hashmap and not the same as i? 
                return [i, hashmap[complement]] # return the indices 
        return [] # reutrn empty list if no solution 
```
**Key Variables:**
- `hashmap`: stores the values of the array as keys with their indices as values for a fast lookup 
- `complement`: used in second pass to check against in hashmap 

## Code Walkthrough - One Pass Hashmap 

```python
class Solution3(object):
    def twoSum(self, nums, target):
        hashmap = {} # init hashmap
        for i in range(len(nums)): # loop through length of array 
            if target - nums[i] in hashmap: # check if complement value is in the hashmap already 
                return [hashmap[target - nums[i]], i] # if it is, return indices
            hashmap[nums[i]] = i # otherwise add nums[i] and continue to next 
        return [] # return empty if not found 
```

## Edge Cases Considered

- Given the description, the only edge case to consider is no two sum in the array equaling the target which means you should return an empty array 

## Related Problems

- 3Sum
- 4Sum 

## Notes

---
