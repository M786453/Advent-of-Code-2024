from itertools import combinations

networks = open('example-input-day-23.txt','r').read().split('\n')

computers_connections = {}

def add_computer_conn(c1, c2):

    if c1 in computers_connections:

        computers_connections[c1].append(c2)
    
    else:

        computers_connections[c1] = [c2]

for net in networks:

    c1, c2 = net.split('-')

    add_computer_conn(c1, c2)
    add_computer_conn(c2, c1)

# Interconnected computers set
three_ics_pair = set()
for c in computers_connections:

    interconnected_computers = [c] # Computers which are connected with each other

    connected_computers = computers_connections[c] # computers connected to current computer

    for cc in connected_computers:

        if all([ic in computers_connections[cc] for ic in interconnected_computers]):
            interconnected_computers.append(cc)

    interconnected_computers.sort()

    if len(interconnected_computers) > 3:
        for comb in combinations(interconnected_computers, 3):
            three_ics_pair.add(tuple(comb))
    elif len(interconnected_computers) == 3:
        three_ics_pair.add(tuple(interconnected_computers))

# print(computers_connections)
for ics in three_ics_pair:
    ics = list(ics)
    print(",".join(ics))


