import csv

file_path = "mydata.csv"

with open(file_path, 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        print(row['Name']) # 딕셔너리라서 키로 참조(리퍼런싱) 가능