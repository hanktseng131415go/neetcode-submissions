class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        if sum(matchsticks) % 4:
            return False
        
        sides = [0] * 4
        lenght = sum(matchsticks) / 4
        matchsticks.sort(reverse=True)
        sides = [0] * 4

        def dfs(i):

            if i >= len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3]
            
            for s in range(4):
                if sides[s] + matchsticks[i] <= lenght:
                    sides[s] += matchsticks[i]
                    if dfs(i+1):
                        return True
                    sides[s] -= matchsticks[i]
            
            return False
        
        return dfs(0)