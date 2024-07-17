import requests

# 외부에 요청...
# 니가 가지고 있는 정보 좀 주시오...
user_id = 1
url = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"

response = requests.get(url)

post_data = response.json()
for comment in post_data:
    print(comment['title'])

# 2. 게시글 ID를 기준으로... 댓글 가져오기...
post_id = 1
url = f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments"

response = requests.get(url)
post_data = response.json()
for comment in post_data:
    print(comment['email'])