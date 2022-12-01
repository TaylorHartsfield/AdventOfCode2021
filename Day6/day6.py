file = open('input.txt', 'r')
data = file.read().split(',')


def jellyfish_babies(data):
    
    day = 1
    loops = 0
    while day <= 80:
        for fish in data:
            loops+=1
            fish = int(fish)
            fish -= 1
            if fish == 0:
                fish = 6
                data.append(8)
        day += 1
    
    print(loops)
    return len(data)


print(jellyfish_babies(data))