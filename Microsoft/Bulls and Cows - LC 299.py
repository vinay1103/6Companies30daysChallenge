# 299. Bulls and Cows

# Method:
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        countA = countB = 0
        
        # 1. Store 2 dictionaries, 1st which stores the number of Places which matched (Bull) and 2nd which stores the frequency counts of Secret String.
        secretCharCount = {}
        matchCount = {}
        
        # 2. To find Bull, we can go with one for-loop. Counting places which match.
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                countA += 1
                # Each time a character matches store it in the HashMap.
                if secret[i] not in matchCount:
                    matchCount[secret[i]] = 1
                else:
                    matchCount[secret[i]] += 1
            
            # Else store the freq Count of Charc in Secret String
            if secret[i] not in secretCharCount:
                secretCharCount[secret[i]] = 1
            else:
                secretCharCount[secret[i]] += 1
        
        # 3. For Cow, we can use these 2 Dictionaries and go in another for loop.
        for i in range(len(guess)):
            
            # If the guess Character is present in SECRET String (checked using secretCharCount Map), 
            if guess[i] in secretCharCount and secretCharCount[guess[i]] != 0:
                
                # and if there was already a matching Place of that character (checked using matchChar HashMap)
                if guess[i] in matchCount and matchCount[guess[i]] != 0:
                    # then just decrement one from the matchChar Map.
                    matchCount[guess[i]] -= 1
                else:
                    # else it means that char is present somewhere else other than the match position, 
                    # So That becomes one Cow Count and we increment by one.
                    countB += 1
                
                # 4.In either case we decrement the secretCharCount by 1.
                # which means one char (which was present in Secret String) has already been checked.
                secretCharCount[guess[i]] -= 1
        
        return "{a}A{b}B".format(a=countA, b= countB)
        # By doing this we can get the answer.
