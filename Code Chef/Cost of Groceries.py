class Solution:
    def compute(self, n, x, a, b):
        # write your code here 
        
        cost = 0
        
        if n == 1 and a[0] >= x :
            return b[0]
        elif n == 1 and a[0] < x:
            return 0
        
        else :
            for i in range(n):
                if a[i] >= x:
                    cost += b[i]
                
        return cost
            