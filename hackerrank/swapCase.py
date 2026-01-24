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

    copy_s = []

    # first, we go through the entire string
    for i in range(len(s)):

        # checking if a character is upper
        if s[i].isupper():

            # converting uppercase letters to lowercase letters
            copy_s.append(s[i].lower())
        
        # next, checking if a character is lower
        elif s[i].islower():

            # then, convert to uppercase
            copy_s.append(s[i].upper())
        
        else:
            copy_s.append(s[i])

    # return a joined string
    return "".join(copy_s)



if __name__ == '__main__':
    s = 'Www.HackerRank.com'
    result = swap_case(s)
    print(result)


    