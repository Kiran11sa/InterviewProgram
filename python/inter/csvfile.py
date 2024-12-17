import csv

data=0
with open('inter.csv','r') as file:
    csv_read=csv.DictReader(file)
    print(" / ".join(csv_read.fieldnames))  # Print header names joined with " | " separator

    for i in csv_read:
        print(i['name'],i['age'],i['company'])
