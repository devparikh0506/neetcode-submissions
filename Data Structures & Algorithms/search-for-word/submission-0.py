class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def backtrack(row, col, index):
            # Every character was matched
            if index == len(word):
                return True

            # Invalid position or character mismatch
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or board[row][col] != word[index]
            ):
                return False

            # Mark current cell as visited
            original = board[row][col]
            board[row][col] = "#"

            # Explore four neighboring cells
            found = (
                backtrack(row + 1, col, index + 1)
                or backtrack(row - 1, col, index + 1)
                or backtrack(row, col + 1, index + 1)
                or backtrack(row, col - 1, index + 1)
            )

            # Undo: restore the cell
            board[row][col] = original

            return found

        # Try every cell as the starting position
        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, 0):
                    return True

        return False
            