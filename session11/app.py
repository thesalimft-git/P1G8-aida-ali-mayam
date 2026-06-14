# with open('session11/sample.txt', '+r') as f:
#     print(f.readline())
#     print(f.readlines())
#     print(f.write('some text'))




# import json
# data = {'name': 'ali', 'age': 17}
# with open('session11/sample.json', 'w') as f:
#     json.dump(data, f)


# with open('session11/sample.json', 'r') as f:
#     print(json.load(f))


import csv

with open('session11/sample.csv', 'r') as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)