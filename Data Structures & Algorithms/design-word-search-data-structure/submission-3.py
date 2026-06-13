class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] =TrieNode()
            cur = cur.children[c]
        
        cur.endOfWord = True
            

    def search(self, word: str) -> bool:
        def dfs(j, node):
            for i in range(j,len(word)):
                if word[i]=='.':
                    for n in node.children.values():
                        if dfs(i+1,n):
                            return True
                    return False
                else:
                    if word[i] not in node.children:
                        return False
                    node = node.children[word[i]]
            return node.endOfWord
                

        return dfs(0, self.root)
