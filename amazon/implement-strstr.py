# Time Complexity = O(m+n)
# Space Complexity = O(n)
# m = size of haystack, n = size of needle
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack or len(haystack) < len(needle):
            return -1
        needleArr = self.createNeedleSuffixArray(needle)
        i = j = 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j > 0:
                j = needleArr[j-1]
            else:
                i += 1
        return i - j if j == len(needle) else -1

    def createNeedleSuffixArray(self, needle: str) -> List[str]:
        result = [0]*len(needle)
        i = 1
        j = 0
        while i < len(needle):
            if needle[i] == needle[j]:
                result[i] = j + 1
                i += 1
                j += 1
            elif j > 0:
                j = result[j-1]
            else:
                i += 1
        return result
