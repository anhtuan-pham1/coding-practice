# https://binarysearch.com/problems/Unidirectional-Word-Search

def solve(board, word):
    for i in board:
            sentence = "".join(i)
            if word in sentence:
                return True

    for i in range (0,len(board[0])):
        sentence = ""
        for j in range (0,len(board)):
            sentence += board[j][i]
        if word in sentence:
            return True
    return False

# Another possible by looping every character in the board (khoa súc vật)

    #def solve(self, board, word):
        # word_len = len(word) - 1
        # col = len(board[0])
        # row = len(board)
        # for i in range (0, len(board)):
        #     for j in range (0, len(board[i])):
        #         if j < col - word_len:
        #             k = 0
        #             while board[i][j+k] == word[k]:
        #                 k +=1
        #                 if k == len(word):
        #                     return True
        #         if i < row - word_len:
        #             k = 0
        #             while board[i+k][j] == word[k]:
        #                 k +=1
        #                 if k == len(word):
        #                     return True    
        # return False