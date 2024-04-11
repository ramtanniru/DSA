class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for i in strs:
            cnt = [0]*26
            for j in i:
                cnt[ord(j)-ord('a')] += 1
            dic[tuple(cnt)].append(i)
        return sorted(dic.values())