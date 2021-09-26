X = [10, 40, 30, 50, 20]  
W = [1, 2, 3, 4, 5]

def weightedMean(X, W):
    mul = []
    eg = []
    for index, number in enumerate(X):
        mul.append(X[index]*W[index])

    avg = sum(mul)/sum(W)
    print("{:.1f}".format(avg))

weightedMean(X, W)