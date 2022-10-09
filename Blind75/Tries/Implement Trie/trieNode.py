class TrieNode:
    def __init__(self):
        self.children = {}
        self.wordEnd = False
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        point = self.root
        
        for c in word:
            if c not in point.children:
                point.children[c] = TrieNode()
            point = point.children[c]
        point.wordEnd = True

    def search(self, word: str) -> bool:
        point = self.root
        
        for c in word:
            if c not in point.children:
                return False
            point = point.children[c]
        return point.wordEnd

    def startsWith(self, prefix: str) -> bool:
        point = self.root
        
        for c in prefix:
            if c not in point.children:
                return False
            point = point.children[c]
        return True


        
if __name__ == "__main__":
    obj = Solution()
    s = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    s1 = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    print(obj.wordBreak(s, wordDict))
