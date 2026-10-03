class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for _str in strs:
            sorted_str = "".join(sorted(_str))
            if sorted_str in seen:
                seen[sorted_str].append(_str)
            else:
                seen[sorted_str] = [_str]
        return list(seen.values())

