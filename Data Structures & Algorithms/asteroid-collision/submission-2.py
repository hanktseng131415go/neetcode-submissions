class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # # time: n
        # # space: n
        # out = []
        # for a in asteroids:
        #     while out and out[-1]>0 and a<0:
        #         collision = out[-1] + a
        #         if collision > 0:
        #             a = 0
        #         elif collision == 0:
        #             a = 0
        #             out.pop()
        #         else:
        #             out.pop()
            
        #     if a:
        #         out.append(a)
        
        # return out

        n = len(asteroids)
        m = -1
        for a in asteroids:
            while m >= 0 and asteroids[m] > 0 and a < 0:
                collision = asteroids[m] + a
                if collision > 0:
                    a = 0
                elif collision == 0:
                    m-=1
                    a=0
                else:
                    m-=1
            
            if a:
                m+=1
                asteroids[m] = a
        
        return asteroids[:(m+1)]