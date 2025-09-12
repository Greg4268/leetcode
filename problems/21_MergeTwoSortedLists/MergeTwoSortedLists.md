# 21. Merge Two Sorted Lists 

**Difficulty**: Easy
**Topics**: Linked List   
**LeetCode Link**: [https://leetcode.com/problems/merge-two-sorted-lists/]

## Problem Statement

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

**Example:**
```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

**Constraints:**
- `The number of nodes in both lists is in the range [0, 50]`
- `100 <= Node.val <= 100`
- `Both list1 and list2 are sorted in non-decreasing order`

## Approach

Traverse lists and add to master list based on sorting... Pretty simple 

## Code Walkthrough

```python
# Paste your Python solution here with comments
def solution_1(n):
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
            current = current.next
        
        # This line attaches ALL remaining nodes
        current.next = list1 or list2
        
        # Returns head of the complete merged list
        return dummy.next
```

## Notes

---
