def queensAttack(n, k, r_q, c_q, obstacles):
    n = n - 1
    r_q = r_q - 1
    c_q = c_q - 1


    # print(obstacles,[r_q,c_q])

    if (k == 0):
        return (2* n)+ min(r_q,c_q) + min(r_q,n - c_q) + min(n - r_q, c_q) + min(n - r_q, n - c_q)


    rowOb = []
    colOb = []
    crosOb1 = []
    crosOb2 = []

    for i in obstacles:
        i[0] = i[0] - 1
        i[1] = i[1] - 1
        if(i[0] == r_q):
            colOb.append(i)

        if(i[1] == c_q):
            rowOb.append(i)

        if(abs(i[0] - r_q) == abs(i[1] - c_q)):
            if(i[0] > r_q and i[1] > c_q) or (i[0] < r_q and i[1] < c_q) : 
                crosOb1.append(i)
            else:
                crosOb2.append(i)

    rowMin = 0
    rowMax = n+1
    rowPos = 0
    for i in rowOb:
        if(i[0] < r_q and i[0] > rowMin):
            rowMin = i[0]+1
        elif(i[0] > r_q and i[0] < rowMax):
            rowMax = i[0]
    rowPos = rowMax - rowMin -1 

    colMin = 0
    colMax = n+1
    colPos = 0
    for i in colOb:
        if(i[1] < c_q and i[1] > colMin):
            colMin = i[1]+1
        elif(i[1] > c_q and i[1] < colMax):
            colMax = i[1]
    colPos = colMax - colMin -1 

    crosMin1 = min(r_q,c_q)
    crosMax1 = min(n - r_q, n - c_q)
    crosPos1 = 0

    for i in crosOb1:
        if(i[0] > r_q):
            print(crosMax1,min(i[0] - r_q,i[1] - c_q))
            if(crosMax1 >= min(i[0] - r_q,i[1] - c_q)):
                crosMax1 = min(i[0] - r_q,i[1] - c_q)-1
        else:
            if(crosMin1 >= min(r_q - i[0],c_q - i[1])):
                crosMin1 = min(r_q - i[0],c_q - i[1])-1


    crosPos1 =  crosMin1 + crosMax1
    

    crosMin2 = min(r_q,n-c_q)
    crosMax2 = min(n - r_q,c_q)
    crosPos2 = 0

    for i in crosOb2:
        if(i[0] > r_q):
            if(crosMax2 >= min(i[0] - r_q, c_q - i[1])):
                crosMax2 = min(i[0] - r_q, c_q - i[1])-1
        else:
            if(crosMin2 >= min(r_q - i[0],i[1] - c_q)):
                crosMin2 = min(r_q - i[0],i[1] - c_q)-1


    crosPos2 = crosMin2 + crosMax2

    return rowPos + colPos + crosPos1 + crosPos2

if __name__ == '__main__':
    # 4 0 4 4 [] #9
    # 5 3 4 3 [[5, 5], [4, 2], [2, 3]] #10
    # 1 0 1 1 [] #0
    n = 5
    k = 3
    r_q = 4
    c_q = 3
    obstacles = [[5, 5], [4, 2], [2, 3]]
    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)

   
