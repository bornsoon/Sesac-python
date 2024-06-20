from flask import Flask, request

app = Flask(__name__)

# @app.route('/user', methods=['GET', 'POST', 'DELETE'])
# def get_user():
#     if request.method == "POST":
#         return "<H1>요청에 의한 데이터 생성</H1>"
#     if request.method == "DELETE":
#         return "<H1>요청에 의한 데이터 삭제</H1>"
    
#     return "<H1>정보 제공</H1>"

@app.route('/user', methods=['GET'])
def get_user():
    return "<H1>정보 제공</H1>"

@app.route('/user', methods=['POST'])
def post_user():
    return "<H1>요청에 의한 데이터 생성</H1>"

@app.route('/user', methods=['DELETE'])
def delete_user():
    return "<H1>요청에 의한 데이터 삭제</H1>"

if __name__== "__main__":
    app.run(debug=True)