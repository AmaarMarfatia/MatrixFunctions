def add(matA,matB):
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
    #is it possible to add them
    if dimA != dimB:
        raise Exception("dimension mismath {} != {}".format(dimA,dimB))
    #add em together
    newArr = [[0 for _ in range(dimA[1])] for _ in range(dimA[0])]
    for i in range(dimA[0]):
        for j in range(dimA[1]):
            newArr[i][j] = matA[i][j] + matB[i][j]
    return newArr