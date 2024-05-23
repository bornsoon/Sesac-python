import csv

file_path = 'mydata.csv'

data = [
    {"Name":"John", "Age":20, "City":"Seoul"},
    {"Name":"Jane", "Age":25, "City":"Busan"},
    {"Name":"Bob", "Age":35, "City":"Jeju"}
]

with open(file_path, 'w', encoding='utf-8', newline='') as file:
    # headers = ["Name", "Age", "City"]
    headers = data[0].keys()
    
    csv_writer = csv.DictWriter(file, fieldnames=headers)

    # 헤더 쓰기
    csv_writer.writeheader()

    # 본문 데이터 쓰기
    csv_writer.writerows(data)

print('CSV 파일 작성 완료')