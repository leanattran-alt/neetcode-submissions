class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        countT = {}
        window = {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1

        have, need = 0, len(countT)
        left = 0
        minLen = float("inf")
        result = [-1, -1]

        for right in range(len(s)):
                c = s[right]
                window[c] = window.get(c, 0) + 1
                
                if c in countT and window[c] == countT[c]:
                    have += 1
                
                while have == need:
                    if right - left + 1 < minLen:
                        minLen = right - left + 1
                        result = [left, right]

                    window[s[left]] -= 1

                    if s[left] in countT and window[s[left]] < countT[s[left]]:
                        have -= 1
                        
                    left += 1
                
        l, r = result  
        return s[l:r + 1] if minLen != float("inf") else""







