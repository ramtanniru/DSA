class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.map = defaultdict(TrieNode)
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.map:
                curr.map[ch] = TrieNode()
            curr = curr.map[ch]
        curr.isEnd = True 

    def search(self, word: str) -> bool:
        def dfs(node,idx):
            if idx==len(word):
                return node.isEnd
            if word[idx]==".":
                for trienode in node.map.values():
                    if dfs(trienode,idx+1):
                        return True
            if word[idx] in node.map:
                return dfs(node.map[word[idx]],idx+1)
            return False 
        return dfs(self.root,0) 