import day3_input

diagnostic_data = day3_input.diagnostic_data.split('\n')

# part 1
gamma = ''
epsilon = ''

for column in range(0,len(diagnostic_data[0])):
    counter_1 = 0
    counter_0 = 0
    for row in range(0,len(diagnostic_data)):
        if diagnostic_data[row][column] == '0':
            counter_0 += 1
        else:
            counter_1 += 1
    if counter_0 > counter_1:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

gamma_dec = int(gamma, base=2)
epsilon_dec = int(epsilon, base=2)
power = gamma_dec * epsilon_dec
#print(gamma_dec)
#print(epsilon_dec)
#print(power)

# part 2

# making copies of lists to maintain data integrity
CO2_possibles = diagnostic_data.copy()
O2_possibles = diagnostic_data.copy()

def get_O2(datalist):
    for column in range(0,len(datalist[0])):
        counter_1 = 0
        counter_0 = 0
        list_of_0 = []
        list_of_1 = []
        for row in range(0,len(datalist)):
            if datalist[row][column] == '0':
                counter_0 += 1
                list_of_0.append(datalist[row])
            else:
                counter_1 += 1
                list_of_1.append(datalist[row])
        # below is the only different in function code
        if counter_0 > counter_1:
            datalist = list_of_0
        else:
            datalist = list_of_1
        if len(datalist) == 1:
            return str(datalist[0])
            break

def get_CO2(datalist):
    for column in range(0,len(datalist[0])):
        counter_1 = 0
        counter_0 = 0
        list_of_0 = []
        list_of_1 = []
        for row in range(0,len(datalist)):
            if datalist[row][column] == '0':
                counter_0 += 1
                list_of_0.append(datalist[row])
            else:
                counter_1 += 1
                list_of_1.append(datalist[row])
        # below is the only difference function code
        if counter_0 > counter_1:
            datalist = list_of_1
        else:
            datalist = list_of_0
        if len(datalist) == 1:
            return str(datalist[0])
            break
        
O2_binary = get_O2(O2_possibles)
CO2_binary = get_CO2(CO2_possibles)

O2_dec = int(O2_binary, base=2)
CO2_dec = int(CO2_binary, base=2)
life_support = CO2_dec * O2_dec

print('O2:',O2_binary,O2_dec)
print('CO2',CO2_binary,CO2_dec)
print('Life Support:', life_support)