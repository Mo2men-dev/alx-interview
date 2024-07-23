def pascal_triangle(n):
    if n <= 0:
        return []
    
    output = [[1], [1, 1]]
    elements_to_add = 1

    for i in range(2, n):
        nxt_arr = [1]
        for j in range(elements_to_add):
            nxt_el = output[elements_to_add][j] + output[elements_to_add][j + 1]
            nxt_arr.append(nxt_el)
        
        elements_to_add += 1
        nxt_arr.append(1)
        output.append(nxt_arr)
    
    return output
