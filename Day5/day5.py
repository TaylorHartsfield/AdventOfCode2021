file = open('input.txt', 'r')
data = file.read().split('\n')

def multiple_points(data):

    line_data = {}
    total_points = 0

    for line in data:

        value = line.split(',')

        x_one = int(value[0])
        y_one = int(value[1].split(' ')[0])
        x_two = int(value[1].split(' ')[2])
        y_two = int(value[2])

        if x_one == x_two:
            for point in range(min(y_one,y_two), (max(y_two,y_one)+1)):
                if (x_one, point) in line_data:
                    line_data[(x_one, point)] += 1
                    if line_data[(x_one, point)] == 2:
                        total_points += 1
                else:
                    line_data[(x_one, point)] = 1
                
        elif y_one == y_two:
            for point in range(min(x_one,x_two), (max(x_two,x_one)+1)):
                if (point, y_one) in line_data:
                    line_data[(point, y_one)] += 1
                    if line_data[(point, y_one)] == 2:
                        total_points += 1
                else:
                    line_data[(point, y_one)] = 1
        
        else:
            if x_one > x_two:
                while x_one >= x_two:
                    if (x_one, y_one) in line_data:
                        line_data[(x_one, y_one)] += 1
                        if line_data[(x_one, y_one)] == 2:
                            total_points += 1      
                    else:
                        line_data[(x_one, y_one)] = 1

                    if y_one < y_two:
                        y_one += 1
                    else:
                        y_one -= 1
                    x_one -= 1

            elif x_one < x_two:
                while x_one <= x_two:
                    if (x_one, y_one) in line_data:
                        line_data[(x_one, y_one)] += 1
                        if line_data[(x_one, y_one)] == 2:
                            total_points += 1
                    else:
                        line_data[(x_one, y_one)] = 1

                    if y_one < y_two:
                        y_one += 1
                    else:
                        y_one -= 1
                    x_one += 1


    return total_points

#part1  & part2 // CORRECT ⭐️ ⭐️
multiple_points(data)

