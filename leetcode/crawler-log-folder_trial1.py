class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        operations = ['../', './']

        for i in range(len(logs)):
            if logs[i] not in operations:
                stack.append(logs[i])
            
            elif logs[i] == '../' and len(stack) > 0:
                stack.pop()
        return len(stack)
        