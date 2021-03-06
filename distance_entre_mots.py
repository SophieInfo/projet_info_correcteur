import numpy as np


def CalculDistanceMots(a, b):
    d = np.zeros((len(a)+1,len(b)+1))
    d[:,0] = np.arange(0,len(a)+1)
    d[0] = np.arange(0, len(b)+1)
    print(d)

    cout = 0
    for i in range(1,len(a)+1):
        print(i)
        for j in range(1,len(b)+1):
            if a[i-1] == b[j-1]:
                cout = 0
            else:
                cout = 1

            d[i][j] = min(d[i-1][j]+1, d[i][j-1]+1, d[i-1][j-1]+cout)

            if i > 1 and j > 1 and a[i-1] == b[j-2] and a[i-2] == b[j-1]:
                d[i][j] = min(d[i][j], d[i-2][j-2]+1)

    print(d)
    return d[len(a)][len(b)]

if __name__ == "__main__":
    print(CalculDistanceMots("camoinne", "camionne"))