import random
import uuid
import csv

firstname = [ "구", "강", "견", "곽", "권", "고", "길", "김", "나", "노", "남궁", "도", "라", "류",\
              "마", "맹", "모", "문", "민", "박", "반", "방", "배", "봉" \
              "성", "신", "서", "선", "소", "선우", "손", "송", "설", "심", \
              "이", "윤", "오", "우", "임", "원", "양", "여", "연", "염", "옥", "온", "용", "육", \
              "장", "전", "정", "점", "조", "주", "지", "진", "차", "채", "천", "최", "춘", \
              "탁", "팽", "표", "하", "한", "함", "허", "현", "홍", "황", "황보"]
lastname = [ "민준", "서준", "도윤", "예준", "시우", "하준", "지호", "주원", "지후", "준우", "도현", "준서", "건우", \
             "현우", "우진", "지훈", "선우", "유준", "연우", "은우", "서진", "민재", "현준", "시윤", "정우", "주한", \
             "환희", "하루", "승혁", "승헌", "준민", "성재", "민", "도운", "동연", "라율", "인서", "결", "한솔", "다솔" \
             "유진", "재희", "세영", "세희", "은설", "윤진", "여원", "여진", "도경", "유안", "한나", "은재", "연재", \
             "도은", "시우", "세빈", "보미", "유이", "예담", "정민", "효린", "예인", "채빈", "세인", "은빈", "은비", \
             "재희", "정연", "하온", "연지", "준희", "효은", "가인", "가을", "아름", "혜민", "채율", "혜진", "단비" ]
cities = [ "서울", "춘천", "광주", "남양주", "양주", "고양", "하남", "부산", "광주", "수원", "오산", "대구", "창원" \
           "인천", "양평", "가평", "평택", "시흥", "화성", "성남", "파주", "김포", "용인", "과천", "전주", "천안" ]
way = [ "중구", "북구", "강남구", "강서구", "강북구", "강동구", "중남구", "성북구", "서구", "동구", "남구", "북구", "도봉구" \
        "서북구", "은평구", "중랑구", "종로구", "동남구", "노원구", "양천구", "광산구"]
    


def create_users():

    num = int(input("생성하고 싶은 사용자 갯수: "))
    users = []

    for _ in range(num):
        id = str(uuid.uuid4())
        name = random.choice(firstname) + random.choice(lastname)
        year = random.randint(1950, 2010)
        month = random.randint(1,12)
        day = random.randint(1,28)
        birthdate = f"{year}-{month:02d}-{day:02d}"
        age = 2024 - year
        gender = random.choice(["Male", "Female"])
        address = random.choice(cities) + ' ' + random.choice(way) + ' ' + str(random.randint(1,99)) + "길 " + str(random.randint(1,99))

        r_user = ( id, name, gender, age, birthdate, address )
        users.append(r_user)

    return users


users = create_users()


with open('users.txt', 'w', encoding = 'utf-8') as file:
    writer = csv.writer(file)
    for l in users:
        writer.writerow(l)
