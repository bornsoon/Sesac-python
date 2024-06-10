from flask import Flask

app = Flask(__name__)

@app.route("/")     # 데코레이터
def home():
    return "<HTML><BODY><H1>나의 헤딩</H1><P>여기는 나의 문장이 들어갑니다.</P></BODY></HTML>"

@app.route("/user/") 
@app.route("/user/<name>")  # <name> 변수임 -> 아 변수명과 함수의 인자를 매칭해서 내부에서 처리
def user(name=None):
    username = name
    print(username)

    return f"""<HTML><BODY><H1>사용자의 페이지: {username}님 안녕하세요.
    </H1><P>여기는 {username}의 소개 내용이 들어갑니다.</P></BODY></HTML>"""

@app.route("/admin") 
def admin():
    return "<HTML><BODY><H1>관리자 페이지</H1><P>여기는 나의 문장이 들어갑니다.</P></BODY></HTML>"

if __name__=="__main__":
    app.run(port=5000, debug=True)  # 개발 환경에서만 사용해야 함... 배포하는 production에서는 debug는 항상 OFF()