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


print(gamma_and_epsilon_rate(data))