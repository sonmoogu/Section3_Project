import googlemaps
gmaps_key = "AIzaSyALa3WC7ilIbtTRPk5jMXc4YY_sin-8NpI"
gmaps = googlemaps.Client(key = gmaps_key)

import json
import folium
import pandas as pd

seoul_Ediya = pd.read_csv("seoul_Ediya_df.csv",sep=",", index_col=0 ,encoding = "utf-8-sig")
seoul_starbucks =pd.read_csv("seoul_starbucks_df.csv",sep=",", index_col=0 ,encoding = "utf-8-sig")

geo_path = "./02. skorea_municipalities_geo_simple.json"
geo_str = json.load(open(geo_path, encoding="utf-8"))

my_map = folium.Map(location=[37.51109538400115, 126.9812696025245],zoom_start= 13)

for idx, rows in seoul_Ediya.iterrows():
    folium.Marker([rows["위도"],rows["경도"]],
                 popup = rows["주소"], # 캡션같은 것 # <b> : 볼드체
                 tooltip = rows["매장명"],
                 icon = folium.Icon(
                                    color = "white",
                                    icon_color = "blue",
                                    icon = "coffee",
                                    angle = 0, # 아이콘 각도 조절
                                    prefix = "fa" # prefix : 특정 아이콘 들은 설정을 해주어야한다.
                                                  # 독스트링 확인하면서 해야한다.
                                                  # "glyphicon" or "fa"
                                     )).add_to(my_map)
    
for idx, rows in seoul_starbucks.iterrows():
    folium.Marker([rows["위도"],rows["경도"]],
                 popup = rows["주소"],
                 tooltip = rows["매장명"],
                 icon = folium.Icon(
                                    color = "green",
                                    icon_color = "white",
                                    icon = "coffee",
                                    angle = 0, # 아이콘 각도 조절
                                    prefix = "fa" # prefix : 특정 아이콘 들은 설정을 해주어야한다.
                                                  # 독스트링 확인하면서 해야한다.
                                                  # "glyphicon" or "fa"
                                     )).add_to(my_map)

for idx, rows in seoul_Ediya.iterrows():
    folium.CircleMarker(
                        location =[rows["위도"],rows["경도"]],
                        radius = 40,
                        fill = True, # 옅은 색으로 칠해짐
                        color = "#1864ab",
                        fill_color = "blue",
                    ).add_to(my_map)
    
for idx, rows in seoul_starbucks.iterrows():
    folium.CircleMarker(
                        location =[rows["위도"],rows["경도"]],
                        radius = 40,
                        fill = True, # 옅은 색으로 칠해짐
                        color = "#2b8a3e",
                        fill_color = "green",
                    ).add_to(my_map)

my_map