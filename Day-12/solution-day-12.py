plants_map = open('input-day-12.txt','r').read().split('\n')
adj_checks = [(-1,0),# UP
              (1,0), # DOWN
              (0,1), # RIGHT
              (0,-1) # LEFT
              ]
visited_cords = set()

def find_region(plot_cords, perimeter, area):

    # print(f"{plants_map[plot_cords[0]][plot_cords[1]]}:", area, perimeter)

    visited_cords.add(plot_cords)

    for adj in adj_checks:

        adj_cords = (plot_cords[0]+adj[0], plot_cords[1]+adj[1],)
        
        if adj_cords[0] >= 0 and adj_cords[0] < len(plants_map) and adj_cords[1] >= 0 and adj_cords[1] < len(plants_map):
            if plants_map[plot_cords[0]][plot_cords[1]] == plants_map[adj_cords[0]][adj_cords[1]]:
                perimeter -= 1
                if adj_cords not in visited_cords:
                    area, perimeter = find_region(adj_cords, perimeter+4, area+1)

    return area, perimeter

# visit plants map
fence_cost = 0

for i in range(len(plants_map)):

    for j in range(len(plants_map)):

        cords = (i,j,)

        if cords not in visited_cords:

            area, perimeter = find_region(cords, 4, 1)

            # print(f"{plants_map[i][j]}:", area, perimeter)

            fence_cost += area * perimeter

            # break
    
    # break

print("Answer:", fence_cost)