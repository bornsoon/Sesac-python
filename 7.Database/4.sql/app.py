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

        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        user_data = db.get_query(query, (username, password))
        print(f'조회된 사용자: ', user_data)
        print([dict(row) for row in user_data])

        if len(user_data) == 1:     #and user_data['password'] == password:
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
                    print('-----')

                if password:
                    query = "UPDATE users SET password = ? WHERE username = ?"
                    db.execute_query(query, (password, username))
                    print(password)
                    
                flash('프로필 업데이트 완료')
                
            elif action == 'delete':
                query = "DELETE FROM users WHERE username = ?"
                db.execute_query(query, (username, ""))
                
            return render_template('user.html', email=email)
    
    # GET 요청일때는, 페이지를 보내줌
    return render_template('user.html')

@app.route('/view')
def view():
    users = db.get_query("SELECT * FROM users")        
    return render_template('view.html', users=users)

@app.route('/signin')
def signin():
    users = []
    return render_template('signin.html', users=users)

@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('email', None)
    flash('로그아웃에 성공하였습니다.')           
    return redirect(url_for('login'))

if __name__=='__main__':
    db.init_db()   # 시스템 부팅(?)시에 DB 초기화 하기..
    app.run(debug=True)