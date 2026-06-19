from collections import deque
class Solution(object):
    def validPath(self, n, edges, source, destination):
        if n==1:
            return True
        nums=deque(edges)
        grid=[[] for _ in range(n)]
        while nums:
            u,v=nums.popleft()
            grid[u].append(v)
            grid[v].append(u)
        q=deque()
        q.append(source)
        visited=[False]*n
        visited[source]=True
        while q:
            x=q.popleft()
            for node in grid[x]:
                if node==destination:
                    return True
                if not visited[node]:
                    visited[node]=True
                    q.append(node)
        return False


        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        