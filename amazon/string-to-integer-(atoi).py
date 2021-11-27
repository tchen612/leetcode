# Time Complexity = O(n)
# Space Complexity = O(1)
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        sign = -1 if s[0] == '-' else 1
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        result = 0
        for char in s:
            if not char.isdigit():
                break
            result = result * 10 + ord(char) - ord('0')
        return max(-2**31, min(sign * result, 2**31-1))
