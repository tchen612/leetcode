# Time Complexity = O(n+k)
# Space Complexity = O(k)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        dict_t = Counter(t)
        len_t = len(dict_t)
        filtered_s = []
        for i, char in enumerate(s):
            if char in dict_t:
                filtered_s.append((i, char))
        left, right = 0, 0
        formed = 0
        window_counts = {}
        ans = float("inf"), None, None
        while right < len(filtered_s):
            character = filtered_s[right][1]
            window_counts[character] = window_counts.get(character, 0) + 1
            if window_counts[character] == dict_t[character]:
                formed += 1
            while left <= right and formed == len_t:
                character = filtered_s[left][1]
                end = filtered_s[right][0]
                start = filtered_s[left][0]
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)

                window_counts[character] -= 1
                if window_counts[character] < dict_t[character]:
                    formed -= 1
                left += 1
            right += 1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
