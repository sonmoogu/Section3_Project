# 서울시 스타벅스 매장 옆에는 이디야 매장이 반드시 있다는 가정에 관한 검정 프로젝트

---

이디야커피는 가끔 스타벅스 커피 매장이 위치하는 곳에 매장을 위치시키는 것이 아니냐는 의심을 받곤 합니다.
공식적인 인터뷰에서 이디야커피 회장은 이 사실을 부인했습니다.
이 사실을 확인해 보려합니다.

---

위도와 경도를 클러스터링을 통해 가까운 거리끼리 계산을 하여 할 수도 있지만 다소 어려움이 있어 시각화를 통해 확인을 해보았다. 
folium에 각 커피숍마다 Circle을 그려 서로 다른 커피숍이 얼마나 겹쳐있는지 주변에 존재하는 지 확인을 해보았다.

---

## **확인 결과**
- 스타벅스보다 이디야커피가 서울에 매장이 더 많은 것을 알 수 있다. 하지만 스타벅스가 있는 곳 주변에 이디야가 없는 곳은 없다.
대체로 스타벅스 매장 근처에 위하는 것이 전략적이라고 볼 수 있다 하지만 다른 면에서는 아니라고 볼 수 있다.

- 이디야 커피는 스타벅스보다 전체적으로 서울 전반적으로 퍼져있는 느낌이라면 스타벅스는 퍼져있기 보다 특정지역에 많이 몰려 있다는 것을 확인 할 수 있었다. 그렇다고 해서 스타벅스 주변에 이디야가 있다라는 것에 상관성을 말하기에는 어려운 부분이 있다. 
그러나 스타벅스 주변에 오히려 스타벅스가 있고 오히려 스타벅스가 없는 곳에 이디야가 있는 곳이 더 많다.
예를 들어 스타벅스가 몰려있는 몇군데를 뽑자면 강남, 종로구, 가산쪽에 몰려있는 것을 볼 수 있다. 이곳에 특징으로는 유동인구가 많고 대체적으로 회사가 많이 몰려있다는 것을 알 수 있습니다.
예시를 확인 해볼 때 스타벅스는 유동인구가 많고 점심시간이나 저녁시간에 사람들이 쉽게 찾아 올 수 있는 곳에 배치 되어있다는 특성이 있다. 
그러하기 때문에 스타벅스 매장 근처에 위하는 것이 전략적이라고 볼 수 있다.
스타벅스가 위치한 곳 자체가 잠재적 고객들이 많이 다니는 곳이고 스타벅스에 자리가 없을 때 대체로 가야 할 커피숍이 필요 할 것이다. 그러할 때 가까운 곳에 다른 커피숍이 있다면 고객을 유치하는 데 좀 더 수월 할 것이기 때문에 스타벅스 근처에 매장을 배치하는 것이 전략적이라고 볼 수 있다.

- 한편으로는 사람들은 스타벅스라는 브랜드 때문에 스타벅스를 가는 사람도 많고 테이크 아웃하는 사람들 또한 많기 때문에 전략적이지 않다고도 볼 수 있다. 스타벅스만의 메뉴를 찾는 사람도 있고 브랜드 평판이 있어 가는 사람이 있기 때문에 스타벅스가 자리가 없고 주문이 많더라도 다른 카페를 찾아 가지 않을 수도 있다. 

- 하지만 folium의 분포도를 보았을 때 스타벅스의 위치는 사람이 많이 다니는 곳이기 때문에 전략적이라고 볼 수 있다. 


- 좀 더 명확한 분석 결과를 가지고 오기 위해서는 지역의 특성, 테이크 아웃 고객이 많은지, 매장에서 먹고가는 고객이 많은지, 유동인구 등 여러가지 요소를 고려할 수 있다면 조금 더 유의미하게 결과를 이야기할 수 있을 것 같아 아쉽다.

--- 

## **지도 시각화 확인법**

""" python

git clone -> flask_app 폴더로 들어가기 (./flask_app) -> Visual Studio Code에서 python __init__.py CLI로 실행!

"""
