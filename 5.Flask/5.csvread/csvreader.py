from flask import Flask ,render_template, request
import csv
import math

csv_data = []

def load_csv_data(filename):
    with open(filename, newline='', encoding='utf=8') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            csv_data.append(row)

app = Flask(__name__)

@app.route("/")
@app.route("/<int:page>")
def search1(page=1):
    per_page = 10    # 한 페이지에 보여줄 항목 수

    start_index = (page - 1) * per_page
    end_index = page * per_page

    headers = csv_data[0]
    csv_data1 = csv_data[1:]

    total_pages = math.ceil(len(csv_data1) / per_page)

    current_pages = csv_data1[start_index:end_index]

    return render_template('index.html', headers=headers, users=current_pages, total_pages=total_pages)

if __name__ =='__main__':
    load_csv_data('./users.csv')                # 여기에서 로딩해야 한 번만 하고 끝남.
    app.run(debug=True)
    