class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @lru_cache(None)
        def dfs(expr):
            results = []
            
            for i in range(len(expr)):
                if expr[i] in "+-*":
                    left = dfs(expr[:i])
                    right = dfs(expr[i+1:])
                    
                    for l in left:
                        for r in right:
                            if expr[i] == "+":
                                results.append(l + r)
                            elif expr[i] == "-":
                                results.append(l - r)
                            else:
                                results.append(l * r)
            
            # base case: it's a number
            if not results:
                results.append(int(expr))
            
            return results
        
        return dfs(expression)