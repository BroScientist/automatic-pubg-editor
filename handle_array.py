action_point_list = [
     550,
     575,
     600,
     625,
     650,
     675,
     1075,
     1100,
     1125,
     1150,
     1375,
     1400,
     1425,
     1450,
     1650,
     1675,
     1700,
     1850,
     1875,
     1900,
     1925,
     2175,
     2200,
     2225,
     2250,
     2275,
     2300,
     2325,
     2350,
     2675,
     2700,
     2725,
     2750,
     2775,
     2800,
     3275,
     3300,
     3350,
     3400,
     3425,
     3450,
     3550,
     3575,
     3600,
     3625
]

new = []




# def perform_action(current_index):
#
#     group = []
#     i = current_index
#     curr = action_point_list[i]
#     next = action_point_list[i+1]
#     while (curr + 125) > next:
#         group.append(curr)
#         i += 1
#         curr = action_point_list[i]
#         next = action_point_list[i + 1]
#     new.append(group)
#     # print(group)
#     group = []
#     current_index = i
#     print(i)
#     # if current_index < len(action_point_list):
#     #      perform_action(current_index)
#     print(new)
#
# perform_action(0)
#
# for index, item in enumerate(action_point_list):
#     if (item + 125) > action_point_list[index+1]:
#         del action_point_list[index+1]

index = 0
while index != len(action_point_list):
    try:
        group = []
        curr = action_point_list[index]
        next = action_point_list[index + 1]
        while (curr + 125) > next:
            group.append(curr)
            index += 1
            curr = action_point_list[index]
            next = action_point_list[index + 1]
        new.append(group)
    except IndexError:
        pass
    finally:
        index += 1

    print(index)

results = []
for item in new:
    print(item[0], item[-1])
    results.append((item[0], item[-1]))

print(results)