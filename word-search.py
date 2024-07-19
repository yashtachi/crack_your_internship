class Solution:
    def exist(self, board, word):
        def helper(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            
            temp = board[i][j]
            board[i][j] = ''
            
            if helper(i+1, j, k+1) or helper(i-1, j, k+1) or helper(i, j+1, k+1) or helper(i, j-1, k+1):
                return True
            
            board[i][j] = temp
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(i, j, 0):
                    return True
        return False
            

