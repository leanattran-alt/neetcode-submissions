from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}

        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node["#"] = word

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            char = board[r][c]

            if char not in node:
                return

            child = node[char]
            word = child.pop("#", None)

            if word:
                result.append(word)

            board[r][c] = "#"

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c +dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if board[nr][nc] in child:
                        dfs(nr, nc, child)

            board[r][c] = char

            if not child:
                del node[char]

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie:
                    dfs(r, c, trie)

        return result