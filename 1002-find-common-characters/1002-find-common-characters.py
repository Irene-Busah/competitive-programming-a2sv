class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        results = []
        counters = []
        for i in range(len(words)):
            counter = Counter(words[i])
            counters.append(counter)
        
        for key in counters[0]:
            min_count = min(counter.get(key, 0) for counter in counters)

            if min_count > 0:
                results.extend([key] * min_count)
        
        return results