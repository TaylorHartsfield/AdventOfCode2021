text = open('input.txt', 'r')
values = text.read().split('\n')
values.remove('')
data = [i.split(' ') for i in values]

# part 1 // CORRECT ⭐️
def dive(depths):

    forward = 0
    depth = 0

    for direction in depths:
        if direction[0].startswith('f'):
            forward += int(direction[1])
        elif direction[0].startswith('u'):
            depth -= int(direction[1])
        else:
            depth += int(direction[1])

    return forward*depth

#part 2 // CORRECT ⭐️
def dive_with_aim(depths):

    forward = 0
    depth = 0
    aim = 0
    
    for direction in depths:
        if direction[0].startswith('f'):
            forward += int(direction[1])
            depth += (int(direction[1])*aim)
        elif direction[0].startswith('u'):
            aim -= int(direction[1])
        else:
            aim += int(direction[1])

    return forward*depth
