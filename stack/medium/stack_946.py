"""
946. Validate Stack Sequences

Given two integer arrays pushed and popped each with distinct values, 
return true if this could have been the result of a sequence of push 
and pop operations on an initially empty stack, or false otherwise.

Example 1:
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Example 2:
Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.

Constraints:
1 <= pushed.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed is a permutation of popped.
pushed and popped have distinct values.
"""
# solution 1:
from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        check = []
        for i in pushed:
            check.append(i)
            while check[-1] == popped[0]:
                check.pop()
                popped.pop(0)
                if not check:
                    break
        return not check
