import csv

data1 = []
data2 = []

with open("Scraper.csv","r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data1.append(row)

with open("Scraper2.csv","r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data2.append(row)
    
headers = data2[0]
star_data = []

star_data = data1[1] + data2[1]

with open("final_Scaper.csv","a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(star_data)