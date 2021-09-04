# Time Complexity = O(n^2)
# Space Complexity = O(1)
def longestPalindrome(string):
    start = end = 0
    for i in range(len(string)):
        length1 = expandAroundCenter(string, i, i)
        length2 = expandAroundCenter(string, i, i + 1)
        length = max(length1, length2)
        if (length > end - start):
            start = i - ((length - 1) // 2)
            end = i + (length // 2)
    return string[start:end+1]

def expandAroundCenter(string, left, right):
    while (left >= 0 and right < len(string) and string[left] == string[right]):
        left -= 1
        right += 1
    return right - left - 1