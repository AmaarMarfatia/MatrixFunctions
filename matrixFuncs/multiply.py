def multiply(matA, matB):
    dimA = []
    dimB = []
    # find dimensions of arrA
    a = matA
    b = matB
    while type(a) == list:
        dimA.append(len(a))
        a = a[0]
    # find dimensions of arrB
    while type(b) == list:
        dimB.append(len(b))
        b = b[0]    
    # is it possible to multiply the matrices
    if dimA[1] != dimB[0]:
        raise Exception("Dimension mismatch {} != {}".format(dimA[1], dimB[0]))
    # aight time to multiply em
    newArr = [[0 for _ in range(dimB[1])] for _ in range(dimA[0])]
    for i in range(dimA[0]):
        for j in range(dimB[1]):
            # find the dot product
            sum = 0
            for n in range(dimA[1]):
                sum += matA[i][n] * matB[n][j]
            newArr[i][j] = sum
    return newArr