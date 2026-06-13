class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        s = set()
        for w in wordList:
            s.add(w)
        q=deque([(beginWord,1)])
        if beginWord in s:
            s.remove(beginWord)
        while q:
            word, level = q.popleft()
            if word == endWord:
                return level
            for i in range(len(word)):
                ogC = word[i]
                for ch in range(ord('a'), ord('z')+1):
                    new_char = chr(ch)
                    if new_char == word[i]:
                        continue

                    new_word = word[:i] + new_char + word[i+1:]
                    if new_word in s:
                        q.append((new_word,level+1))
                        s.remove(new_word)
        return 0
                    


