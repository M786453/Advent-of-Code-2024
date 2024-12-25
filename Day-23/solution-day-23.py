networks = open('input-day-23.txt','r').read().split('\n')

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

# Pairs of Three Interconnected computers set
three_ics_pair = set()

for c in computers_connections:

    connected_computers = computers_connections[c] # computers connected to current computer

    for i in range(len(connected_computers)):

        for j in range(len(connected_computers)):

            c1 = connected_computers[i]
            c2 = connected_computers[j]

            if c1 != c2:
                
                if c1 in computers_connections[c2]:
                    ics = [c, c1, c2] # Interconnected computers
                    if any([c.startswith('t')for c in ics]):
                        ics.sort()
                        three_ics_pair.add(tuple(ics))

print(len(three_ics_pair))
# for ics in three_ics_pair:
#     ics = list(ics)
#     print(",".join(ics))


