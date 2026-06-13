class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> map2;
        unordered_map<char, int> map1;
        int required = t.size();  // Total required characters to match
        int found = 0;  // Number of required characters currently matched
        int l = 0, minLen = INT_MAX, start = 0;

        // Build frequency map for `t`
        for (char c : t) {
            map2[c]++;
        }

        // Sliding window
        for (int r = 0; r < s.length(); r++) {
            if (map2.find(s[r]) != map2.end()) { // Only count relevant characters
                if (map1[s[r]] < map2[s[r]]) {
                    found++;  // Only count if it's needed
                }
                map1[s[r]]++;
            }

            // When all characters are found, try to shrink the window
            while (found == required) {
                // Update the minimum substring if found smaller
                if (r - l + 1 < minLen) {
                    minLen = r - l + 1;
                    start = l;
                }

                // Try to remove the leftmost character
                if (map2.find(s[l]) != map2.end()) {
                    if (map1[s[l]] == map2[s[l]]) {
                        found--;  // Reduce found count only if it was fully matching
                    }
                    map1[s[l]]--;
                }
                l++; // Move left pointer forward
            }
        }

        return (minLen == INT_MAX) ? "" : s.substr(start, minLen);
    }
};