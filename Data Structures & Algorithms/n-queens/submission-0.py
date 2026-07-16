class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = [["."] * n for _ in range(n)]
        result = []

        columns = set()
        positive_diagonals = set()  # row + col
        negative_diagonals = set()  # row - col

        def backtrack(row):

            if row == n:
                result.append(["".join(r) for r in board])
                return

            # Try placing the queen in every column
            for col in range(n):
                if (
                    col in columns
                    or row + col in positive_diagonals
                    or row - col in negative_diagonals
                ):
                    continue

                # Choose
                board[row][col] = "Q"
                columns.add(col)
                positive_diagonals.add(row + col)
                negative_diagonals.add(row - col)

                # Explore the next row
                backtrack(row + 1)

                # Undo
                board[row][col] = "."
                columns.remove(col)
                positive_diagonals.remove(row + col)
                negative_diagonals.remove(row - col)

        backtrack(0)
        return result
                
            
