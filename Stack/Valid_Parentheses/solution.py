# https://leetcode.com/problems/valid-parentheses/
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
# Time O(N) | Space O(N)
def isValid(s):
    closeToOpen = {")": "(", "}": "{", "]": "["}
    stack = []

    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            # Main part of the whole algo.
            else:
                # we will return false and the algo ends here : as the open and close brackets will also have to be in currect order.
                return False
        else:
            # in stack we will only store the open parentheses
            stack.append(c)

    return True if not stack else False


print(isValid("()[]{}"))
print(isValid("(]"))
