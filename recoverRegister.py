import csv

with open('myfile.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
