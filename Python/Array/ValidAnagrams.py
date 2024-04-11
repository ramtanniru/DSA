class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Method-1:
        d = dict()
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i in t:
            if i in d:
                d[i] -= 1
            else:
                return False
        for i in d:
            if d[i]!=0:
                return False
        return True

        # Method-2:
        map_1 = Counter(s)
        map_2 = Counter(t)

        return map_1==map_2
        