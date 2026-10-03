class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for _str in strs:
            # print("original: ", _str)
            sorted_str = "".join(sorted(_str))
            # print("sorted_str: ", sorted_str)
            # print("1", seen)
            if sorted_str in seen:
                # print("seen[sorted_str]: ", seen[sorted_str])
                seen[sorted_str].append(_str)
                # print("middle seen: ", seen)
            else:
                seen[sorted_str] = [_str]
            # print("2", seen)
        # print("3", list(seen.values()))
        return list(seen.values())

