# 187. Repeated DNA Sequences

from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()

        # Approach: Check if Substring of 10 chars is present in the subsequent string, done using String Slicing.
        for i in range(10,len(s)):
            if s[i-10:i] in s[i-9:]:
                res.add(s[i-10:i])
        return list(res)