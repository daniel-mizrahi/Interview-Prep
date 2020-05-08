class TrieNode():
    def __init__(self, value = None):
        self.val = value
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        temp = self.root
        for c in word:
            if c not in temp.children:
                temp.children[c] = TrieNode(c)
            temp = temp.children[c]
        temp.isWord = True
                    
    def search(self, word: str) -> bool:
        temp = self.root
        for c in word:
            if c in temp.children:
                temp = temp.children[c]
            else:
                return False
        return True if temp.isWord else False

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for c in prefix:
            if c in temp.children:
                temp = temp.children[c]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
