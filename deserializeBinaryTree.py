class Codec:

    def serialize(self, root):
        if not root:
            return ""

        result = []

        def dfs(node):
            if not node:
                result.append("N")
                return

            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(result)

    def deserialize(self, data):
        if not data:
            return None

        values = data.split(",")
        index = [0]

        def dfs():
            if values[index[0]] == "N":
                index[0] += 1
                return None

            node = TreeNode(int(values[index[0]]))
            index[0] += 1

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()