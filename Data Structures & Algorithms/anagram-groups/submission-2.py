class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = defaultdict(list)
        res: [List[List[str]]] = []
        for s in strs:
            ss = "".join(sorted(s))
            h[ss].append(s)
        
        return list(h.values())
