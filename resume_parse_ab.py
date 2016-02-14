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

for ind in data:
    ind[3] = ind[3][62:-9]
    if len(ind) == 4:
        for i in range(len(ind[3]) - 1, 0, -1):
            if ind[3][i] == ".":
                ind.append(ind[3][i:])

    print ind[3]
    try:
        os.rename(ind[3], '_' + ind[1].strip() + '_' + ind[2].strip() + ind[4].strip())
    except OSError:
        print "error   " + ind[3]
