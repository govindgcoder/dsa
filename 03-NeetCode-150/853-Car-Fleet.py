"""
There are n cars traveling to the same destination on a one-lane highway.
You are given two arrays of integers position and speed, both of length n.
- position[i] is the position of the ith car (in miles)
- speed[i] is the speed of the ith car (in miles per hour)
The destination is at position target miles.

A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination.

Examples:
        Input: target = 10, position = [1,4], speed = [3,2]
        Output: 1
        Explanation: The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet, meeting each other at 10, the destination.

        Example 2:
        Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
        Output: 3
        Explanation: The cars starting at 4 and 7 become a fleet at position 10. The cars starting at 1 and 0 never catch up to the car ahead of them. Thus, there are 3 car fleets that will arrive at the destination.

Constraints:
    n == position.length == speed.length.
    1 <= n <= 1000
    0 < target <= 1000
    0 < speed[i] <= 100
    0 <= position[i] < target
    All the values of position are unique.

Solution plan:

target = pos + vel.t => t = (target-pos)/vel

Sort the total array according to position. Pop the highest value, (since no previous value), build an array of time and put its time. Keep track of it as previous value.
Pop next element, get its time, if it is less than or equal to previous value, put its value equal to the previous value.
Repeat till the stack is empty.
Return number of unique values

Next thought after drawing this out:

sort the array of positions in decreasing order. Iterate. Check if current fleet's time is greater than stack top value, if so push the value to the stack. if stack empty, push the current value. repeat. finally return the stack's length.
"""

# note: To sort one array (the "secondary array") based on the order of a "primary array" in Python, you can use a combination of the zip() function, the sorted() function with a key, and list comprehension. 

def carFleet(target: float, position: list, speed: list):
    stk = []
    # sorting according the position array
    values = zip(position, speed)
    values = sorted(values, key=lambda x: x[0], reverse=True)
    for i in range(position.__len__()):
        currTime = (target - values[i][0]) / values[i][1]
        if stk:
            if stk[-1] < currTime:
                stk.append(currTime)
        else:
            stk.append(currTime)
    return stk.__len__()


print(carFleet(10, [4, 1, 0, 7], [2, 2, 1, 1]))
