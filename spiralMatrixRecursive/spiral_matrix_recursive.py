def snail(snail_map: list) -> list:
    if snail_map == [[]]: return []
    if len(snail_map) == 1: return snail_map.pop()
    array = []
    return snail_recursive(snail_map, array)
    
    
def snail_recursive(snail_map: list, array: list) -> list: 
    if len(snail_map) == 1:
        array.extend(snail_map.pop())
        return array
    elif len(snail_map) == 2:
        array.extend(snail_map.pop(0))
        snail_map[0].reverse()
        array.extend(snail_map.pop())
        return array
    else:
        array.extend(snail_map.pop(0)) #strip outer layer starting with whole top row
        n = len(snail_map)
        for val in range(len(snail_map)): # len gives the number of rows after first one has been popped. Pop last element of each row
            array.append(snail_map[val].pop(n))
        snail_map[n-1].reverse() # reverse last row and pop
        array.extend(snail_map.pop(n-1)) 
        n = len(snail_map)
        for v in range(n-1, -1, -1): # take 1st element of each list in reverse order to do left hand side
            array.append(snail_map[v].pop(0))
        return snail_recursive(snail_map, array) #recursive call on new 2d array
        


    

array1 = [2]
arrayTest = [[5]]
array2 = [[9,1],
         [2,7]]

array3 = [[1,2,3],
         [4,5,6],
         [7,8,9]]

array4 = [[1,2,4,5],
         [3,100,7,8],
         [7,8,9,12],
         [12,15,103,2]]

array5 = [[1,2,4,5,12],
         [3,100,7,8,290],
         [7,8,9,12,1],
         [12,15,103,2,56],
         [56,79,2,8,82]]

print(snail(arrayTest))
print(snail(array3))
print(snail(array1))
print(snail(array2))
print(snail(array4))
print(snail(array5))





# tests
"""
array3 = [[1,2,3],
         [4,5,6],
         [7,8,9]]
expected3 = [1,2,3,6,9,8,7,4,5]

print('True' if expected3 == snail(array3) else 'False')
print (snail(array3))

array4 = [[1,2,4,5],
         [3,100,7,8],
         [7,8,9,12],
         [12,15,103,2]]
expected4 = [1,2,4,5,8,12,2,103,15,12,7,3,100,7,9,8]

print('True' if expected4 == snail(array4) else 'False')
print (snail(array4))
"""

