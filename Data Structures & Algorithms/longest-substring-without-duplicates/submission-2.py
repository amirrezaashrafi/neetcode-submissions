class Solution:
    def lengthOfLongestSubstring(self, s):
        left = 0
        max_len = 0
        last_seen = {}
        
        for right in range(len(s)):
            if s[right] in last_seen and last_seen[s[right]] >= left:
                left = last_seen[s[right]] + 1
            
            last_seen[s[right]] = right

            curr_len = right - left + 1
            max_len = max(max_len, curr_len)

        return max_len
            