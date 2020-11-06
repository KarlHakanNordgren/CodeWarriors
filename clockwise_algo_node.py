class Node:
   def __init__(self, position: list, next = None):
       self.row_location = position[0]
       self.col_location = position[1]
       self.next = next



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

    def check_location_validity(position: list) -> bool:
        if position[0] <= MATRIX_ROW_MAX and position[0] >= 0 and position[1] <= MATRIX_COL_MAX and position[1] >= 0:
            return True
        return False

    def check_node_present(visited_nodes: list, position: list) -> bool:
        for node in visited_nodes:
            if node.row_location == position[0] and node.col_location == position[1]:
                return True
        return False 

    # returns new set of node positions
    def update_directions(current_row: int, current_col: int) -> list:
        return [[current_row, current_col + 1], [current_row + 1, current_col],
            [current_row, current_col - 1], [current_row - 1, current_col]]

    visited_nodes = []
    MATRIX_ROW_MAX, MATRIX_COL_MAX = len(snail_map) - 1, len(snail_map) - 1

    # init first node
    current_row = 0
    current_col = 0
    current_node = Node([current_row, current_col])
    visited_nodes.append(current_node)

    #list of directions, Right - Down - Left - Up
    node_directions = [[current_row, current_col + 1], [current_row + 1, current_col],
            [current_row, current_col - 1], [current_row - 1, current_col]
        ]

    while len(visited_nodes) < len(snail_map)*len(snail_map):
        
        #iterate over directions to check validity
        for direction in node_directions:
            if check_location_validity(direction):
                #check if a node exists and create if it doesn't
                if not check_node_present(visited_nodes, direction):
                    current_node = Node(direction)
                    visited_nodes.append(current_node)
                    node_directions = update_directions(current_node.row_location, current_node.col_location)
                    break
    
    final_array = []
    for node in visited_nodes:
        final_array.append(snail_map[node.row_location][node.col_location])

    return final_array

    

# tests

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
expected = [1,2,3,6,9,8,7,4,5]
print (snail(array))