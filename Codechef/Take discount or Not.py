class Solution:
    def check_coupon(self, n, x, y, prices):
        # write your code here
        
        toatl = sum(prices)
        total_coup = 0
        
        for i in range(n):
            if prices[i] < y:
                continue
            else :
                total_coup += prices[i]-y
                
        after_dis = total_coup + x
        
        if toatl > after_dis:
            return "COUPON"
        else:
            return "NO COUPON"