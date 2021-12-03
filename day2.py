
# Open file, use readlines to split each line into rows, strip whitespace and split on the space to create a list of directions
submarine_directions = []
with open('day2_submarine_directions.txt', newline='') as f:
    for row in f.readlines():
        submarine_directions.append(row.strip().split(' '))

horizontal_position = 0
depth_position = 0

for direction_group in submarine_directions:
    if direction_group[0] == 'forward':
        horizontal_position += int(direction_group[1])
    elif direction_group[0] == 'down':
        depth_position += int(direction_group[1])
    else:
        depth_position -= int(direction_group[1])

multiplied_coordinates = horizontal_position * depth_position
print('Part 1')
print(horizontal_position)
print(depth_position)
print(multiplied_coordinates)


# part 2

horizontal_position = 0
depth_position = 0
aim = 0

for direction_group in submarine_directions:
    if direction_group[0] == 'forward':
        horizontal_position += int(direction_group[1])
        depth_position += int(direction_group[1])*aim
    elif direction_group[0] == 'down':
        aim += int(direction_group[1])
    else:
        aim -= int(direction_group[1])

multiplied_coordinates = horizontal_position * depth_position
print('Part 2')
print(horizontal_position)
print(depth_position)
print(multiplied_coordinates)