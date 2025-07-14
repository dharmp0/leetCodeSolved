class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for i in asteroids:
            
            if i > 0:                               
                
                stack.append(i)
            
            else:

                while stack and i < 0 < stack[-1]:
                    
                    if abs(i) > stack[-1]:
                        stack.pop()
                    
                    elif abs(i) == stack[-1]:
                        stack.pop()
                        break
                    
                    else:
                        break
                
                else:
                    stack.append(i)

        return stack
