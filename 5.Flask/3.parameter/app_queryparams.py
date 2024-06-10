from flask import Flask, jsonify, request, json

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'phone': '123-123-1245'},
    {'name': 'Alice', 'age': 30, 'phone': '123-321-1234'},
    {'name': 'Bob', 'age': 30, 'phone': '234-234-2345'},
    {'name': 'Charlie', 'age': 35, 'phone': '555-555-5556'}
]

@app.route('/')
def home():
    return jsonify(users)

@app.route('/search')
def search():
    name_query = request.args.get('name')
    age_query = request.args.get('age')
    num_query = request.args.get('phone')
    result = users

    if name_query:
        result = [u for u in users if name_query.lower() in u['name'].lower()]    #리스트로 반환

    if age_query:
        try:
            age_query = int(age_query)
            result = [u for u in result if age_query == u['age']]
        except ValueError:
            # return jsonify({'error':'Age parameter must be an integer'}), 400
            return json.dumps({'error':'나이는 숫자로 입력해야 합니다.'}, ensure_ascii=False), 400  #한글 처리
    print(result)
    
    if num_query:
        try:
            num_query = num_query
            result = [u for u in result if num_query == u['phone'][-4:]]
        except ValueError:
            return jsonify({'error':'Phone parameter must be an integer'}), 400
        
    return jsonify(result), 200

    # print(type(u[0]['age']))
    # print(type(age_query))
    # v = [v for v in u if str(v['age']) == age_query]
    # result = []
    # if result:
    #     return jsonify(result), 200
    # else:
    #     return jsonify({'error': 'user not found'}), 404

if __name__=="__main__":
    app.run(debug=True)