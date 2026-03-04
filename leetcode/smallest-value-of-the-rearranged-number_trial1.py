class Solution:
    def smallestNumber(self, num: int) -> int:
        digit_list = [int(d) for d in str(abs(num))]
        if num > 0:
            digit_list.sort()

            count = 0
            for i in range(len(digit_list)):
                if digit_list[i] == 0:
                    count += 1
            
            digit_list[0], digit_list[count] = digit_list[count], digit_list[0]

            return int("".join(str(d) for d in digit_list))
        else:
            digit_list.sort(reverse=True)
            val = "".join(str(d) for d in digit_list)
            
            return int("-" + val)