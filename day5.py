
coordinates = {}
coordinates_list = []
with open('day5_input.txt') as f:
    data = f.read()
    temp_coordinates_list = [line.split(' -> ') for line in data.split('\n')]
    for list in temp_coordinates_list:
        for pair in list:
            coordinates_list.append(tuple(pair.split(',')))


for i in range(0,len(coordinates_list),2):
    coordinates[coordinates_list[i]] = coordinates_list[i+1]




#print(coordinates)
# keep track of horizontal / vertical line points
#coordinate_tracker = {}.fromkeys(coordinates_list, 0)
coordinate_tracker = {}

for i in range(0, 1000):
    for j in range(0,1000):
        coordinate_tracker[(str(i), str(j))] = 0

#print(coordinate_tracker)

for start, end in coordinates.items():
    if (start[0] != end[0]) and (start[1] != end[1]):
        continue
    else:
        coordinate_tracker[start] += 1
        coordinate_tracker[end] += 1
        if start[0] == end[0]:
            i = 1

            # if end is greater than start coordinate, go forward from start coordinate and track
            if int(start[1]) < int(end[1]):
                while int(start[1]) + i < int(end[1]):
                    coordinate_tracker[start[0], str(int(start[1]) + i)] += 1
                    i += 1
            # if start is greater than end coordinate, go forward from end coordinate and track
            else:
                while int(end[1]) + i < int(start[1]):
                    coordinate_tracker[end[0], str(int(end[1]) + i)] += 1
                    i += 1

        if start[1] == end[1]:
            i = 1

            # if end is greater than start coordinate, go forward from start coordinate and track
            if int(start[0]) < int(end[0]):
                while int(start[0]) + i < int(end[0]):
                    coordinate_tracker[str(int(start[0]) + i), start[1]] += 1
                    i += 1
            # if start is greater than end coordinate, go forward from end coordinate and track
            else:
                while int(end[0]) + i < int(start[0]):
                    coordinate_tracker[str(int(end[0]) + i), end[1]] += 1
                    i += 1
                
# need to add intermediate coordinates to tracker

counter = 0
for key, value in coordinate_tracker.items():
    if value > 1:
        counter += 1
        pass

print(counter)


# day 2 

coordinate_tracker = {}

for i in range(0, 1000):
    for j in range(0,1000):
        coordinate_tracker[(str(i), str(j))] = 0

#print(coordinate_tracker)

for start, end in coordinates.items():
    if (start[0] == end[0]) or (start[1] == end[1]):
        coordinate_tracker[start] += 1
        coordinate_tracker[end] += 1
        if start[0] == end[0]:
            i = 1

            # if end is greater than start coordinate, go forward from start coordinate and track
            if int(start[1]) < int(end[1]):
                while int(start[1]) + i < int(end[1]):
                    coordinate_tracker[start[0], str(int(start[1]) + i)] += 1
                    i += 1
            # if start is greater than end coordinate, go forward from end coordinate and track
            else:
                while int(end[1]) + i < int(start[1]):
                    coordinate_tracker[end[0], str(int(end[1]) + i)] += 1
                    i += 1

        if start[1] == end[1]:
            i = 1

            # if end is greater than start coordinate, go forward from start coordinate and track
            if int(start[0]) < int(end[0]):
                while int(start[0]) + i < int(end[0]):
                    coordinate_tracker[str(int(start[0]) + i), start[1]] += 1
                    i += 1
            # if start is greater than end coordinate, go forward from end coordinate and track
            else:
                while int(end[0]) + i < int(start[0]):
                    coordinate_tracker[str(int(end[0]) + i), end[1]] += 1
                    i += 1

    if abs(int(start[0]) - int(end[0])) == abs(int(start[1]) - int(end[1])):
        coordinate_tracker[start] += 1
        coordinate_tracker[end] += 1

        # if going northwest
        if int(start[0]) > int(end[0]) and int(start[1]) > int(end[1]):
            i = 1
            while int(start[0]) - i > int(end[0]) and int(start[1]) - i > int(end[1]):
                coordinate_tracker[str(int(start[0]) - i), str(int(start[1]) - i)] += 1
                i += 1

        # if going northeast
        if int(start[0]) < int(end[0]) and int(start[1]) > int(end[1]):
            i = 1
            while int(start[0]) + i < int(end[0]) and int(start[1]) - i > int(end[1]):
                coordinate_tracker[str(int(start[0]) + i), str(int(start[1]) - i)] += 1
                i += 1

        # if going southwest
        if int(start[0]) > int(end[0]) and int(start[1]) < int(end[1]):
            i = 1
            while int(start[0]) - i > int(end[0]) and int(start[1]) + i < int(end[1]):
                coordinate_tracker[str(int(start[0]) - i), str(int(start[1]) + i)] += 1
                i += 1
        
        # if going southeast
        else:
            i = 1
            while int(start[0]) + i < int(end[0]) and int(start[1]) + i < int(end[1]):
                coordinate_tracker[str(int(start[0]) + i), str(int(start[1]) + i)] += 1
                i += 1                    
        
    else:
        continue
                
# need to add intermediate coordinates to tracker

counter = 0
for key, value in coordinate_tracker.items():
    if value > 1:
        counter += 1
        pass

print(counter)