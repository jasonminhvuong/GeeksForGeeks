"""
    Given a 2D board and a word, find if the word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cell,
    where "adjacent" cells are those horizontally or vertically neighboring.
    The same letter cell may not be used more than once.
"""

from collections import Counter

class Solution:
    def find_word(self, board, word, row, col, visited, bc):
        if word == "":
            return True
        
        visited[row][col] = True
        
        target = word[0]
        last_row = len(board) - 1
        last_col = len(board[0]) - 1
        
        if row != 0 and board[row-1][col] == target and not visited[row-1][col]:
            if self.find_word(board, word[1:], row-1, col, visited, bc):
                return True
            else:
                visited[row-1][col] = False
        
        if col != last_col and board[row][col+1] == target and \
        not visited[row][col+1]:
            if self.find_word(board, word[1:], row, col+1, visited, bc):
                return True
            else:
                visited[row][col+1] = False
        
        if row != last_row and board[row+1][col] == target \
        and not visited[row+1][col]:
            if self.find_word(board, word[1:], row+1, col, visited, bc):
                return True
            else:
                visited[row+1][col] = False
                
        if col != 0 and board[row][col-1] == target and \
        not visited[row][col-1]:
            if self.find_word(board, word[1:], row, col-1, visited, bc):
                return True
            else:
                visited[row][col-1] = False
            
        return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        if word == "":
            return True
        
        if not board:
            return False
        
        bc = Counter([c for row in board for c in row])
        wc = Counter(word)
        
        for c in word:
            if bc[c] < wc[c]:
                return False
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if word[0] == board[row][col]:
                    
                    visited = [[False for elem in row] for row in board]
                    
                    if self.find_word(board, word[1:], row, col, visited, bc):
                        return True
        
        return False