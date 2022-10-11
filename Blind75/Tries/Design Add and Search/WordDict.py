class WordDictionary:
    
    def __init__(self):
        self.root = {}
        self.end_symbol = '*'

    def addWord(self, word: str) -> None:
        current_node = self.root
        for idx in range(len(word)):
            if word[idx] not in current_node:
                current_node[word[idx]] = {}
                
            current_node = current_node[word[idx]]
            
        current_node[self.end_symbol] = {}

    def search(self, word: str) -> bool:
        def helper(idx, word, node):
            if idx == len(word):
                return self.end_symbol in node
            
            if word[idx] != '.':
                if word[idx] not in node:
                    return False
                return helper(idx+1, word, node[word[idx]])
            
            else:
                for key in node:
                    if helper(idx+1, word, node[key]) is True:
                        return True
                return False
            
            return True
        
        return helper(0, word, self.root)

if __name__ == "__main__":
    obj = Solution()
    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    print(obj.Trie(s, wordDict))