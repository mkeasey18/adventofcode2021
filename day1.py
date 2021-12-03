import csv, re


depth_measurements = []
with open('depth_measurements.csv') as f:
    csv_reader = csv.reader(f)
    num_regex = re.compile(r'\d+')
    for row in csv_reader:
        mo1 = num_regex.search(row[0])
        depth_measurements.append(int(mo1.group()))

increase_count = 0
previous_num = depth_measurements[0]
for num in depth_measurements:
    if num > previous_num:
        increase_count += 1
    previous_num = num

print(increase_count)

# part 2

group_list = []
for i in range(0,len(depth_measurements)):
    try:
        group_list.append(depth_measurements[i] + depth_measurements[i+1] + depth_measurements[i+2])
    except IndexError:
        continue

previous_num = group_list[0]
increase_count = 0
for num in group_list:
    if num > previous_num:
        increase_count += 1
    previous_num = num

print(increase_count)