class Solution:
    def findSubtreeSizes(self, parent, s):
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        last_seen = [-1] * 26
        new_parent = list(parent)
        ans = [1 for _ in range(n)]
        
        def dfs(u):
            char_idx = ord(s[u]) - ord('a')
            prev_ancestor = last_seen[char_idx]
            
            if prev_ancestor != -1:
                new_parent[u] = prev_ancestor
                
            last_seen[char_idx] = u
            
            for v in adj[u]:
                dfs(v)
                ans[new_parent[v]] += ans[v]
                
            last_seen[char_idx] = prev_ancestor
            
        dfs(0)
        return ans
