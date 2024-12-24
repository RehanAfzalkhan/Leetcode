class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        count=0
        for i in range(1,len(colors)): 
            if colors[i]==colors[i-1]:
                if neededTime[i]<neededTime[i-1] :
                    count+=neededTime[i]
                    neededTime[i]=neededTime[i-1]
                else:
                    count+=neededTime[i-1]
        return count