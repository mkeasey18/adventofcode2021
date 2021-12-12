import statistics

initial_positions = []
with open('day7_input.txt') as f:
    data = f.read()
    initial_positions = [int(line) for line in data.split(',')]

#print(initial_positions)

# day 1
median = statistics.median(initial_positions)
#print(median)


fuel = 0

for position in initial_positions:
    fuel += abs(median - position)

print(fuel)

# day 2

point_dict = {}
for i in range(max(initial_positions)+1):
    point_dict[i] = float('inf')

for point in point_dict.keys():
    total_fuel = 0
    for crab in initial_positions:
        distance = abs(crab - point)
        for i in range(1, distance + 1):
            total_fuel += i
    point_dict[point] = total_fuel

least_fuel = float('inf')
for key, value in point_dict.items():
    if value < least_fuel:
        least_fuel = value
    else:
        continue
print(least_fuel)

