"""
150. Evaluate Reverse Polish Notation

Given a string array tokens, return the result of evaluating the 
RPN expression.


Constraints:

1 <= tokens.length <= 104
tokens[i] is either an integer or an operator ('+', '-', '*', or '/').
Each integer in the tokens array will be an integer in the range [-200, 200].
"""

# solution 1
"""
做法:
使用stack
複雜度:
- 時間複雜度: O(n)
- 空間複雜度: O(n)
"""
tokens = ["2", "1", "+", "3", "*"]
RPN = []
for token in tokens:
    if token in "+-*/":
        second = RPN.pop()
        first = RPN.pop()
        if token == "+":
            RPN.append(int(first)+int(second))
        elif token == "-":
            RPN.append(int(first)-int(second))
        elif token == "*":
            RPN.append(int(first)*int(second))
        elif token == "/":
            RPN.append(int(int(first)/int(second)))
    else:
        RPN.append(token)
print(int(RPN[0]))
