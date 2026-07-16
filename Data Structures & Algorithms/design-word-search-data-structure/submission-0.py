
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        
        current  = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.is_end = True


    def search(self, word: str) -> bool:
        
        def dfs(index, node):

            if index == len(word):
                return node.is_end
            
            c = word[index]

            if c == '.':
                for child in node.children.values():
                    if dfs(index+1, child):
                        return True
                return False
            
            if c not in node.children:
                return False
            return dfs(index+1, node.children[c])
        return dfs(0, self.root)