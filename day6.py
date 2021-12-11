
angler_states = []
with open('day6_input.txt') as f:
    data = f.read()
    angler_states = data.split(',')

angler_states = [int(datapoint) for datapoint in angler_states]

# day 1

#print(angler_states)
fish_dict = {}
# setting default values for dictionary
for i in range(9):
    fish_dict[i] = 0

# setting initial values for dictionary
for countdown in angler_states:
    fish_dict[countdown] += 1

# checking dictionary
print(fish_dict)

# for each day, create a new dictionary and shift each population down a day. Then, check to see if the key has gone under 0, if so update 6/8 keys in original dictionary.
# for part 1, use range(80). for part 2, use range(256)
for day in range(256):
    temp_fish_dict = {}
    for key, population in fish_dict.items():
        new_key = key - 1
        temp_fish_dict[new_key] = population
        fish_dict[key] = 0
    
    for new_key, population in temp_fish_dict.items():
        if new_key < 0:
            fish_dict[6] += population
            fish_dict[8] += population
        else:
            fish_dict[new_key] += population

print(fish_dict)
total_fish = 0
for key, value in fish_dict.items():
    total_fish += value

print(total_fish)
