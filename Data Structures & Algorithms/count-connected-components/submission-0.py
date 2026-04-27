class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit  = [False] * n
        adj = [[] for i in range(n)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        # def bfs(node):
        #     q = deque([node])
        #     visit[node] = True
        #     while q:
        #         cur = q.popleft()
        #         for nei in adj[cur]:
        #             if not visit[nei]:
        #                 visit[nei] = True
        #                 q.append(nei)
        # result = 0
        # for i in range(n):
        #     if not visit[i]:
        #         bfs(i)
        #         result += 1
        # return result

        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        res = 0
        for i in range(n):
            if not visit[i]:
                visit[i] = True
                res += 1
                dfs(i) 
        return res
#TC = N+E
#SC = N+E
        
        