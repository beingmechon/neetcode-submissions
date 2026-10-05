class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([char.lower() for char in s if char.isalnum()])
        # return s[:] == s[::-1]
        _len = len(s)
        res = True
        i = 0
        while res and i<=(_len/2) and s:
            # print(i, _len-1-i)
            # print(i)
            if s[i] == s[_len-1-i]:
                i += 1
                continue 
            else:
                return not res
            
        
        return res


        # for i in range(_len/2):
        #     if s[i] == s[_len-i]:
                