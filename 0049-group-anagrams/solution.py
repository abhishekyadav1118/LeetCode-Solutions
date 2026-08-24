from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Map sorted string to its list of anagrams
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sorting a string returns a list, join it back to make a string key
            sorted_key = "".join(sorted(s))
            anagram_map[sorted_key].append(s)
            
        # Return all the grouped lists
        return list(anagram_map.values())