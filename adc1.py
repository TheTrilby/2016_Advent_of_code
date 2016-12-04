
#print 'test'

input = open('input').read()

#input = 'R3, L5, R2, L1, L2, R5, L2, R2, L2, L2, L1, R2, L2, R4, R4, R1, L2, L3, R3, L1, R2, L2, L4, R4, R5, L3, R3, L3, L3, R4, R5, L3, R3, L5, L1, L2, R2, L1, R3, R1, L1, R187, L1, R2, R47, L5, L1, L2, R4, R3, L3, R3, R4, R1, R3, L1, L4, L1, R2, L1, R4, R5, L1, R77, L5, L4, R3, L2, R4, R5, R5, L2, L2, R2, R5, L2, R194, R5, L2, R4, L5, L4, L2, R5, L3, L2, L5, R5, R2, L3, R3, R1, L4, R2, L1, R5, L1, R5, L1, L1, R3, L1, R5, R2, R5, R5, L4, L5, L5, L5, R3, L2, L5, L4, R3, R1, R1, R4, L2, L4, R5, R5, R4, L2, L2, R5, R5, L5, L2, R4, R4, L4, R1, L3, R1, L1, L1, L1, L4, R5, R4, L4, L4, R5, R3, L2, L2, R3, R1, R4, L3, R1, L4, R3, L3, L2, R2, R2, R2, L1, L4, R3, R2, R2, L3, R2, L3, L2, R4, L2, R3, L4, R5, R4, R1, R5, R3'

# Tests
#input = 'R2, L3' # should be 5 blocks away
#input = 'R2, R2, R2' # should be 2 blocks
#input = 'R5, L5, R5, R3' # should be 12 blocks

directions = input.strip().split(', ')

#print directions[0:5]


def track(orientation, coordinates, turn, blocks):
    
    x = coordinates[0]
    y = coordinates[1]
    
    newspot = {
    ('North', 'L'): [(x - blocks, y), 'West'],
    ('North', 'R'): [(x + blocks, y), 'East'],
    ('South', 'L'): [(x + blocks, y), 'East'],
    ('South', 'R'): [(x - blocks, y), 'West'],
    ('West', 'L'): [(x, y - blocks), 'South'],
    ('West', 'R'): [(x, y + blocks), 'North'],
    ('East', 'L'): [(x, y + blocks), 'North'],
    ('East', 'R'): [(x, y - blocks), 'South']
    }
    
    coordinates = newspot[(orientation, turn)][0]
    orientation = newspot[(orientation, turn)][1]
    
    return orientation, coordinates


def travel(directions, coordinates, orientation):
    for direction in directions:
        newstart = track(orientation, coordinates, direction[0], int(direction[1:]))
        orientation = newstart[0]
        coordinates = newstart[1]
    return coordinates



start_coordinates = (0,0)
start_orientation = 'North'

final = travel(directions, start_coordinates, start_orientation)

print final


