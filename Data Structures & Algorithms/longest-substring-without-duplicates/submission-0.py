class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # We should use two pointers/sliding window to solve this problem
        left = 0
        maxLength = 0
        prevChar = set()

        for right in range(len(s)):
            while s[right] in prevChar:
                prevChar.remove(s[left])
                left = left + 1
            else: 
                prevChar.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            
        return maxLength