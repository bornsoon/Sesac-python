from flask import Flask ,render_template, request
import csv
import math

csv_data = []
headers = []

def load_csv_data(filename):
    global headers # 바깥 scope (글로벌 variable) 의 내용을 변경하려고 할 때 선언해야함
    with open(filename, newline='', encoding='utf=8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        headers = [fieldname.strip() for fieldname in csv_reader.fieldnames]
        for row in csv_reader:
            clean_row = {fieldname.strip(): value.strip() for fieldname, value in row.items()}
            csv_data.append(clean_row)

app = Flask(__name__)

@app.route("/")
@app.route("/<int:page>")
def index(page=1):
    per_page = 10    # 한 페이지에 보여줄 항목 수

    start_index = (page - 1) * per_page
    end_index = page * per_page

    total_pages = math.ceil(len(csv_data) / per_page)

    current_pages = csv_data[start_index:end_index]

    # current_pages 안에 index 추가하기
    for i, item in enumerate(current_pages, start =start_index + 1):
        item['index'] = i

    print(f'현재페이지 데이터2: {current_pages}')

    return render_template('index3.html', headers=headers, users=current_pages, total_pages=total_pages)

@app.route("/user/<uuid>")
def user_detail(uuid):
    for u in csv_data:
        if u['Id']==uuid:
            user = u
    return render_template('user_detail.html', headers=headers, user=user)


if __name__ =='__main__':
    load_csv_data('./users.csv')                # 여기에서 로딩해야 한 번만 하고 끝남.
    app.run(debug=True)
    print(csv_data)
    print(headers)