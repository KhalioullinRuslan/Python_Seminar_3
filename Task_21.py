# Задача №21. 
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# Dictionary = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
# {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# print("Original List: ", Dictionary)

# d_value = set(val for dic in Dictionary for val in dic.values())
# print("Dictionary Values: ", d_value)

slov = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
 {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
res = set()

for i in slov:
    for k,v in i.items():
        res.add(v.strip())
print(res)