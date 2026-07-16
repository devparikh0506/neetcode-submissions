class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            node = root

            for character in word:
                if character not in node.children:
                    node.children[character] = TrieNode()

                node = node.children[character]

            node.word = word

        rows = len(board)
        cols = len(board[0])
        result = []

        def dfs(row, col, parent):
            character = board[row][col]

            if character not in parent.children:
                return

            node = parent.children[character]

    
            if node.word is not None:
                result.append(node.word)

                node.word = None

            board[row][col] = "#"

            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and board[new_row][new_col] != "#"
                ):
                    dfs(new_row, new_col, node)

            board[row][col] = character

           
            if not node.children and node.word is None:
                del parent.children[character]

        for row in range(rows):
            for col in range(cols):
                if board[row][col] in root.children:
                    dfs(row, col, root)

        return result