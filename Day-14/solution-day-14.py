from math import prod

max_rows = 103
max_cols = 101
mid_row = max_rows//2
mid_col = max_cols//2
quads = [0,0,0,0] # quadrants

def get_robots():

    robots_data_list = []

    robots = open('input-day-14.txt', 'r').read().split('\n')

    for r in robots:

        r_data_parts = r.split(' ')

        r_data = []

        for part in r_data_parts:

            r_data.append([int(val) for val in part.split('=')[-1].split(',')])
        
        robots_data_list.append(r_data)

    return robots_data_list

robots_data = get_robots()

# Puzzle 1

"""
Find the numbers of robots present in each quadrant after 100 seconds of movement from given position using given velocity.
Return the product of numbers of robots present in each quadrant.
Note:
- Robots present on center (vertical/horizontal) should be not be consider in count.
- Robots can teleport (according to their position in map) if they cross the boundries.
"""

for r in robots_data:

    pos, vel = r

    new_pos_col = (pos[0] + (vel[0]*100)) % max_cols

    new_pos_row = (pos[1] + (vel[1]*100)) % max_rows

    if new_pos_col < mid_col and new_pos_row < mid_row:

        quads[0] += 1 # First Quad
    
    elif new_pos_col > mid_col and new_pos_row < mid_row:

        quads[1] += 1 # Second Quad
    
    elif new_pos_col < mid_col and new_pos_row > mid_row:

        quads[2] += 1 # third quad

    elif new_pos_col > mid_col and new_pos_row > mid_row:

        quads[3] += 1 # fourth quad

print('Answer Puzzle#1:', prod(quads))

# Puzzle 2

"""
No robot will overlap when they form christmas tree
"""

time_ = 0 # Seconds

while True:

    time_ += 1

    robots_positions = set()

    is_overlapping = False

    for r in robots_data:

        x,y = r[0]

        vx,vy = r[1]

        new_x = (x + (vx*time_)) % max_cols

        new_y = (y + (vy*time_)) % max_rows

        if (new_x,new_y,) in robots_positions: # Robots overlap

            is_overlapping = True

            break

        robots_positions.add((new_x,new_y,))

    if not is_overlapping:

        print("Answer Puzzle#2:", time_)

        break