class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s=[]
        for i in range(len(asteroids)):
            while s and asteroids[i]<0 and s[-1]>0 and  abs(asteroids[i])>s[-1]:
                s.pop()
            if s and asteroids[i]<0 and abs(asteroids[i])==s[-1]:
                s.pop()
                continue
            if s and asteroids[i]<0 and s[-1]>0:
                continue
            s.append(asteroids[i])
        return s
            
        