text = open('input.txt', 'r')
values = text.read().split('\n')
values.remove('')
to_ints = list(map(int, values))


#part 1 // CORRECT ⭐️
def increased_depth(depths):

    i = 1
    total_increase = 0
    while i < len(depths):
        if depths[i] > depths[i - 1]:
            total_increase += 1
        i += 1

    return total_increase


# part2 // CORRECT ⭐️
def sliding_window(depths):
    increase = 0
    i = 0
    j = 2

    while j < len(depths):
        val1 = sum(depths[i:j+1])
        val2 = sum(depths[i+1:j+2])
        if val2 > val1:
            increase += 1
        i += 1
        j += 1

    return increase