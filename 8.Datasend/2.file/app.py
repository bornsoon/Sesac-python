from flask import Flask, render_template, request
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'

# 미리 폴더가 있으면 무방함.. 근데 없으면... 만들어 주는 코드를 짜거나. 아니면 직접 만들어주거나..
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return "<H1>파일 저장 완료</H1>"
    else:
        return "<H1>파일 없음!!</H1>"



if __name__ == "__main__":
    app.run(debug=True)