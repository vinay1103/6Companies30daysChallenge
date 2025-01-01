# 1823. Find the Winner of the Circular Game

class Solution:
    # Logic: Simulate the game using List
    def findTheWinner(self, n: int, k: int) -> int:
        playerList = [i for i in range(1,n+1)]
        ind = 0

        while len(playerList) > 1:
            ind = (ind + k - 1) % len(playerList)
            playerList.pop(ind)
        
        return playerList[0]