#transpose
print('\ntranspose')
test_t = [
    [[1, 2, 3]],
    [[1], [2], [3]],
    [[1, 2], [3, 4]],
    [],
    [[1, 2], [3]]
]


def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    len_mat = len(mat[0])
    for i in mat:
        if len(i) != len_mat:
            return 'ValueError'

    len_column = len(mat[0]) 
    result_t = [[] for _ in range(len_column)]
    
    for str in range(len(mat)): 
        for column in range(len_column):  
            result_t[column].append(mat[str][column])  
    
    return result_t

for i in test_t:
    print(transpose(i))


#row_sums
print('\nrow_sums')
test_rs = [
    [[1, 2, 3], [4, 5, 6]],
    [[-1, 1], [10, -10]],
    [[0, 0], [0, 0]],
    [[1, 2], [3]]
]


def row_sums(mat: list[list[float | int]]) -> list[float]:
    res = []
    len_column = len(mat[0])
    for i in mat:
        if len(i) != len_column:
            return 'ValueError'
    for row in mat:
        row_sum = sum(row)
        res.append(row_sum)
    return res
for i in test_rs:
    print(row_sums(i))




#col_sums
print('\ncol_sums')
test_cs = [
    [[1, 2, 3], [4, 5, 6]],
    [[-1, 1], [10, -10]],
    [[0, 0], [0, 0]],
    [[1, 2], [3]]
]

def col_sums(mat: list[list[float | int]]) -> list[float]:
    result_cs = []
    len_str = len(mat[0])
    result_cs = [0] * len_str
    for i in mat:
        if len(i) != len_str:
            return 'ValueError'
        
    for column in mat:
        k = 0
        for strok in column:
            result_cs[k%len_str] = result_cs[k%len_str] + strok
            k+=1
    return result_cs
for i in test_cs:
    print(col_sums(i))

            
        

