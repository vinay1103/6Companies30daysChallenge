from typing import List

# Approach: Brute Force, But mainly tests our CLEAN CODE Writing. Involves multiple Condition Checking
class Solution:
    def findAvg(self, img: List[List[int]], loc: List[int],m: int, n: int):
        deltaMovement = [[0,0], [0,+1], [+1,0], [0,-1],[-1,0],[+1,+1],[-1,-1],[+1,-1],[-1,+1]]
        sumVal = 0
        count = 0
        for i,j in deltaMovement:
            if loc[0] + i < 0 or loc[0] + i >= m or loc[1] + j < 0 or loc[1] + j >= n:
                continue
            sumVal += img[loc[0]+i][loc[1]+j]
            count += 1
        return sumVal//count
    
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(img)):
            tmp = []
            for j in range(len(img[0])):
                tmp.append(self.findAvg(img, [i,j], len(img), len(img[0])))
            res.append(tmp)
        return res