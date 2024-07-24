class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque([])
        s = set(wordList)
        if endWord not in s:
            return 0
        s.add(beginWord)
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        queue.append((beginWord,0))
        while queue:
            word,pathLen = queue.popleft()
            if word not in s:
                continue
            s.remove(word)
            if word==endWord:
                return pathLen+1
            for i in range(len(word)):
                for j in alpha:
                    temp = word[:i]+j+word[i+1:]
                    if temp in s:
                        queue.append((temp,pathLen+1)) 
        return 0 