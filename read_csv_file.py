import csv

with open('some.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# DictReader () method to read particular column name:
reader = csv.DictReader(open(r"C:\Users\HP\Desktop/data.csv"))
for raw in reader:
print(raw)
        
with open('test.csv') as f:
    DictReader_obj = csv.DictReader(f)
    for item in DictReader_obj:
        print(item['Month'])
