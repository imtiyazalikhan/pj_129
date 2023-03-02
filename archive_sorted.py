import csv

data = []

with open("total_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        data.append(row)

headers = data[0]
star_data = data[1:]

#Converting all planet names to lower case
for data_point in star_data:
    data_point[2] = data_point[2].lower()

#Sorting planet names in alphabetical order
star_data.sort(key=lambda star_data: star_data[2])


with open("unit_converted_stars.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)

#remove blank lines
with open('unit_converted_stars.csv') as input, open('star_with_gravity.csv', 'w', newline='') as output:
     writer = csv.writer(output)
     for row in csv.reader(input):
         if any(field.strip() for field in row):
             writer.writerow(row)