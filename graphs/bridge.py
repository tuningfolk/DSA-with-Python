class Solution:
    def criticalConnections(self,n,connections):
        neighbors = [[] for i in range(n)]
        explored = [-1 for i in range(n)]
        critical = []
        id = [0]
        for v1,v2 in connections:
            neighbors[v1].append(v2)
            neighbors[v2].append(v1)
        
        def dfs(vertex,last):
            if explored[vertex] != -1:
                return explored[vertex]
            explored[vertex] = id[0]
            id[0] += 1
            for neighbor in neighbors[vertex]:
                if neighbor == last: continue
                explored[vertex] = min(explored[vertex],dfs(neighbor,vertex))
            for neighbor in neighbors[vertex]:
                if neighbor == last: continue
                if explored[vertex] <explored[neighbor]:
                    critical.append([vertex,neighbor])
            return explored[vertex]
        dfs(0,None)
        return critical
s = Solution()
print(s.criticalConnections(5,[[1,0],[2,0],[3,0],[4,1],[4,2],[4,0]]))

            
