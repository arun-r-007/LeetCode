class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1

        else :
            tank = index = 0
            n = len(gas)

            for i in range(n):
                tank += gas[i] - cost[i]
                if tank < 0:
                    tank, index = 0, i+1
            
            return index