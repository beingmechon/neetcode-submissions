class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([char.lower() for char in s if char.isalnum()])
        # return s[:] == s[::-1]
        
        i = 0
        res = True
        
        while res and i < len(s) and s:
            # start, end = s[i], s[len(s)-i-1]
            # print(i)
            # print(s[i], s[len(s)-i-1])
            start, end = s[i], s[len(s)-i-1]
            if start == end:
              i += 1
              continue
            else:
              return not res

        return res
