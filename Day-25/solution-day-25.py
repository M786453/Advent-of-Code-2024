data = open('input-day-25.txt','r').read().split('\n\n')

max_length = 0

locks, keys = [],[]

lock_key_fit_counter = 0

def extract_pins(obj, start, stop, step, pin_offset):

    pins = []

    for col_no in range(len(obj[0])):

        for row_no in range(start, stop, step):

            if obj[row_no][col_no] == '.':

                pins.append(abs(row_no+pin_offset))

                break

    return pins

for e in data:

    e = e.split('\n')

    max_length = len(e)

    if e[0][0] == '#':
        locks.append(extract_pins(e, 0, len(e), 1, -1))
    else:
        keys.append(extract_pins(e, -1, -(len(e)+1), -1, 2))

for l in locks:

    for k in keys:
        
        summed_list = [x+y for x,y in zip(l,k) if x+y < max_length-1]

        if len(summed_list) == len(k):

            lock_key_fit_counter += 1

print("Answer Puzzle#1:", lock_key_fit_counter)