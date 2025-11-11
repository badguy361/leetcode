"""
155. Min Stack

Design a stack that supports push, pop, top, and retrieving 
the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.

You must design a solution with O(1) time complexity for each function.

Constraints:

-231 ≤ val ≤ 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.

"""

# solution 1
"""
做法: 使用min遍歷stack
複雜度:
- 時間複雜度: O(n)
- 空間複雜度: O(n)
"""
# class MinStack:

#     def __init__(self):
#         self.stack = []

#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         return

#     def pop(self) -> None:
#         self.stack.pop()
#         return

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return min(self.stack)

# solution 2
"""
做法: push時同時push最小值
複雜度:
- 時間複雜度: O(1)
- 空間複雜度: O(n)
"""
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            self.minStack.append(min(val, self.minStack[-1]))
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
