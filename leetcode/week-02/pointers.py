"""
You are given a positive integer array skill of even length n where skill[i] denotes the skill 
of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of 
each team is equal.

The chemistry of a team is equal to the product of the skills of the players on that team.

Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide 
the players into teams such that the total skill of each team is equal.

 

Example 1:

Input: skill = [3,2,5,1,3,4]
Output: 22
Explanation: 
Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team 
has a total skill of 6.
The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.
Example 2:

Input: skill = [3,4]
Output: 12
Explanation: 
The two players form a team with a total skill of 7.
The chemistry of the team is 3 * 4 = 12.
Example 3:

Input: skill = [1,1,2,3]
Output: -1
Explanation: 
There is no way to divide the players into teams such that the total skill of each team is equal.
"""


from typing import Counter, List


# class Solution:
#     def dividePlayers(self, skill: List[int]) -> int:
#         skill.sort()

#         skillTotal = sum(skill)
#         teams = len(skill) // 2

#         if skillTotal % teams != 0:
#             return -1

#         res = 0
#         teamSum = skillTotal // teams
            
        
#         left, right = 0, len(skill)-1

#         while left < right:
#             if skill[left] + skill[right] != teamSum:
#                 return -1
#             res += skill[left] * skill[right]

#             left += 1
#             right -= 1

#         print(res)


"""
A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', 
and 'u') and has all five vowels present in it.

Given a string word, return the number of vowel substrings in word.

Example 1:

Input: word = "aeiouu"
Output: 2
Explanation: The vowel substrings of word are as follows (underlined):
- "aeiouu"
- "aeiouu"
Example 2:

Input: word = "unicornarihan"
Output: 0
Explanation: Not all 5 vowels are present, so there are no vowel substrings.
Example 3:

Input: word = "cuaieuouac"
Output: 7
Explanation: The vowel substrings of word are as follows (underlined):
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
"""

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         left = 0

#         lengthString = 0
#         window = set()

#         for right in range(len(s) - 1):
#             # windowSize += s[right]

#             while s[right] in window:
#                 window.remove(s[left])

#                 left += 1
            
#             window.add(s[right])
#             lengthString = max(lengthString, right - left + 1)
        
#         return lengthString

# class Solution:
#     def countVowelSubstrings(self, word: str) -> int:
#         vowels = set("aeiou")
#         last_seen = {}
#         left = 0
#         count = 0

#         for right, ch in enumerate(word):
#             if ch not in vowels:
#                 last_seen.clear()
#                 left = right + 1
#                 continue

#             last_seen[ch] = right

#             if len(last_seen) == 5:
#                 count += min(last_seen.values()) - left + 1

#         print(count)




"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""


# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:

#         res = []

#         if len(p) > len(s):
#             print(res)

#         counter_p = Counter(p)
#         window = Counter()

#         lenOfP = len(p)

#         for i in range(len(s)):
#             window[s[i]] += 1

#             if i >= lenOfP:
#                 if window[s[i-lenOfP]] == 1:
#                     del window[s[i-lenOfP]]
#                 else:
#                     window[s[i-lenOfP]] -= 1
            
#             if window == counter_p:
#                 res.append(i-lenOfP+1)
            
#         print(res)



"""
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
"""

# class Solution:
#     def numberOfSubarrays(self, nums: List[int], k: int) -> int:
#         ans = 0

#         window = []

#         for i in range(len(nums)):
#             if nums[i] % 2 != 0:
#                 window.append(1)
#             else:
#                 window.append(0)

        
#         # left, right = 0, left + 1
        
#         for start in range(len(window)):
#             curr_sum = 0

#             for end in range(start, len(window)):
#                 curr_sum += window[end]

#                 if curr_sum == k:
#                     ans += 1

#                 if curr_sum > k:
#                     break

#         return ans



# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         res = []

#         currSum = 0

#         for i in range(len(nums)):
#             currSum += nums[i]
#             res.append(currSum)
        
#         print(res)


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        res = []

        currSum = 0
        for i in range(left, right+1):
            res.append(currSum)

            currSum += self.nums[i]

        
        return currSum


if __name__ == '__main__':
    ["NumArray", "sumRange", "sumRange", "sumRange"]
    [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]

