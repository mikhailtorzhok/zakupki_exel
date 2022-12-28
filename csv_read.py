import csv
with open('Корреспонденты.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)