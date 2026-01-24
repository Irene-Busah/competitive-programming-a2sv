"""
You are given a string and your task is to swap cases. In other words, 
convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  

Function Description
Complete the swap_case function in the editor below.
swap_case has the following parameters:

string s: the string to modify

Returns
string: the modified string, s.

Input Format
A single line containing a string .
"""


def swap_case(s):
    """
    Sawps the cases of letters in the string
    """

    copy_s = s

    # first, we go through the entire string
    for i in range(len(s)):
        if s[i].isupper():
            copy_s[i].lower()
            print(copy_s[i].lower())
        elif s[i].islower():
            copy_s[i].upper()
            print(copy_s[i].upper())

    return copy_s

if __name__ == '__main__':
    s = 'Pythonist 2'
    result = swap_case(s)
    print(result)