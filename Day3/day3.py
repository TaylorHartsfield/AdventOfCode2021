file = open('input.txt', 'r')
data = file.read().split('\n')

#part1 // CORRECT ⭐️
def gamma_and_epsilon_rate(data):

    gamma = ""
    epsilon = ""
    
    for i in range(12):
        count1 = 0
        count0 = 0
        for entry in data:
            if entry[i] == "1":
                count1 +=1
            else:
                count0 +=1
        
        if count1>count0:
            gamma+= "1"
            epsilon +="0"
        else:
            epsilon+="1"
            gamma+="0"

    return (int(gamma, 2)) * (int(epsilon, 2))


# part 2 // CORRECT ⭐️
def life_support_rating(data):


    oxygen_data = data
    co2_data = data
    oxygen = ""
    co2 = ""
     
    for i in range(12):
        count1 = 0
        count0 = 0

        for entry in oxygen_data:
            if entry[i] == "1":
                count1 +=1
            else:
                count0 +=1

        if count1 >= count0:
            oxygen_data = [item for item in oxygen_data if item[i] == '1']
        else:
            oxygen_data = [item for item in oxygen_data if item[i] == '0']
        
        if len(oxygen_data) == 1:
            oxygen = int(oxygen_data[0],2)


    for i in range(12):

        count1 = 0
        count0 = 0

        for entry in co2_data:
            if entry[i] == "1":
                count1 +=1
            else:
                count0 +=1
        if count1 >= count0:
            co2_data = [item for item in co2_data if item[i] == "0"]
        else:
            co2_data = [item for item in co2_data if item[i] == '1']
                
        if len(co2_data) == 1:
            co2 = int(co2_data[0], 2)


    return oxygen*co2
