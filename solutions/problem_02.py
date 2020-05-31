def new_arr(arr):
    product_arr = []
    product = 1
    
    # Create product of all values in arr
    for num in arr:
        product *= num
    
    # Divide by each num separately to create new arr
    for num in arr:
        product_arr.append(product / num)
    
    return product_arr

assert new_arr([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert new_arr([3, 2, 1]) == [2, 3, 6]
assert new_arr([]) == []
assert new_arr([1]) == [1]
#assert new_arr([3, 0, 5]) == [0, 15, 0] # Doesn't work against 0 (division by zero err)

def new_arr_no_div(arr):
    if len(arr) <= 1:
        return arr
        
    prod_from_left = []
    product = 1
    for num in arr:
        product *= num
        prod_from_left.append(product)

    prod_from_right =[]
    product = 1
    for num in arr[::-1]:
        product *= num
        prod_from_right.insert(0, product)

    product_arr = []
    for i in range(len(arr)):
        if i == 0:
            product_arr.append(prod_from_right[i + 1])
        elif i == len(arr) - 1:
            product_arr.append(prod_from_left[i - 1])
        else:
            product_arr.append(prod_from_right[i + 1] * prod_from_left[i - 1])
    
    return product_arr

assert new_arr_no_div([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert new_arr_no_div([3, 2, 1]) == [2, 3, 6] 
assert new_arr_no_div([]) == []
assert new_arr_no_div([1]) == [1]
assert new_arr_no_div([3, 0, 5]) == [0, 15, 0]