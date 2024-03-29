class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        s = s.lstrip()
        count = 0;
        s = list(s)

        for i in range(len(s)-1, 0, -1):
            if s[i] == " ":
                count = i + 1
                break
            if i == 0:
                count = 0
                break

        output = len(s) - count
      
        return output
      
        