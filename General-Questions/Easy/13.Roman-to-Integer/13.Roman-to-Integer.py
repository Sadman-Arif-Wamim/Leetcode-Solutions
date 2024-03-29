class Solution:
    def romanToInt(self, s: str) -> int:
        library = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        z = 0
        for i in range(len(s)-1):
            if library[s[i]] < library[s[i+1]]:
                z -= library[s[i]]
            else:
                z += library[s[i]]
        return z + library[s[-1]]
        
        