def avaliable(board):
    v = []
    for i in range(len(board)):
        # print(i)
        if i == 0:
            if board[i] == 0 and board[i+1]==0:
                v.append(i)
            continue
        if i ==19:
            if board[i] == 0 and board[i-1]==0:
                v.append(i)
            continue

        
        
        if board[i] == 0 and board[i+1]==0 and board[i-1]==0:
            v.append(i)

        
    return v


def minmax(board,turn,de,st):
    
    if turn ==1:
        score = [-100,st]
        aval_board = avaliable(board)
        if len(aval_board)==0:

            return [-10-de,st]
        for i in aval_board:
            board[i] = 1
            val_minmax=minmax(board,2,de+1,st+f"[{i}1]-")

            score = [max(score[0] ,val_minmax[0]),val_minmax[1]]
            
            board[i] = 0
            
        return score
    if turn ==2:
        score = [100,st]
        aval_board = avaliable(board)
        if len(aval_board)==0:
            return [10+de,st]
        for i in aval_board:
            board[i] = 2
            val_minmax=minmax(board,1,de+1,st+f"[{i}2]-")
            score = [min(score[0] ,val_minmax[0]),val_minmax[1]]
            
            board[i] = 0
            
        return score
        
q=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]
for i in avaliable(q):
    q[i]=1
    s = minmax(q,2,0,"")
    print(i)
    print(s)
    q[i]=0
    
    
