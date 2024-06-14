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
def search1(page=1):
    # per_page = request.args.get('per_page')    # 한 페이지에 보여줄 항목 수
    per_page = 10
    print('----------------')
    print(per_page)
    
    start_index = (page - 1) * per_page
    end_index = page * per_page

    headers = csv_data[0]

    total_pages = math.ceil(len(csv_data) / per_page)

    current_pages = csv_data[start_index:end_index]

    index_pages = []
    for i in range(len(current_pages)):
        index_pages.append({'index': i+1} | current_pages[i])

    return render_template('index3.html', headers=headers, users=index_pages, total_pages=total_pages)


@app.route("/search")
def search2(page=1):
    per_page = int(request.args.get('per_page'))
    print('----------------')
    print(per_page)
    start_index = (page - 1) * per_page
    end_index = page * per_page

    name = request.args.get('name')

    headers = csv_data[0]

    filtered_csv_data = []
    for u in csv_data:
        if name in u['Name']:
            filtered_csv_data.append(u)

    total_pages = math.ceil(len(filtered_csv_data) / per_page)

    current_pages = filtered_csv_data[start_index:end_index]
    
    index_pages = []
    for i in range(len(current_pages)):
        index_pages.append({'index': i+1} | current_pages[i])

    return render_template('index3.html', headers=headers, users=index_pages, total_pages=total_pages)


if __name__ =='__main__':
    load_csv_data('./users.csv')                # 여기에서 로딩해야 한 번만 하고 끝남.
    app.run(debug=True)
    # print(csv_data)
    # print(headers)