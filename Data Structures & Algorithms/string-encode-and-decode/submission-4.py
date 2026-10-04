class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for _str in strs:
            _len = str(len(_str))
            encoded = _len+"a#a"+_str
            encoded_str = encoded_str + encoded
        return encoded_str

    def decode(self, s: str) -> List[str]:
        word = []
        i = 0
        while i<len(s):
            j = s.find("a#a", i)
            num = int(s[i:j])
            start = j+3
            word.append(s[start:start+num])
            i = (start+num)

        return word

        # words = []
        # return [word for word in s.split("a#a")[:-1]]


            
