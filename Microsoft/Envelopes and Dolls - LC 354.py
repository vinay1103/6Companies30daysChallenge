# 354. Russian Doll Envelopes

from typing import List
from bisect import bisect_left

class Solution:
    # Longest Increasing Subsequence (LIS) using BINARY SEARCH approach (learnt while solving this problem)
    def LIS(self, heights: List[int]) -> int:
        finalList = []
        for h in heights:
            if not finalList or h > finalList[-1]:
                finalList.append(h)
            else:
                ind = bisect_left(finalList, h)
                finalList[ind] = h
        return finalList

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Final Approach
        
        # Sort envelopes based on width, and then height in Desc (so that we choose the best among similar width)
        envNew = sorted(envelopes, key = lambda x: (x[0], -x[1]))
        
        # Store all heights of this sorted List seperately
        heights = [dim[1] for dim in envNew]

        # return the length of LIS list of this heights (since widths are already taken care of during sorting)
        return len(self.LIS(heights))
    
    #--------------------------------------------------------------------------------------------------------------
        # Initial Approach - Brute Force (Not practised LIS much)
        # ls = [[(ele[0] + ele[1])/2, ele] for ele in envelopes]
        # lsNew = sorted(ls, key = lambda x: x[0])
        # count = 0
        # for i in range(len(lsNew)-1):
        #     for j in range(i+1, len(lsNew)):
        #         if lsNew[i][1][0] < lsNew[j][1][0] and lsNew[i][1][1] < lsNew[j][1][1]:
        #             count += 1
        #             break
        # return count + 1