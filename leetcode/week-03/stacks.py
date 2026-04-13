from typing import List, Deque
from collections import deque


"""
You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.

Example 1:

Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".
Example 2:

Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.
"""


# class Solution:
#     def removeStars(self, s: str) -> str:
#         stack = []

#         for i in range(len(s)):
#             if s[i] != '*':
#                 stack.append(s[i])
#             else:
#                 stack.pop()
#         if len(stack) == 0:
#             print("")
#         else:
#             print("".join(stack))



"""
The Leetcode file system keeps a log each time some user performs a change folder operation.

The operations are described below:

"../" : Move to the parent folder of the current folder. (If you are already in the main folder, 
remain in the same folder).
"./" : Remain in the same folder.
"x/" : Move to the child folder named x (This folder is guaranteed to always exist).
You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

The file system starts in the main folder, then the operations in logs are performed.

Return the minimum number of operations needed to go back to the main folder after the change 
folder operations.


Example 1:

Input: logs = ["d1/","d2/","../","d21/","./"]
Output: 2
Explanation: Use this change folder operation "../" 2 times and go back to the main folder.
"""

# class Solution:
#     def minOperations(self, logs: List[str]) -> int:
#         stack = []

#         operations = ['../', './']

#         for i in range(len(logs)):
#             if logs[i] not in operations:
#                 stack.append(logs[i])
            
#             elif logs[i] == '../' and len(stack) > 0:
#                 stack.pop()
#         print(len(stack))



"""
You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and 
returns the number of requests that has happened in the past 3000 milliseconds (including the new 
request). Specifically, return the number of requests that have happened in the inclusive range
[t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

Example 1:

Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3
"""

# class RecentCounter:

#     def __init__(self):
#         self.queue = Deque()

#     def ping(self, t: int) -> int:
#         # adding a new request
#         self.queue.append(t)

#         # removing the older requests
#         while self.queue[0] < t - 3000:
#             self.queue.popleft()

#         return len(self.queue)
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)



"""
For a stream of integers, implement a data structure that checks if the last k integers parsed in the stream are equal to value.

Implement the DataStream class:

DataStream(int value, int k) Initializes the object with an empty integer stream and the two integers value and k.
boolean consec(int num) Adds num to the stream of integers. Returns true if the last k integers are equal to value, and 
false otherwise. If there are less than k integers, the condition does not hold true, so returns false.
 

Example 1:

Input
["DataStream", "consec", "consec", "consec", "consec"]
[[4, 3], [4], [4], [4], [3]]
Output
[null, false, false, true, false]

Explanation
DataStream dataStream = new DataStream(4, 3); //value = 4, k = 3 
dataStream.consec(4); // Only 1 integer is parsed, so returns False. 
dataStream.consec(4); // Only 2 integers are parsed.
                      // Since 2 is less than k, returns False. 
dataStream.consec(4); // The 3 integers parsed are all equal to value, so returns True. 
dataStream.consec(3); // The last k integers parsed in the stream are [4,4,3].
                      // Since 3 is not equal to value, it returns False.
"""


# class DataStream:

#     def __init__(self, value: int, k: int):
#         self.value = value
#         self.k = k
#         self.count = 0

#     def consec(self, num: int) -> bool:
#         if num == self.value:
#             self.count += 1
#         else:
#             self.count = 0
        
#         return self.count >= self.k


"""
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] 
in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
"""

# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         next_greater = {}
#         stack = []

#         # Compute next greater for each number in nums2
#         for num in nums2:
#             while stack and num > stack[-1]:
#                 prev = stack.pop()
#                 next_greater[prev] = num
#             stack.append(num)

#         # For elements that have no next greater
#         while stack:
#             prev = stack.pop()
#             next_greater[prev] = -1

#         # Build result for nums1
#         return [next_greater[num] for num in nums1]



"""
There are n people in a line queuing to buy tickets, where the 0th person is at the front of the 
line and the (n - 1)th person is at the back of the line.

You are given a 0-indexed integer array tickets of length n where the number of tickets that the 
ith person would like to buy is tickets[i].

Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time 
and has to go back to the end of the line (which happens instantaneously) in order to buy more 
tickets. If a person does not have any tickets left to buy, the person will leave the line.

Return the time taken for the person initially at position k (0-indexed) to finish buying tickets.

Example 1:

Input: tickets = [2,3,2], k = 2

Output: 6

Explanation:
The queue starts as [2,3,2], where the kth person is underlined.
After the person at the front has bought a ticket, the queue becomes [3,2,1] at 1 second.
Continuing this process, the queue becomes [2,1,2] at 2 seconds.
Continuing this process, the queue becomes [1,2,1] at 3 seconds.
Continuing this process, the queue becomes [2,1] at 4 seconds. Note: the person at the front left the queue.
Continuing this process, the queue becomes [1,1] at 5 seconds.
Continuing this process, the queue becomes [1] at 6 seconds. The kth person has bought all their 
tickets, so return 6.

"""


# class Solution:
#     def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
#         count = 0

#         while tickets[k] != 0:
#             for i in range(len(tickets)):
#                 if tickets[i] > 0:
#                     tickets[i] -= 1
#                     count += 1

#                     if tickets[k] == 0:
#                         break
        
#         print(count)



"""
Given an array of integers temperatures represents the daily temperatures, return an array answer 
such that answer[i] is the number of days you have to wait after the ith day to get a warmer 
temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
"""


# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         stack = []

#         ans = [0] * len(temperatures)

#         for i, temp in enumerate(temperatures):
#             while stack and temperatures[stack[-1]] < temp:
#                 prev_index = stack.pop()
#                 ans[prev_index] = i - prev_index
#             stack.append(i)
        
#         return ans


"""
Given a string s, find the first non-repeating character in it and return its index. If it does not 
exist, return -1.

 

Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1
"""

# class Solution:
#     def firstUniqChar(self, s: str) -> int:

#         # newS = s

#         d = deque()

#         mapper = {}

#         # print(s.index('o'))

#         for i in range(len(s)):
#             if s[i] not in mapper:
#                 mapper[s[i]] = 1
#             else:
#                 mapper[s[i]] += 1
        
#         for ch in s:
#             if mapper[ch] == 1:
#                 d.append(ch)
                
#         if d:
#             ele = s.index(d.popleft())
#             print(ele)
#         else:
#             print(-1)


"""
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater 
number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you 
could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

 

Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
"""


# class Solution:
#     def nextGreaterElements(self, nums: List[int]) -> List[int]:
#         ans = [-1] * len(nums)

#         stack = []

#         for i in range(2 * len(nums)):
#             # stack.append(nums[i])
#             while stack and nums[stack[-1]] < nums[i % len(nums)]:
#                 idx = stack.pop()
#                 ans[idx] = nums[i % len(nums)]
            
#             if i < len(nums):
#                 stack.append(i)
            
#         print(ans)



"""
You are given an array of strings tokens that represents an arithmetic expression in a 
Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        operations = ['+', '-', '*', '/']

        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:  # division
                    stack.append(int(a / b))
        
        return stack[0]
          

if __name__ == '__main__':
    tokens = ["2","1","+","3","*"]

    Solution().evalRPN(tokens)
