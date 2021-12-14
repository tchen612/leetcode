# Time Complexity = O(max(m,n))
# Space Complexity = O(max(m,n))
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ptr1 = ptr2 = 0
        n1, n2 = len(version1), len(version2)
        while ptr1 < n1 or ptr2 < n2:
            digit1, ptr1 = self.get_next_chunk(version1, n1, ptr1)
            digit2, ptr2 = self.get_next_chunk(version2, n2, ptr2)
            if digit1 != digit2:
                return 1 if digit1 > digit2 else -1
        return 0

    def get_next_chunk(self, version: str, n: int, ptr: int) -> List[int]:
        if ptr > n - 1:
            return 0, ptr
        chunk_end = ptr
        while chunk_end < n and version[chunk_end] != '.':
            chunk_end += 1
        i = int(version[ptr:chunk_end]) if chunk_end != n - 1 else int(version[ptr:n])
        ptr = chunk_end + 1
        return i, ptr
