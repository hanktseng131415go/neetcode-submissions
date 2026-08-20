class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        out = []
        for a in asteroids:
            while out and out[-1]>0 and a<0:
                collision = out[-1] + a
                if collision > 0:
                    a = 0
                elif collision == 0:
                    a = 0
                    out.pop()
                else:
                    out.pop()
            
            if a:
                out.append(a)
        
        return out