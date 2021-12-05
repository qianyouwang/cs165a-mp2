import math
# expectmax algorithm is implemented

def value(Grid,limit):
    if limit == 0:
        return evaluate(Grid)
    else:
        return maxtrick(Grid,limit)

def maxtrick(Grid,limit):
    expect = 0
    for id in range(4):
        expect += value(gridMove(Grid,id),limit-1)
    return expect/4


def evaluate(Grid):
    sum_value = 0
    nonzero_cnt = 0
    for i in Grid:
        for j in i:
            sum_value += j
            if j != 0:
                nonzero_cnt += 1
    if nonzero_cnt != 0:
        return sum_value/nonzero_cnt
    else:
        return 0


def gridMove(Grid,code):
    new_grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    if code == 0:
        for i in range(4):
            assist = []
            for j in range(4):
                if Grid[j][i] != 0:
                    assist.append(Grid[j][i])
            k = 1
            while k < len(assist):
                if assist[k] == assist[k-1]:
                    assist[k-1] += assist[k-1]
                    del assist[k]
                k += 1
            for w in range(len(assist)):
                new_grid[w][i] = assist[w]
    elif code == 1:
        for i in range(4):
            assist = []
            for j in range(3,-1,-1):
                if Grid[j][i] != 0:
                    assist.append(Grid[j][i])
            k = 1
            while k < len(assist):
                if assist[k] == assist[k-1]:
                    assist[k-1] += assist[k-1]
                    del assist[k]
                    k += 1
                k += 1
            for w in range(len(assist)):
                new_grid[-(w+1)][i] = assist[w]
    elif code == 2:
        for i in range(4):
            assist = []
            for j in range(4):
                if Grid[i][j] != 0:
                    assist.append(Grid[i][j])
            k = 1
            while k < len(assist):
                if assist[k] == assist[k-1]:
                    assist[k-1] += assist[k-1]
                    del assist[k]
                k += 1
            for w in range(len(assist)):
                new_grid[i][w] = assist[w]
    elif code == 3:
        for i in range(4):
            assist = []
            for j in range(3,-1,-1):
                if Grid[i][j] != 0:
                    assist.append(Grid[i][j])
            k = 1
            while k < len(assist):
                if assist[k] == assist[k-1]:
                    assist[k-1] += assist[k-1]
                    del assist[k]
                    k += 1
                k += 1
            for w in range(len(assist)):
                new_grid[i][-(w+1)] = assist[w]
    return new_grid


def NextMove(Grid,Step):
    """
    :param Grid:the current state
    :param Step:how many step algorithm would
    :return: 0:up 1:down 2:left 3:right 4:quit other integer:do nothing
    """
    maxc = -math.inf
    MoveCode = -1
    for i in range(4):
        if value(gridMove(Grid,i),10) > maxc:
            maxc = value(gridMove(Grid,i),3)
            MoveCode = i
    return MoveCode

# if __name__ == '__main__':
#     x = NextMove([[2,2,2,0],[2,0,0,0],[0,4,4,4],[2,4,4,0]],1)
#     print(x)
#     print(gridMove([[2,2,2,0],[2,0,0,0],[0,4,4,4],[2,4,4,0]],x))
#     print(gridMove([[2,2,2,0],[2,0,0,0],[0,4,4,4],[2,4,4,0]],1))
