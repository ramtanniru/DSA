from collections import defaultdict
class TrieNode:
    def __init__(self) -> None:
        self.isEnd = False
        self.map = defaultdict(TrieNode)
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    def insert(self,word):
        curr = self.root
        for ch in word:
            if ch not in curr.map:
                curr.map[ch] = TrieNode()
            curr = curr.map[ch]
        curr.isEnd = True
    def search(self,word):
        curr = self.root
        for ch in word:
            if ch not in curr.map:
                return False
            curr = curr.map[ch]
        return curr.isEnd 
    def startsWith(self,word):
        curr = self.root
        for ch in word:
            if ch not in curr.map:
                return False
            curr = curr.map[ch]
        return True 

obj = Trie()
words = ['hi','hello','hey','who']
w = 'he'
for word in words:
    obj.insert(word)
print(obj.search(w))
print(obj.startsWith(w)) 
