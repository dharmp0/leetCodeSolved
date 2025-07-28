from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        R = deque()
        D = deque()
        
        for idx in range(len(senate)):
           
            if senate[idx] == 'R':
                R.append(idx)
            else:
                D.append(idx)
        
        while D and R:

            D_idx = D.popleft()
            R_idx = R.popleft()
            
            if D_idx < R_idx:
                D.append(D_idx + len(senate))
            else:
                R.append(R_idx+len(senate))

        if D:
            return "Dire"
        else:
            return "Radiant"
