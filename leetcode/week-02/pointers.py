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


from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        teamTotal = skill[0] + skill[-1]
        chemistrySum = 0

        for i in range(len(skill) / 2):
            pass




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


if __name__ == '__main__':
    word = "aeiouu"
    Solution().countVowelSubstrings(word)

