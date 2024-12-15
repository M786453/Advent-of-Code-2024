"""
Day#: 15
Problem Title: Warehouse Woes
Author: Muhammad Ahtesham Sarwar
"""
from copy import deepcopy

warehouse_map, robot_movements = open('example-input-day-15.txt', 'r').read().split('\n\n')

robot_movements = robot_movements.replace('\n','') # Remove newlines

warehouse_map = [list(row) for row in warehouse_map.split('\n')]

original_warehouse_map = deepcopy(warehouse_map)

warehouse_max_rows = len(warehouse_map)

warehouse_max_cols = len(warehouse_map[0])

robot_cords = (0,0,)

movements_dict = {
    '^': (-1,0), # UP
    'v': (1,0),  # DOWN
    '<': (0,-1), # LEFT
    '>': (0,1)   # RIGHT
}

def get_robot_cords():

    for i in range(warehouse_max_rows):

        for j in range(warehouse_max_cols):

            if warehouse_map[i][j] == '@':
                return (i,j,)

def find_boxes(robot_cords, movement):

    boxes = []

    while True:

        new_cords = (robot_cords[0] + movement[0], robot_cords[1] + movement[1],)

        if new_cords[0] >=0 and new_cords[0] < warehouse_max_rows and new_cords[1] >= 0 and new_cords[1] < warehouse_max_cols:

            object = warehouse_map[new_cords[0]][new_cords[1]]

            if object == 'O': # Box
                boxes.append(new_cords)
            else:
                return boxes
            
            robot_cords = new_cords

def show_map(map_):

    print()

    print()

    for row in map_:
        print(''.join(row))

def get_boxes_gps_cords():

    boxes_gps_cords = []

    for i in range(warehouse_max_rows):

        for j in range(warehouse_max_cols):

            if warehouse_map[i][j] == 'O':

                boxes_gps_cords.append((100*(i)) + j)

    return boxes_gps_cords

def move_robot():

    # Find robot coordinates
    robot_cords = get_robot_cords()

    # Robot movements
    for movement in robot_movements:

        new_cords = ((robot_cords[0] + movements_dict[movement][0]),(robot_cords[1] + movements_dict[movement][1]),)

        new_object = warehouse_map[new_cords[0]][new_cords[1]]

        if new_object == '.':

            warehouse_map[robot_cords[0]][robot_cords[1]] = '.'

            warehouse_map[new_cords[0]][new_cords[1]] = '@'

            robot_cords = new_cords

        elif new_object == 'O':

            boxes = find_boxes(robot_cords, movements_dict[movement])

            last_box = boxes[-1]

            if warehouse_map[last_box[0] + movements_dict[movement][0]][last_box[1] + movements_dict[movement][1]] == '.':

                warehouse_map[last_box[0] + movements_dict[movement][0]][last_box[1] + movements_dict[movement][1]] = 'O'

                warehouse_map[robot_cords[0]][robot_cords[1]] = '.'

                warehouse_map[boxes[0][0]][boxes[0][1]] = '@'

                robot_cords = boxes[0]

def solve_puzzle_1():

    # Implement robot movements
    move_robot()

    print('Answer Puzzle#1:',sum(get_boxes_gps_cords()))

if __name__ == "__main__":

    solve_puzzle_1()