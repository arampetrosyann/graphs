def matrix_to_list(adj_mat):
    result = []
    
    for i in range(0, len(adj_mat)):
        result.append([])
        for j in range(0, len(adj_mat[i])):
            if adj_mat[i][j]:
                result[i].append(j)
        
    return result
