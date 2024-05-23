import csv

file_path = "mydata.csv"

with open(file_path, 'r', encoding='utf-8') as file:  # 파일에 한글 포함되면 encoding='utf-8'
    csv_reader = csv.reader(file)

    for row in csv_reader:
        print(row)