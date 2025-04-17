import streamlit as st
import folium
from streamlit_folium import st_folium

# 관광지 설명 및 툴팁 정보는 생략된 상태로 이미 city_attractions, city_coordinates 정의됨

# 툴팁 정보 (도시별 간단한 팁 + 이모지 포함)
city_tooltips = {
    '도쿄': "🎁 기념품 핫플! 나카미세 거리에서 잊지 말고 쇼핑하세요!",
    '오사카': "🍢 타코야키 맛집 천국! 도톤보리에서 먹방 투어 추천!",
    '교토': "⛩️ 일본 전통 감성 100%! 기온 거리 산책은 꼭 해보세요~",
    '히로시마': "🕊️ 평화의 메시지를 느낄 수 있는 도시, 공원 산책 강추!",
    '삿포로': "❄️ 겨울왕국 같은 눈 축제! 오도리 공원은 포토 스팟!",
    '후쿠오카': "🍜 하카타 라멘! 후쿠오카는 진짜 라멘 천국이에요!",
    '나고야': "🏯 성덕이라면 나고야성은 필수 방문지예요!",
    '하코다테': "🌅 야경 맛집! 하코다테산 전망은 꼭 봐야 해요!",
    '카나자와': "🎨 예술과 전통이 살아있는 도시! 21세기 미술관 추천!",
    '오카야마': "🌸 정원 덕후라면 여긴 천국! 코이시카케 정원 강추!",
    '센다이': "🌲 초록초록한 자연 가득! 가족 나들이에 최고예요~",
    '도쿠시마': "🌊 자연 경관이 예쁜 힐링 도시! 조용히 쉬고 싶을 땐 여기!",
    '고베': "🥩 고베비프 안 먹으면 서운해요~ 항구 산책도 추천!",
    '미야자키': "🌴 열대기후와 해변🌞 여름휴가엔 미야자키~",
    '나가사키': "🎆 낭만항구! 히스토리와 야경 모두 잡자!",
    '시오노미사키': "🌅 일본 최남단의 일출 맛집! 등대 뷰는 환상적이에요!",
    '니가타': "🍚 일본 최고 쌀의 고장! 니가타 사케도 놓치지 마세요!",
    '구마모토': "🏯 구마모토성에서 시간여행을 떠나보세요!",
    '이바라키': "🧪 이바라키 수족관은 아이들과 함께하기 좋은 명소예요!",
    '오키나와': "🏖️ 바다, 산호, 슈리성! 남국의 낭만을 즐기세요~",
}

def main():
    st.title("🗾 일본 도시 관광지 지도 🧭")

    # 도시 선택 상자
    city = st.selectbox("🎌 가고 싶은 도시를 선택하세요:", list(city_attractions.keys()))

    # 선택된 도시 정보 표시
    st.markdown(f"## ✨ 당신이 선택한 도시: **{city}**")
    st.write(city_attractions[city])

    # 지도 생성 (일본 중심으로 확대)
    m = folium.Map(location=[36.2048, 138.2529], zoom_start=5)

    # 모든 도시 마커 추가
    for city_name, coord in city_coordinates.items():
        tooltip = city_tooltips.get(city_name, "🎒 즐거운 여행 되세요!")
        folium.Marker(
            location=coord,
            popup=folium.Popup(f"<b>{city_name}</b><br>{tooltip}", max_width=250),
            tooltip=tooltip,
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(m)

    # 지도 출력
    st_folium(m, width=700, height=500)

# 실행
if __name__ == "__main__":
    main()
