"""
853. Car Fleet

There are n cars at given miles away from the starting mile 0,
traveling to reach the mile target.

You are given two integer arrays position and speed, where 
position[i] is the initial position of the i-th car and speed[i] 
is the speed of the i-th car (in miles per hour).

A car cannot pass another car, but it can catch up and then travel 
next to it at the speed of the slower car.

A car fleet is a single car or a group of cars driving next to each
other. The speed of the car fleet is the minimum speed of any car in
the fleet.

If a car catches up to a car fleet at the mile target, it will still
be considered as part of the car fleet.

Return the number of car fleets that will arrive at the destination.

Constraints:

n == position.length == speed.length
1 <= n <= 105
0 < target <= 106
0 <= position[i] < target
All the values of position are unique.
0 < speed[i] <= 106

Example 1:
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3

Example 2:
Input: target = 10, position = [3], speed = [3]
Output: 1

Example 3:
Input: target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1
"""
# solution 1
"""
做法: monotonic stack
複雜度:
- 時間複雜度: O(nlogn)
- 空間複雜度: O(n)
"""
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
cars = sorted(zip(position, speed), reverse=True)
fleets = 0
min_time = 0

for pos, spd in cars:
    time = (target - pos) / spd
    if time > min_time:
        fleets += 1
        min_time = time
print(fleets)
