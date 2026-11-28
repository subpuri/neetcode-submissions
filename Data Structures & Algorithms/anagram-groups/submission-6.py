class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        o = {}
        for word in strs:
            l = [0]*26
            for ch in word:
                l[ord(ch) - ord('a')] += 1
            key = tuple(l)

            if key not in o:
                o[key] = []
            o[key].append(word)

        return list(o.values())

        