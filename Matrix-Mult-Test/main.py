import numpy as np
import math

aThree = np.array([
                      [[1,2,3], [4,5,6], [7,8,9]]
                    , [[10,11,12], [13,14,15], [16,17,18]]
                    , [[19,20,21], [22,23,24], [25,26,27]]
                    , [[19,20,21], [22,23,24], [25,26,27]]
                 ])

bThree = np.array([
                      [[100,101,102,103], [104,105,106,0], [106,107,108,0],  [106,107,108,0]]
                    , [[110,111,112,0], [113,114,115,0], [116,117, 118,0],  [106,107,108,0]]
                    , [[119,120,121,0], [122,123,124,0], [125,124,125,0],  [106,107,108,0]]
                    # , [[126,127,128,0], [129,130,131,0], [132,133,134,0]]
                ])    

'''
isPerfSquare:
    -   Take in a 3D array
    -   Compares the length of the rows vs columns
    -   returns a boolean 
'''                       
def isPerfSquare(arr):
    row = len(arr) #rows
    col = len(arr[0]) #columns
    print("Number of rows: ", row,'\n')
    print("Number of columns: ", col,'\n')
    rxc = row - col
    if(rxc != 0):
        return(False)
    return (True)

'''
makePerfSquare : 
    -   Takes in a 3D array
    -   will make the array a perfect square by taking 
        either the row or column and making that the length
        of both sides. 
    -   return a new perfect square array. Padded with zeros to make 
        the perfect square matric possible
'''
def makePerfSquare(arr):
    row = len(arr) #rows
    col = len(arr[0]) #columns
    if(row >  col):
        newarr = np.zeros((row, row, 3), dtype = int)
        for i in range(0, col):
            for j in range(0,col):
                for k in range(0,3):
                    newarr[i][j][k] = arr[i][j][k] 
        return newarr
    else:
        newarr = np.zeros((col, col, 3), dtype = int)        
        for i in range(0, row):
            for j in range(0,col):
                for k in range(0,3):
                    newarr[i][j][k] = arr[i][j][k] 
        return newarr

'''
matrix_mult:
    -   Receives an array
    -   Creates a cypher array which will be used for matrix multiplication
    -   Saves cypher array into its own list which will later be used for inversion (decryption)
    -   applies matrix multiplication to image array and cypher array.
    -   returns new encrypted image array 
'''
cypher_list = []
def matrix_mult(arr):
    cypher = np.random.random(arr.shape) # Cypher matrix of arr shape
    cypher_list.append(cypher) # Appends cypher to cypher list for matrix inversion
    result = np.zeros(arr.shape) # Cypher matrix of arr shape

    a2 = arr.reshape(-1, arr.shape[1])
    c2 = cypher.reshape(-1, cypher.shape[1])
    
    # Matrix multiplication
    res = np.dot(a2, c2.T)

    # Reshape 2D -> 3D 
    res3d = res.reshape(3,-1, 3)
    return res3d

'''
Function Calls
'''
isSquare = isPerfSquare(aThree)  

if(isSquare):
    print('Its a square.')
else:
    print(aThree)
    print('')
    print('Converting to perfect square..')    
    print('')    
    sqrArray = makePerfSquare(aThree)
    print(sqrArray)       
    print('')
    print('Multiplying the Matrices')
    print('')        
    print(matrix_mult(aThree))      































aOneD = aThree.flatten()
# isPerfSquare = math.sqrt(len(aOneD)) - math.floor(math.sqrt(len(aOneD)))
isPerfSquare = len(aOneD) % 1
# print(isPerfSquare)


if(isPerfSquare != 0):
    newArrSize = int(math.pow(2, (math.floor(math.sqrt(len(aOneD))) + 1)))
    newCol = int(math.sqrt(newArrSize))
    newRow = int(math.sqrt(newArrSize))
    newArr = np.zeros((newCol, newRow), dtype = int)

    # for i in range(0, newCol):
    #     for j in range(0, newRow):
    #         for k in range(0, len(aOneD)):    
                # newArr[i][j] = aOneD[k]
    # print(newArr)
    #         for i in range(0,3):
    #             newArr.append(aThree[i][j][k])
    # print(newArr)

# Conver given 3D arrays into 2D arrays
aTwo = aThree.transpose(2,0,1).reshape(-1,aThree.shape[1])
bTwo = bThree.transpose(2,0,1).reshape(-1,bThree.shape[1])

# Lengths of rows and colums for the given arrays
aCol = len(aTwo[0])
bCol = len(bTwo[0])
aRow = len(aTwo)
bRow = len(bTwo)

# Create empty array of size aRow and bCol
result = np.zeros((aRow, bCol), dtype = int)
# print(aTwo)
# print(bTwo)
# print("aCol: ", aCol)
# print("bRow: ", bRow)

# Matrix multiplicaiton
if aCol == bRow:
    for i in range(0, aRow):
        for j in range(0, bCol):
            for k in range(0, aCol):
                result[i][j] += aTwo[i][k] * bTwo[k][j] 
    result_3d = result.reshape(np.roll(aThree.shape,1)).transpose(1,2,0)
    print(result_3d)

else:
    print("")

# Reshape our 2D matrix multiplication result into 3D array
