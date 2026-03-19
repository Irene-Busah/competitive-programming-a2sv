class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        total = 0
        count = 0

        for i in range(k):
            if blocks[i] == 'W':
                count += 1 
            
        min_ops = count

        # slide window
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                count -= 1

            if blocks[i] == 'W':
                count += 1

            min_ops = min(min_ops, count)

        return min_ops


        