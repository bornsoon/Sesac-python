from flask import Flask ,render_template, request

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'phone': '123-123-1234'},
    {'name': 'Alice', 'age': 30, 'phone': '132-555-6789'},
    {'name': 'Bob', 'age': 30, 'phone': '234-234-2345'},
    {'name': 'Charlie', 'age': 35, 'phone': '555-555-5555'}
]

@app.route('/')
def main():
    return render_template('index.html', users=users)

@app.route('/user')
def get_user_by_name():
    search_name = request.args.get('name')
    search_age = request.args.get('age')
    # search_phone = request.args.get('phone')

    print(f"검색한이름:{search_name}, 검색한나이:{search_age}")
    # return 'OK'
    
    filtered_user = users

    if search_name:
        for u in users:
            filtered_user = [u for u in filtered_user if search_name.lower() in u['name'].lower()]

    if search_age:
        for u in users:
            filtered_user = [u for u in filtered_user if int(search_age) == u['age']]



    return render_template('index.html', users=filtered_user)

if __name__=="__main__":
    app.run(debug=True)

    