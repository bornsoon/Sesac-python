from flask import Flask, render_template, request, session, redirect, url_for, flash
from datetime import timedelta
import database as db

app = Flask(__name__)
app.secret_key = 'hello1234'
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']


        # prepared statement('?')를 통해서 입력 받게 되어 있다
        # '?' <- 입력값을 정제해서 처리하는 기능이 이미 포함되어 있음 
        # 입력값에 대한 검증이 중요함!!!!!!!!!!!!!
        #  
        # query = "SELECT * FROM users WHERE username = ? AND password = ?"
        query = f"SELECT * FROM users WHERE username = '{username}' AND password='{password}';"
        # user1 --> user1' --   (--로 마지막 따옴표 주석처리)
        # password --> ' OR 1=1 --   (--로 마지막 따옴표 주석처리)
        # user_data = db.get_query(query, (username, password))
        user_data = db.get_query(query)
        print(f'조회된 사용자: ', user_data)
        print([dict(row) for row in user_data])

        # if len(user_data) == 1:     #and user_data['password'] == password:
        if len(user_data):     #and user_data['password'] == password:
            session['user'] = user_data[0]["username"]
            if "email" in user_data[0]:
                session['email'] = user_data[0]["email"]
            session.permanent = True
            flash('로그인에 성공하였습니다.')  
            return redirect(url_for("home"))
        else:
            print('패스워드 틀림!!')
            flash('아이디/패스워드가 일치하지 않습니다.')
            return redirect(url_for("login"))
    
    else:
         # GET 요청이라서 로그인 폼 보여주기
        if "user" in session:
            print('이전에 로그인 했음!!')
            return redirect(url_for("home"))
        
    return render_template('login.html')


@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        action = request.form['action']
        if 'user' in session:
            username = session['user']
            if 'email' in session:
                email = session['email']
        
            if action == 'submit':
                email = request.form.get('email')
                password = request.form.get('password')

                if email:
                    session['email'] = email
                    query = "UPDATE users SET email = ? WHERE username = ?"
                    db.execute_query(query, (email, username))
                    # print('-----')

                if password:
                    query = "UPDATE users SET password = ? WHERE username = ?"
                    db.execute_query(query, (password, username))
                    # print(password)
                    
                flash('프로필 업데이트 완료')
                
                return render_template('user.html', email=email)


            elif action == 'delete':
                query = "DELETE FROM users WHERE username = ?"
                db.execute_query(query, (username,))
                session.pop('user', None)
                return redirect(url_for('login'))

    else:         
        # GET 요청일때는, 페이지를 보내줌
        return render_template('user.html')


@app.route('/view')
def view():
    users = db.get_query("SELECT * FROM users")       
    return render_template('view.html', users=users)


@app.route('/post')
def post():
    title = request.args.get('title')
    content = request.args.get('content')
    password = request.args.get('password')
    if not 'user' in session:
        flash('로그인을 해주세요')
    else:
        user = session['user']
        query = "INSERT INTO posts (username, title, content, password) VALUES (?,?,?,?)"
        db.execute_query(query, (user, title, content, password))
 
    return render_template('post.html')


@app.route('/post_update/<id>')
def post_update(id):
    password = request.args.get('password')
    content = request.args.get('content')
    post = db.get_query('SELECT * FROM posts WHERE id = ?', (id,))
    if request.args.get('action')=='update':
        print('update')
        if password == post[0]['password']:
            query = "UPDATE posts SET content = ? WHERE id = id and password = ?"
            db.execute_query(query, (content, id, password))
            print(1)
            return render_template('post_detail.html', post=post)
        else:
            flash('비밀번호가 틀렸습니다.')

    return render_template('post_update.html', post=post)


@app.route('/post_list')
def post_list():
    posts = db.get_query("SELECT * FROM posts")     
    return render_template('post_list.html', posts=posts)


@app.route('/post_detail/<id>')
def post_detail(id):
    post = db.get_query("SELECT * FROM posts WHERE id = ?", (id,))
    if request.args.get('btn') == "update":
        if 'user' in session:
            if session['user'] == post[0]['username']:
                return redirect(url_for('post_update', id=id))
            else:
                flash('수정 권한이 없습니다.')
        else:
            flash('수정 권한이 없습니다.')
    if request.args.get('btn') == "delete":
        if 'user' in session:
            if session['user'] == post[0]['username']:
                db.execute_query("DELETE FROM posts WHERE id = ?", (id,))
                return redirect(url_for('post_list'))
            else:
                flash('삭제 권한이 없습니다.')
        else:
            flash('삭제 권한이 없습니다.')
    return render_template('post_detail.html', post=post)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]

        query = "SELECT username FROM users WHERE username = ?"
        isUser = db.get_query(query, (username,))
        if isUser:
            flash('Username이 중복되었습니다. 다른 입력값을 넣어주세요')
        else:
            query = "INSERT INTO users (username, password, email) VALUES (?, ?, ?)"
            db.execute_query(query, (username, password, email))
            session['user'] = username
            return redirect(url_for('login'))
        
    return render_template('signup.html')


@app.route('/logout')
def logout():
    session.pop('user', None)      # 세션에 user가 존재하면 삭제하고 없으면 None을 반환
    session.pop('email', None)
    flash('로그아웃에 성공하였습니다.')           
    return redirect(url_for('login'))

if __name__=='__main__':
    db.init_db()   # 시스템 부팅(?)시에 DB 초기화 하기..
    app.run(debug=True)