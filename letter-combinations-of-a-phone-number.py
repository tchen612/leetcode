# Time Complexity = O(4^n)
# Space Complexity = O(4^n)
def letterCombinations(digits):
    mappings = {
        '2': 'abc', 
        '3': 'def', 
        '4': 'ghi', 
        '5': 'jkl', 
        '6': 'mno', 
        '7': 'pqrs', 
        '8': 'tuv', 
        '9': 'wxyz'
    }
    all_combinations = [''] if digits else []
    for digit in digits:
        current_combinations = list()
        for letter in mappings[digit]:
            for combination in all_combinations:
                current_combinations.append(combination + letter)
        all_combinations = current_combinations
    return all_combinations