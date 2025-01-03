# 638. Shopping Offers
from typing import List

# DP Method - Memoisation
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        def directPurchase(needs):
            return sum(needs[i] * price[i] for i in range(len(needs)))

        memo = {}

        # Memoisation Approach
        def dfs(needs):
            needs_tuple = tuple(needs)
            if needs_tuple in memo:
                return memo[needs_tuple]

            if all(need == 0 for need in needs):
                return 0

            # Initial Min Cost is direct purchase without Special Discounts
            min_cost = directPurchase(needs)

            for offer in special:
                new_needs = []
                for i in range(len(needs)):
                    if needs[i] < offer[i]:  
                        break
                    new_needs.append(needs[i] - offer[i])
                else:
                    min_cost = min(min_cost, offer[-1] + dfs(new_needs))

            memo[needs_tuple] = min_cost
            return min_cost

        return dfs(needs)