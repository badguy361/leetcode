"""
682. Baseball Game
You are keeping score for a baseball game with strange rules. 
The game consists of several rounds, where the scores of past rounds 
may affect future rounds' scores.

At the beginning of the game, you start with an empty record. 
You are given a list of strings ops, where ops[i] is the ith operation 
you must apply to the record and is one of the following:

An integer x - Record a new score of x.
"+" - Record a new score that is the sum of the previous two scores. 
It is guaranteed there will always be two previous scores.
"D" - Record a new score that is double the previous score. It is guaranteed 
there will always be a previous score.
"C" - Invalidate the previous score, removing it from the record. It is 
guaranteed there will always be a previous score.
Return the sum of all the scores on the record after applying all the operations.

Example 1:

Input: ops = ["5","2","C","D","+"]
Output: 30

Example 2:

Input: ops = ["5","-2","4","C","D","9","+","+"]
Output: 27

Constraints:
1 <= ops.length <= 1000
ops[i] is "C", "D", "+", or a string representing an integer in the range [-3 * 104, 3 * 104].
For operation "+"", there will always be at least two previous scores on the record.
For operations "C" and "D", there will always be at least one previous score on the record.
"""
# solution 1
from typing import List
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans_list = []
        for ope in operations:
            if ope == "C":
                ans_list.pop()
            elif ope == "D":
                ans_list.append(ans_list[-1]*2)
            elif ope == "+":
                ans_list.append(ans_list[-1] + ans_list[-2])
            else:
                ans_list.append(int(ope))
        return sum(ans_list)
