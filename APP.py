import streamlit as st
import time

# 페이지 설정
st.set_page_config(page_title="Fit Me Up!", page_icon="👗", layout="wide")

# 사이드바 - 옷장 스캔 상태 및 데이터
st.sidebar.title("📁 내 가상 옷장 (Scan)")
st.sidebar.info("📷 옷장, 신발장 스캔 완료!")
st.sidebar.subheader("보유 아이템 리스트")
st.sidebar.text("👔 상의: 흰색 셔츠, 오버핏 맨투맨, 검은 티셔츠")
st.sidebar.text("👖 하의: 와이드 슬랙스, 청바지, 카고 팬츠")
st.sidebar.text("👟 신발: 화이트 스니커즈, 더비 슈즈, 러닝화")
st.sidebar.text("🕶️ 액세서리: 실버 목걸이, 검은색 볼캡")

# 메인 화면 타이틀
st.title("👗 Fit Me Up! (핏미업)")
st.caption("사용자의 옷장을 기반으로 최고의 스타일을 추천하는 패션 AI 에이전트")
st.markdown("---")

# 1. 에이전트 시작화면 (요구사항 입력)
st.subheader("💡 AI에게 패션 스타일 요구하기")
selected_style = st.selectbox(
    "오늘 어떤 스타일의 패션을 원하시나요?",
    ["스타일을 선택하세요...", "미니멀 (Minimal)", "스트릿 (Street)", "캐주얼 (Casual)"]
)

# 2. 실행 및 결과 화면 로직
if selected_style != "스타일을 선택하세요...":
    st.markdown("---")
    with st.spinner(f"✨ 사용자의 옷장을 스캔하여 {selected_style} 조합을 생성 중입니다..."):
        time.sleep(1.5)  # 에이전트가 생각하는 듯한 효과
    
    st.success(f"🎉 오늘 추천하는 최적의 **{selected_style}** 조합입니다!")
    
    # 레이아웃 나누기
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📋 오늘의 추천 OOTD 조합")
        
        if "미니멀" in selected_style:
            st.info("**[상의]** 흰색 셔츠 + **[하의]** 와이드 슬랙스")
            st.info("**[신발]** 깔끔한 더비 슈즈")
            st.info("**[액세서리]** 심플한 미니멀 실버 목걸이")
        elif "스트릿" in selected_style:
            st.info("**[상의]** 오버핏 맨투맨 + **[하의]** 카고 팬츠")
            st.info("**[신발]** 화이트 스니커즈")
            st.info("**[액세서리]** 검은색 볼캡")
        elif "캐주얼" in selected_style:
            st.info("**[상의]** 검은 티셔츠 + **[하의]** 청바지")
            st.info("**[신발]** 화이트 스니커즈 또는 러닝화")
            st.info("**[액세서리]** 포인트용 볼캡")

    with col2:
        st.subheader("🛒 AI 스마트 옷장 피드백")
        if "미니멀" in selected_style:
            st.warning("💡 **쇼핑 추천**\n\n현재 옷장에 미니멀 아이템이 70%를 차지하고 있습니다. 가지고 계신 슬랙스와 매치하기 좋은 **'검은색 로퍼'**를 추가하면 스타일 매력도가 더 높아집니다!")
        else:
            st.warning("💡 **스타일 팁**\n\n전체적으로 톤온톤 매치가 잘 어울리는 조합입니다. 외출 전 날씨를 확인하고 가벼운 아우터를 걸치셔도 좋습니다.")

