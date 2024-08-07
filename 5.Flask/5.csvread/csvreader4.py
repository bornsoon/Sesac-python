from flask import Flask ,render_template, request
import csv
import math

csv_data = []
headers = []

def load_csv_data(filename):
    global headers # 바깥 scope (글로벌 variable) 의 내용을 변경하려고 할 때 선언해야함
    global csv_data
    with open(filename, newline='', encoding='utf=8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        headers = [fieldname.strip() for fieldname in csv_reader.fieldnames]
        for row in csv_reader:
            clean_row = {fieldname.strip(): value.strip() for fieldname, value in row.items()}
            csv_data.append(clean_row)
    return csv_data

app = Flask(__name__)

@app.route("/")
def search():
    page = int(request.args.get('page', default=1))
    per_page = int(request.args.get('per_page', default=10))    # 한 페이지에 보여줄 항목 수
    
    start_index = (page - 1) * per_page
    end_index = page * per_page

    name = request.args.get('name')
    data = []
    if name:
        for u in csv_data:
            if name in u['Name']:
                data.append(u)   
    else:
        name = ''
        data = csv_data

    total_pages = math.ceil(len(data) / per_page)
    current_pages = data[start_index:end_index]

    index_pages = []
    for i in range(len(current_pages)):
        index_pages.append({'index': i+1} | current_pages[i])

    return render_template('index4.html', headers=headers, users=index_pages, total_pages=total_pages, per_page=per_page, current_page=page, name=name)


@app.route("/user/<id>")
def user_detail(id):
    headers = csv_data[0]
    print(id)
    for u in csv_data:
        if u['Id'] == id:
            user = u
    print(user)
    return render_template('user_detail.html', headers=headers, user=user)

if __name__ =='__main__':
    csv_data = load_csv_data('./users.csv')                # 여기에서 로딩해야 한 번만 하고 끝남.
    app.run(debug=True)
    # print(csv_data)
    # print(headers)