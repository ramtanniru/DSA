class Solution:
    def minDistance(self, str1: str, str2: str) -> int:
        # using cache
        # @cache
        # def rec(i, j):
        #     # base cases
        #     if i<0 and j<0:
        #         return 0
        #     if i < 0 or j < 0:
        #         return max(i,j)+1
        #     if str1[i] == str2[j]:
        #         return rec(i - 1, j - 1)
        #     else:
        #         # insert
        #         pos1 = 1 + rec(i, j - 1)
        #         # delete
        #         pos2 = 1 + rec(i - 1, j)
        #         # replace
        #         pos3 = 1 + rec(i - 1, j - 1)
        #         return min(pos1, pos2, pos3)
        # if not str1 and not str2:
        #     return 0
        # if not str1 or not str2:
        #     return max(len(str1),len(str2))
        # return rec(len(str1) - 1, len(str2) - 1) 

        # top-down memoisation
        def rec(i, j):
            # base cases
            if i<0 and j<0:
                return 0
            if i < 0 or j < 0:
                return max(i,j)+1
            if dp[i][j]!=-1:
                return dp[i][j]
            if str1[i] == str2[j]:
                dp[i][j] = rec(i - 1, j - 1)
            else:
                # insert
                pos1 = 1 + rec(i, j - 1)
                # delete
                pos2 = 1 + rec(i - 1, j)
                # replace
                pos3 = 1 + rec(i - 1, j - 1)
                dp[i][j] = min(pos1, pos2, pos3)
            return dp[i][j]
        if not str1 and not str2:
            return 0
        if not str1 or not str2:
            return max(len(str1),len(str2))
        dp = [[-1 for i in range(len(str2))] for j in range(len(str1))]
        return rec(len(str1) - 1, len(str2) - 1) 