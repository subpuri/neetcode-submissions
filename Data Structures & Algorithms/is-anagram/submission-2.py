class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            sf = {}
            tf = {}
            for x in s:
                if x in sf:
                    sf[x] = sf[x]+1
                else:
                    sf[x] = 1
            for x in t:
                if x in tf:
                    tf[x] = tf[x]+1
                else:
                    tf[x] = 1
            for i in s:
                if sf[i] != tf.get(i, 0):
                    return False
            return True

        else:
            return False
              


        