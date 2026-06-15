class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        h_ran = defaultdict(int)
        h_maz = defaultdict(int)

        for c in ransomNote:
            h_ran[c] = h_ran.get(c, 0) + 1
        
        for c in magazine:
            h_maz[c] = h_maz.get(c, 0) + 1
        print(h_ran)
        for key, value in h_ran.items():
            if key in h_maz and h_ran[key] <= h_maz[key]:
                continue
            else:
                return False
        
        return True