import csv
import os

ofile = open('test_write.csv', "wb")
fieldnames = ['id', 'fname', 'lname', 'college', 'grad_year', 'github']
writer = csv.DictWriter(ofile, fieldnames=fieldnames)
accept_ids = []

with open('resumes.csv') as file2:
    reader2 = csv.DictReader(file2)
    for row in reader2:
        accept_ids.append(row['id'])

data = []

with open('form.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['id'] in accept_ids:
           #data.append([row['id'], row['fname'], row['lname'], row['college'], row['grad_year'], row['github']])
           writer.writerow({'fname':row['fname'], 'lname':row['lname'], 'college':row['college'], 'grad_year':row['grad_year'], 'github': row['github']})

# data.pop(0)
#
# for individual in data:
#     individual[3] = individual[3][62:-9]
#     if len(individual) == 4:
#         for i in range(len(individual[3]) - 1, 0, -1):
#             if individual[3][i] == ".":
#                 individual.append(individual[3][i:])
#
#     print individual[3]
#     try:
#         os.rename(individual[3], '_' + individual[1].strip() + '_' + individual[2].strip() + individual[4].strip())
#     except OSError:
#         print "error   " + individual[3]
