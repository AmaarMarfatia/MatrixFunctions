def determinant(matA):
    dimA = []
    # find dimensions of arrA
    a = matA
    while type(a) == list:
        dimA.append(len(a))
        a = a[0]
    #is it square
    if dimA[0] != dimA[1]:
        raise Exception("Matrix is not square")
    #find determinant
    total = 0
    if dimA[0] == 2:
        total = matA[0][0] * matA[1][1] - matA[1][0] * matA[0][1]
        return total
    else:
        sign = 1
        for i in range(dimA[0]):
            temp = matA[1:]
            #remove the current column from the temp stuff
            for j in range(dimA[0]-1):
                temp[j] = temp[j][0:i] + temp[j][i+1:]
            sub = determinant(temp)
            total = total + sign * matA[0][i] * sub
            sign *= -1
    return total

matA = [[1,2,3],[4,5,6],[7,8,15]]   
print(determinant(matA))