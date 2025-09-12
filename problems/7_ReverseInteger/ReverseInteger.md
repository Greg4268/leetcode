# 7. Reverse Integer

**Difficulty**: Medium
**Topics**: Strings
**LeetCode Link**: https://leetcode.com/problems/two-sum/description/

## Problem Statement

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range, then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

**Example:**
```
Input: x = -123
Output: -321
```

**Constraints:**
- `-231 <= x <= 231 - 1`

## Approach

My first solution is not the ideal however it is simple. Find whether positive or negative, convert to string, reverse, add sign and return as long as within size limit of integer. 

## Code Walkthrough - String Reversal 

```python
class Solution(object):
    def reverse(self, x):
        # max and min values for int 
        INT_MAX, INT_MIN = 2**32 - 1, -2**32 - 1

        # get sign 
        sign = -1 if x < 0 else 1
        # convert to string 
        x_str = str(abs(x))

        # reverse the string 
        reversed_str = x_str[::-1]
        # convert back to int and apply sign 
        result = sign * int(reversed_str)

        # return 0 only if reverse value is outside int bounds 
        return result if INT_MAX >= result >= INT_MIN else 0 
```

## Edge Cases Considered

## Related Problems

- Reverse Bits 

## Notes

---

