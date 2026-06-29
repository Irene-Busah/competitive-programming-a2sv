class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        result = []

        for i in range(1, len(searchWord) + 1):
            prefix = searchWord[:i]

            # grab all products that start with this prefix, sort them, take top 3
            matches = sorted([p for p in products if p.startswith(prefix)])
            result.append(matches[:3])

        return result