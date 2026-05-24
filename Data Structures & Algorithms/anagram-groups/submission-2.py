class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for i in word:
                count[ord(i) - ord('a')] += 1
            final[tuple(count)].append(word)
        
        return list(final.values())