# Time Complexity = O(nk)
# Space Complexity = O(nk)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list)
        for string in strs:
            char_counts = [0] * 26
            for char in string:
                char_counts[ord(char) - ord('a')] += 1
            result[tuple(char_counts)].append(string)
        return result.values()
