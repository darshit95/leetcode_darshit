class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                first = s[i+1:j+1]
                second = s[i:j]
                return first == first[::-1] or second == second[::-1]
            i += 1; j -= 1
        return True