from flask import Flask, render_template
# leaflet에서 필요한 html 코드를 대신 만들어 주는 라이브러리... wrapper 함수
import folium
from folium.plugins import MarkerCluster

app = Flask(__name__)

@app.route('/')
def index():
    # 커피샵 데이터 - 나중에는 DB에서 가져올 것 (GPS)

    coffee_shops = {
        'Gangnam': [
            {'name': 'Coffee Shop 1', 'latitude': 37.4979, 'longitude': 127.0276},
            {'name': 'Coffee Shop 2', 'latitude': 37.4969, 'longitude': 127.0306},
            {'name': 'Coffee Shop 3', 'latitude': 37.5002, 'longitude': 127.0278},
            {'name': 'Coffee Shop 4', 'latitude': 37.4985, 'longitude': 127.0287},
            {'name': 'Coffee Shop 5', 'latitude': 37.4993, 'longitude': 127.0293},
        ],
        'Seodaemun': [
            {'name': 'Coffee Shop 6', 'latitude': 37.5760, 'longitude': 126.9368},
            {'name': 'Coffee Shop 7', 'latitude': 37.5755, 'longitude': 126.9380},
            {'name': 'Coffee Shop 8', 'latitude': 37.5770, 'longitude': 126.9340},
            {'name': 'Coffee Shop 9', 'latitude': 37.5780, 'longitude': 126.9350},
        ],
        'Seongdong': [
            {'name': 'Coffee Shop 10', 'latitude': 37.5635, 'longitude': 127.0372},
            {'name': 'Coffee Shop 11', 'latitude': 37.5610, 'longitude': 127.0352},
            {'name': 'Coffee Shop 12', 'latitude': 37.5640, 'longitude': 127.0332},
        ]
    }

    # 서울의 중심으로 셋팅
    map_center = [37.5665, 126.9780]

    mymap = folium.Map(location=map_center, zoom_start=12)

    # 커피샵 갯수에 따라 다른 크기로 동그라미 그리기...
    # for area, shops in coffee_shops.items():
    #     latitudes = [shop['latitude'] for shop in shops]
    #     longitudes = [shop['longitude'] for shop in shops]
    #     avg_lat = sum(latitudes) / len(latitudes)
    #     avg_lng = sum(longitudes) / len(longitudes)

    #     folium.CircleMarker(
    #         location=[avg_lat, avg_lng],
    #         radius=10 * len(shops),
    #         color='red',
    #         fill=True,
    #         fill_color='pink',
    #         fill_opacity=0.6,
    #         popup=f"{area} (커피샵 수: {len(shops)}"
    #     ).add_to(mymap)


    # 클러스터 추가
    marker_cluster = MarkerCluster().add_to(mymap)
    for _, shops in coffee_shops.items():
        for shop in shops:
            folium.Marker(
                location=[shop['latitude'], shop['longitude']],
                popup=shop['name']
            ).add_to(marker_cluster)
   

    # # 마커 추가
    # for area, shops in coffee_shops.items():
    #     for shop in shops:
    #         folium.Marker(
    #             location=[shop['latitude'], shop['longitude']],
    #             popup=shop['name']
    #         ).add_to(mymap)

    # HTML 저장
    map_html = mymap._repr_html_()
    print(map_html)

    return render_template('index.html', map_html=map_html)


if __name__ == '__main__':
    app.run(debug=True)