from typing import List
from math import sqrt

class Solution:
    def EuclideanDistance(self, circleCenter: List[int], squareCenter: List[int]):
        return sqrt((circleCenter[0] - squareCenter[0])**2 + (circleCenter[1]-squareCenter[1])**2)
    
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:

    # What I tried using:
    # Distance between Circle Center & Rectangle Center should be less than largest distance possible (Radius + Half Diagonal Length) for Overlap.

        # squareCenter = [(x1+x2)/2, (y1+y2)/2]
        # print(squareCenter)
        
        # length = abs((x1-x2)/2)
        # breadth = abs((y1-y2)/2)
        
        # halfDiagonalLeng = sqrt(length**2 + breadth**2)
        # print(halfDiagonalLeng)
        
        # centersDistance = self.EuclideanDistance([xCenter,yCenter], squareCenter)
        # print(centersDistance)

        # if (centersDistance > radius + halfDiagonalLeng):
        #     return False
        # else:
        #     return True

    # Mistakes:
    # Started Solving keeping Square in mind instead of Rectangle, (Human-Error), proceed in wrong direction.
    # Missed EdgeCase where Less the sum need not touch each other, Therefore Couldnt pass last 3 TC
    
    # ---------------------------------------------------------------------------------------------- #
    # FINAL Method:
    # Circle Clamping: Find the Point on Rectangle which is Nearest to the circle, check if dist >= radius. 
        nearestX = max(x1, min(xCenter, x2))
        nearestY = max(y1, min(yCenter, y2))

        dist = sqrt((nearestX-xCenter)**2 + (nearestY - yCenter)**2)

        return dist <= radius