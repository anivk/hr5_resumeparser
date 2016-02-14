import csv
import os

ofile = open('test_write.csv', "wb")
fieldnames = ['id', 'fname', 'lname', 'resume']
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
           data.append([row['id'], row['fname'], row['lname'], row['resume']])
           #print row['id'], row['fname'], row['lname']
           #writer.writerow({'id':row['id'], 'fname':row['fname'], 'lname':row['lname'], 'resume':row['resume']})

data.pop(0)

count = 0

for individual in data:
    individual[3] = individual[3][62:-9]
    count += 1
    if len(individual) == 4:
        for i in range(len(individual[3]) - 1, 0, -1):
            if individual[3][i] == ".":
                individual.append(individual[3][i:])

    print individual[3]
    os.rename(individual[3], '_' + individual[1].strip() + '_' + individual[2].strip() + individual[4].strip())
