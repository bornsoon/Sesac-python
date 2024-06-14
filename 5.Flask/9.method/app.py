from flask import Flask, render_template, request

app = Flask(__name__)

users = [
    {'name': 'Alice', 'id':'alice', 'pw':'alice'},
    {'name': 'Bob', 'id':'bob', 'pw':'bob1234'},
    {'name': 'Charlie', 'id':'charlie', 'pw':'hello'}
]

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])  # 메소드 지정  GET > header , POST > body
def home():
    id = request.args.get('id')   # 이거는 GET방식의 URL 파라미터를 처리할 때만 가능한 방법

    if request.method == 'POST':
        id = request.form['id']  # 여기는 POST방식 중에서, FORM-Data를 처리할 때 payload를 받아오는 방법
        pw = request.form['password']  # 여기는 POST방식 중에서, FORM-Data를 처리할 때 payload를 받아오는 방법

    # 위에 있는 user 목로과 입력학 id/pw 를 비교해서, print로 로그인 혀용/불허 출력
        # user = None
        # for u in users:
        #     if id == u['id'] and pw == u['pw']:
        #         print('매치되는 사용자가 있음!!!')
        #         user = u
        # 위 5줄짜리 코드를 1줄로, next() 함수와 list comprehenstion으로 작성하기
        # next() 함수는, next(iteration 조건은, 기본값) 형태로 구성됨
        user = next((user for user in users if user['id'] == id and user['pw']==pw), None)

        print(f'입력한ID: {id}, 입력한PW: {pw}')

        if user:
            print(f"로그인한 사용자는 {user['name']}입니다")
            message = None
            # return f'<H1>로그인 성공!!</H1>'
        else:
            print(f"로그인 가능한 사용자가 없습니다. id={id}")
            message = '로그인 실패'
            # return f'<H1>로그인 실패!!</H1>'

        return render_template('index.html', user=user, error=message)
    
    # else:
        # GET 요청에 대한 처리

    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)