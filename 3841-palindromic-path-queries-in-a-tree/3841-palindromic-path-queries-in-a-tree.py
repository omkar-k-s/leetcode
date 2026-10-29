
class Solution:
    def palindromePath(self, n, edges, s, queries):
        from collections import defaultdict

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        # Euler tour and parent/depth arrays
        stack = [(0, -1, 0)]
        while stack:
            u, p, state = stack.pop()

            if state == 0:
                parent[u] = p
                tin[u] = timer
                timer += 1

                stack.append((u, p, 1))
                for v in reversed(adj[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer

        # Binary lifting for LCA
        LOG = n.bit_length()
        up = [[0] * n for _ in range(LOG)]
        for u in range(n):
            up[0][u] = u if parent[u] == -1 else parent[u]

        for k in range(1, LOG):
            for u in range(n):
                up[k][u] = up[k - 1][up[k - 1][u]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for k in range(LOG):
                if diff & (1 << k):
                    u = up[k][u]

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]

            return parent[u]

        # Fenwick tree for subtree range XOR
        bit = [0] * (n + 2)

        def bit_update(i, val):
            i += 1
            while i <= n:
                bit[i] ^= val
                i += i & -i

        def bit_query(i):
            i += 1
            result = 0
            while i > 0:
                result ^= bit[i]
                i -= i & -i
            return result

        def range_update(l, r, val):
            bit_update(l, val)
            if r < n:
                bit_update(r, val)

        chars = list(s)
        for u in range(n):
            mask = 1 << (ord(chars[u]) - ord('a'))
            range_update(tin[u], tout[u], mask)

        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                old_mask = 1 << (ord(chars[u]) - ord('a'))
                new_mask = 1 << (ord(c) - ord('a'))

                if old_mask != new_mask:
                    range_update(tin[u], tout[u], old_mask ^ new_mask)
                    chars[u] = c

            else:
                u = int(parts[1])
                v = int(parts[2])

                w = lca(u, v)
                mask_u = bit_query(tin[u])
                mask_v = bit_query(tin[v])
                mask_w = 1 << (ord(chars[w]) - ord('a'))

                path_mask = mask_u ^ mask_v ^ mask_w
                ans.append((path_mask & (path_mask - 1)) == 0)

        return ans
