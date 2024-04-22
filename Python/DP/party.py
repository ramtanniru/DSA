# Intuition: a person can party either individually or can pair up. So we have two possibilities.
# Possibility-1: He can party individually and recursively call function for n-1 people as we need to exclude that person.
# Possibility-2: He can pair up with any of the person from the remaining people i.e., n-1 people.
# So we need to call function recursively for n-1 times for n-2 people as we need to exclude the pair. 

class Solution:
    def countFriendsPairings(self, n):
        def cnt(n):
            if n not in d:
                d[n] = (cnt(n-1) + (n-1)*cnt(n-2))%(10**9+7)
            return d[n]
        d = {0:1,1:1}
        return cnt(n)