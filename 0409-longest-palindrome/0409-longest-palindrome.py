class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=0
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        for ch in freq:
            count+=(freq[ch]//2)*2
        if count<len(s):
            count+=1
        return count