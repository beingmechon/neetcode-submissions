class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for _str in strs:
            encoded = _str+"a#a"
            encoded_str = encoded_str + encoded
        return encoded_str

    def decode(self, s: str) -> List[str]:
        words = []
        return [word for word in s.split("a#a")[:-1]]


            
