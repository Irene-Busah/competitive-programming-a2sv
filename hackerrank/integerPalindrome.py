class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        A palindrome is a number that remains the same when reversed

        For example:
            x = 121

            Output: True
        """

        # return false if negative number
        if x < 0:
            return False

        reversed = 0
        copy_x = x

        while x > 0:
            reminder = x % 10 # 1
            new_num = reversed * 10 # 0
            reversed = new_num + reminder # 1
            x //= 10

            print(reminder, new_num)

        return reversed == copy_x


if __name__ == '__main__':
    print(Solution().isPalindrome(121))


# - First 3 months, $10 per hour, min 20 hrs per week.
# - After 3 months, $12 per hour, min 20 hrs per week.