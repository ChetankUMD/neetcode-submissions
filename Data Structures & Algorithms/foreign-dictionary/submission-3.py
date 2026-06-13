class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = {}
        s = set()
        for word in words:
            for ch in word:
                s.add(ch)
                indegree[ch] = 0
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            wordLength = min(len(w1), len(w2))
            if w1.startswith(w2) and len(w1) > len(w2):
                return ""
            for j in range(wordLength):
                if w1[j]!=w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        for c in s:
            indegree[c] = indegree.get(c, 0)
        print(graph)
        n = len(s)
        q = deque()
        topo=deque()

        for k,v in indegree.items():
            if indegree[k] == 0:
                q.append(k)
        
        # print(indegree)
        while q:
            node = q.popleft()
            topo.append(node)
            for ni in graph[node]:
                indegree[ni]-=1
                if indegree[ni]==0:
                    q.append(ni)
        # print(topo)
        if len(topo)!=n:
            return ""
        return "".join(topo)

