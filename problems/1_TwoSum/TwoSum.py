# First Solution 
# Brute Force O(n^2)
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)): # start index i + 1 to not go over duplicates 
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # return empty list if no solution found 

# Test the solution
nums = [2, 7, 11, 15]
target = 9
solution = Solution()
print("--- Brute Force Solution ---")
print("Expected answer: [0, 1]")
print("Solution answer: ", solution.twoSum(nums, target))
print("----------------------------")

# Second Solution 
# Two Pass Hashmap O(n)
class Solution2(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]] 
        return []

solution2 = Solution2()
print("--- 2Pass Hashmap Solution ---")
print("Expected answer: [0, 1]")
print("Solution answer: ", solution2.twoSum(nums, target))
print("------------------------------")