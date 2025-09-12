# 190. Reverse Bits

**Difficulty**: Easy
**Topics**: Binary  
**LeetCode Link**: [https://leetcode.com/problems/reverse-bits/]

## Problem Statement

Reverse bits of a given 32 bits signed integer.

**Example:**
```
Input: n = 43261596

Output: 964176192

Explanation:

Integer	Binary
43261596	00000010100101000001111010011100
964176192	00111001011110000010100101000000
```

**Constraints:**
- `0 <= n <= 231 - 2`
- `n is even`

## Approach

Simple solution: convert to 32 bit binary with leading 0s, reverse, return interger value 

## Code Walkthrough

```python
# Paste your Python solution here with comments
def solution_1(n):
    # format int(n) as 32 bit binary with leading values 
    b = format(n, '032b')
    # return the integer value of binary reversed (base 2)
    return int(b[::-1],2)
```

## Notes

[Any additional insights, optimizations you discovered, or things you learned while solving this problem]

---
