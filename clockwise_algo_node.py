class Node:
   def __init__(self, position: list, next = None, isVisited = False):
       self.row_location = position[0]
       self.col_location = position[1]
       self.next = next
       self.isVisited = isVisited



def snail(snail_map: list) -> list:
    """
    traverses nodes straight always turning right as long as it can not got straight 
    or reaches a previously visited node. Stop if reach the Max Col or Max Row 
    or if node has been visited
    Solution is complete when node can no longer advance. Store node values.

    nxn matrix so Rows & Cols defined by amount of len(snail_map)

    To always turn right you will move through these steps in a series
    Increase Col to move right, increase Row to move down, 
    decrease Col - left, decrease Row to move up

    Check if next node is valid..store if so. 

    

    
    """

    #check for empty list edge case
    if not snail_map:
         return []

    #set max dimensions of matrix based on length of the passed arrays
    MATRIX_ROW_MAX, MATRIX_COL_MAX = len(snail_map) - 1, len(snail_map) - 1

    # change position values depending on direction
    def move_position(direction: int, positions: list) -> list:
        new_positions = []
        if i == 0: # move right..increment col
            new_positions = [positions[0], positions[1] + 1]
        elif i == 1: # move down..increment row
            new_positions = [positions[0] + 1, positions[1]]
        elif i == 2: # move left decrement col
            new_positions = [positions[0], positions[1] - 1]
        elif i == 3: # move up decerement row
            new_positions = [positions[0] - 1, positions[1]]
        return new_positions # returns a new list so passed list is unchanged

    def check_valid_move(positions: list, MATRIX_ROW_MAX: int, MATRIX_COL_MAX: int) -> bool:
     # check if in bounds and return True along with update row and col
        if positions[0] >= 0 and positions[0] <= MATRIX_ROW_MAX:
            if positions[1] >= 0 and positions[1] <= MATRIX_COL_MAX:
                return True
        return False

    # check if there is a node present in position arg
    def check_node_present(visited_nodes: list, position: list) -> bool:
        for node in visited_nodes:
            if node.row_location == position[0] and node.col_location == position[1]:
                return True
        return False 


    visited_nodes = []
    # init first node
    current_positions = [0,0]
    current_node = Node(current_positions, isVisited= True)
    visited_nodes.append(current_node)

    i =0
    #while there are still nodes to visit
    while len(visited_nodes) < len(snail_map)*len(snail_map):
        # reset direction after trying all directions
        if i > 3:
            i = 0
        #update next position for node
        next_positions = move_position(i, current_positions)
        # check if next positions are valid and in bounds
        if check_valid_move(next_positions, MATRIX_ROW_MAX, MATRIX_COL_MAX):
            #check if a node is not present in the next position
            if not (check_node_present(visited_nodes, next_positions)):
                # Create a new node at that position, store it in visited and reset current positions to next
                current_node = Node(next_positions, isVisited= True)
                visited_nodes.append(current_node)
                current_positions = next_positions
            else: #if node present, try a different direction
                i += 1
        else: # if not a valid move, reset next to current and change direction
            next_positions = current_positions
            i += 1


    
    final_array = []
    for node in visited_nodes:
        final_array.append(snail_map[node.row_location][node.col_location])

    return final_array

    

# tests

array3 = [[1,2,3],
         [4,5,6],
         [7,8,9]]
expected3 = [1,2,3,6,9,8,7,4,5]

array4 = [[1,2,4,5],
         [3,100,7,8],
         [7,8,9,12],
         [12,15,103,2]]
expected4 = [1,2,4,5,8,12,2,103,15,12,7,3,100,7,9,8]
print('True' if expected3 == snail(array3) else 'False')
print (snail(array3))
print('True' if expected4 == snail(array4) else 'False')
print (snail(array4))