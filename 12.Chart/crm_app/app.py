from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    data = {
        'labels' : ['2023-01', '2023-02','2023-03', '2023-04', '2023-05', '2023-06'],
        'revenue' : [797000, 401000, 650000, 660000, 560000, 700000]
    }
    return jsonify(data)  # JSON은 '' 안됨 -> "" 만 됨 / dict는 '' 도 ok


if __name__ == '__main__':
    app.run(debug=True)