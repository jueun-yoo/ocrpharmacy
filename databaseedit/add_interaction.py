import sqlite3


conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()


def add_interaction(contents, nutrient1_id, nutrient2_id):
    sql = "INSERT INTO supplements_interaction (contents, nutrient1_id, nutrient2_id) VALUES (?, ?, ?)"
    cursor.execute(sql, (contents, nutrient1_id, nutrient2_id))
    conn.commit()

# 비타민A와 스테로이드의 상호작용
add_interaction('[비타민A - 스테로이드] 같이 섭취 시 부작용: 비타민 A의 흡수와 대사에 영향을 줄 수 있음', "비타민A", "스테로이드")
# 비타민A와 프레드니솔론의 상호작용
add_interaction('[비타민A - 프레드니솔론] 같이 섭취 시 부작용: 칼슘흡수 방해, 비타민D 활성화 억제, 골밀도 감소 우려 영향을 줄 수 있음', "비타민A", "프레드니솔론")
# 비타민A와 베타카로틴의 상호작용
add_interaction('[비타민A - 베타카로틴] 같이 섭취 시 부작용: 지용성 비타민 흡수 억제 영향을 줄 수 있음', "비타민A", "베타카로틴")
# 비타민A와 제니칼의 상호작용
add_interaction('[비타민A - 제니칼] 같이 섭취 시 부작용: 비타민A 흡수 감소 영향을 줄 수 있음', "비타민A", "제니칼")
# 비타민A와 콜레스티라민의 상호작용
add_interaction('[비타민A - 콜레스티라민] 같이 섭취 시 부작용: 비타민D를 포함한 지용성 비타민 흡수 억제 영향을 줄 수 있음', "비타민A", "콜레스티라민")
# 비타민A와 페노바르비탈의 상호작용
add_interaction('[비타민A - 페노바르비탈] 같이 섭취 시 부작용: 비타민 분해 촉진 영향을 줄 수 있음', "비타민A", "페노바르비탈")
# 비타민A와 페니토인의 상호작용
add_interaction('[비타민A - 페니토인] 같이 섭취 시 부작용: 비타민 분해 촉진 영향을 줄 수 있음', "비타민A", "페니토인")
#비타민K와 비타민E의 상호작용
add_interaction('[비타민K - 비타민E] 같이 섭취 시 부작용: 서로 상충되어 영향을 미칠 수 있으므로 주의해야 함', "비타민K", "비타민E")
#비타민C와 철의 상호작용
add_interaction('[비타민C - 철] 같이 섭취 시 부작용: 서로 상충되어 영향을 미칠 수 있으므로 주의해야 함', "비타민C", "철")
#비타민B1과 푸로세미드의 상호작용
add_interaction('[비타민B1 - 푸로세미드] 같이 섭취 시 부작용: 비타민B1 배설 촉진 영향을 줄 수 있음', "비타민B1", "푸로세미드")
#비타민B1과 플루오로우라실의 상호작용
add_interaction('[비타민B1 - 플루오로우라실] 같이 섭취 시 부작용: 분해 및 활성형 방지 영향을 줄 수 있으므로 주의해야 함', "비타민B1", "플루오로우라실")
#비타민B6과 발프론산의 상호작용
add_interaction('[비타민B6 - 발프론산] 같이 섭취 시 부작용: 대사, 분해를 촉진하는 영향을 줄 수 있음', "비타민B6", "발프론산")
#비타민B6과 카바마제핀의 상호작용
add_interaction('[비타민B6 - 카바마제핀] 같이 섭취 시 부작용: 대사, 분해를 촉진하는 영향을 줄 수 있음', "비타민B6", "카바마제핀")
#비타민B6과 사이클로세린의 상호작용
add_interaction('[비타민B6 - 사이클로세린] 같이 섭취 시 부작용: 비타민B6의 배설을 촉진하는 영향을 줄 수 있음', "비타민B6", "사이클로세린")
#비타민B12과 클로람페니콜의 상호작용
add_interaction('[비타민B12 - 클로람페니콜] 같이 섭취 시 부작용: 비타민B12의 흡수를 방해하는 영향을 줄 수 있음', "비타민B12", "클로람페니콜")
#비타민B12과 메트포르민의 상호작용
add_interaction('[비타민B12 - 메트포르민] 같이 섭취 시 부작용: 비타민B12의 흡수를 방해하는 영향을 줄 수 있음', "비타민B12", "메트포르민")
#비타민C과 철의 상호작용
add_interaction('[비타민C - 철] 같이 섭취 시 부작용: 서로 상충되어 영향을 미칠 수 있으므로 주의해야 함', "비타민C", "철")
#아연과 철의 상호작용
add_interaction('[철 - 아연] 같이 섭취 시 부작용: 서로 상충되어 영향을 미칠 수 있으므로 주의해야 함', "철", "아연")
#아연과 구리의 상호작용
add_interaction('[아연 - 구리] 같이 섭취 시 부작용: 아연의 흡수 방해를 초래할 수 있음', "아연", "구리")
#클로렐라과 구리의 상호작용
add_interaction('[구리 - 클로렐라] 같이 섭취 시 부작용: 아미노산을 제재하여 단백질이 칼슘의 흡수를 방해함', "구리", "클로렐라")
#스피루리나과 구리의 상호작용
add_interaction( '[구리 - 스피루리나] 같이 섭취 시 부작용: 아미노산을 제재하여 단백질이 칼슘의 흡수를 방해함', "구리", "스피루리나")
# 연결 닫기 (중요)
conn.close()