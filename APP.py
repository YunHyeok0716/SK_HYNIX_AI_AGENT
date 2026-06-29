import streamlit as st
import time
import random  # 랜덤 조합을 위한 라이브러리 추가

# 페이지 설정
st.set_page_config(page_title="Fit Me Up!", page_icon="👗", layout="wide")

# 세션 상태 초기화 (옷장 스캔 여부 확인용)
if "scanned" not in st.session_state:
    st.session_state.scanned = False

# 메인 화면 타이틀 및 설명
st.title("👗 Fit Me Up! (핏미업)")
st.caption("사용자의 옷장을 실시간 스캔하여 보유 아이템 기반 최고의 스타일을 추천하는 패션 AI 에이전트")
st.markdown("---")

# 레이아웃 구성 (좌측: 옷장 스캔 및 데이터 / 우측: 스타일 추천 에이전트)
col_left, col_right = st.columns([1, 2])

# ==========================================
# 데이터 원본 정의 (랜덤 추출 및 화면 표시용)
# ==========================================
tops = ["흰색 기본 셔츠", "오버핏 회색 맨투맨", "검은색 무지 티셔츠", "네이비 스트라이프 셔츠", "베이지 린넨 셔츠", "차콜 그래픽 후드티", "브라운 카라 니트", "반집업 니트 스웨터", "올리브그린 카디건", "흰색 롱슬리브 티"]
bottoms = ["와이드 크림진", "검은색 와이드 슬랙스", "진청 데님 팬츠", "연청 데님 팬츠", "카키 카고 팬츠", "그레이 트레이닝 조거팬츠", "베이지 치노 팬츠", "차콜 울 테이퍼드 슬랙스", "생지 데님 팬츠", "나일론 파라슈트 팬츠"]
shoes = ["미니멀 화이트 스니커즈", "클래식 검은색 더비 슈즈", "뉴발란스 그레이 러닝화", "독일군 스니커즈", "스웨이드 첼시 부츠", "반스 블랙 올드스쿨", "닥터마틴 3홀 로퍼", "살로몬 고어텍스 트레킹화", "메종 미하라 야스히로 스니커즈", "가죽 블로퍼"]
accs = ["레이어드 실버 목걸이", "검은색 무지 볼캡", "나일론 메신저 백", "가죽 스퀘어 숄더백", "클래식 메탈 시계", "빈티지 가죽 벨트", "카키 버킷햇", "은색 체인 팔찌", "뿔테 안경", "비니 (Beanie)"]

# ==========================================
# [왼쪽 영역] 옷장 스캔 및 보유 데이터 관리
# ==========================================
with col_left:
    st.header("📁 가상 옷장 시스템")
    
    # 1. 옷장 스캔 기능
    if not st.session_state.scanned:
        st.warning("⚠️ 스타일을 추천받기 전, 먼저 옷장을 스캔해주세요.")
        if st.button("📷 옷장/신발장/수납장 전체 스캔 시작", type="primary", use_container_width=True):
            with st.spinner("🔍 스마트 비전 AI가 옷장 안의 패션 아이템을 분석 중..."):
                time.sleep(2.0)  # 스캔 처리 애니메이션 효과
            st.session_state.scanned = True
            st.rerun()
    else:
        st.success("✅ 스마트 비전 스캔 완료 (데이터 동기화됨)")
        if st.button("🔄 옷장 다시 스캔하기", use_container_width=True):
            st.session_state.scanned = False
            st.rerun()
            
    st.markdown("---")
    st.subheader("📊 AI 인지 보유 아이템 (각 10종 이상)")
    
    if st.session_state.scanned:
        with st.expander("👔 상의 (Tops) - 10개", expanded=True):
            st.text("\n".join([f"• {item}" for item in tops]))
        with st.expander("👖 하의 (Bottoms) - 10개", expanded=True):
            st.text("\n".join([f"• {item}" for item in bottoms]))
        with st.expander("👟 신발 (Shoes) - 10개", expanded=False):
            st.text("\n".join([f"• {item}" for item in shoes]))
        with st.expander("🕶️ 액세서리 & 모자 (Accessories) - 10개", expanded=False):
            st.text("\n".join([f"• {item}" for item in accs]))
    else:
        st.info("옷장을 스캔하시면 AI가 분석한 보유 아이템 목록이 여기에 시각화됩니다.")

# ==========================================
# [오른쪽 영역] AI 스타일링 및 추천 로직
# ==========================================
with col_right:
    st.header("💡 AI 맞춤 스타일링 에이전트")
    
    # 2. 패션 스타일 선택
    selected_style = st.selectbox(
        "오늘 어떤 스타일의 패션을 원하시나요?",
        ["스타일을 선택하세요...", "미니멀 (Minimal)", "스트릿 (Street)", "캐주얼 (Casual)", "비즈니스 캐주얼 (Office)", "고프코어 (Gorpcore)"]
    )
    
    if selected_style != "스타일을 선택하세요..." and not st.session_state.scanned:
        st.error("🚨 왼쪽 메뉴에서 [옷장 전체 스캔]을 먼저 완료해야 취향 분석 및 아이템 조합이 가능합니다.")
        
    elif selected_style != "스타일을 선택하세요..." and st.session_state.scanned:
        st.markdown("---")
        with st.spinner(f"✨ 보유하신 데이터베이스를 기반으로 최적의 {selected_style} 룩을 매칭 중입니다..."):
            time.sleep(1.5)
            
        st.success(f"🎉 오늘 추천하는 최적의 **{selected_style}** 스타일 조합입니다!")
        
        res_col1, res_col2 = st.columns([3, 2])
        
        with res_col1:
            st.subheader("📋 오늘의 추천 OOTD 조합")
            
            # 스타일 버튼을 누를 때마다 무작위로 샘플링하여 유동적인 결과 도출
            if "미니멀" in selected_style:
                chosen_top = random.choice(["흰색 기본 셔츠", "베이지 린넨 셔츠", "브라운 카라 니트", "검은색 무지 티셔츠"])
                chosen_bottom = random.choice(["검은색 와이드 슬랙스", "차콜 울 테이퍼드 슬랙스", "와이드 크림진"])
                chosen_shoe = random.choice(["클래식 검은색 더비 슈즈", "가죽 블로퍼", "독일군 스니커즈"])
                chosen_acc = random.choice(["레이어드 실버 목걸이 + 가죽 스퀘어 숄더백", "클래식 메탈 시계 + 뿔테 안경"])
                
            elif "스트릿" in selected_style:
                chosen_top = random.choice(["차콜 그래픽 후드티", "오버핏 회색 맨투맨", "흰색 롱슬리브 티"])
                chosen_bottom = random.choice(["카키 카고 팬츠", "나일론 파라슈트 팬츠", "그레이 트레이닝 조거팬츠"])
                chosen_shoe = random.choice(["메종 미하라 야스히로 스니커즈", "반스 블랙 올드스쿨", "미니멀 화이트 스니커즈"])
                chosen_acc = random.choice(["검은색 무지 볼캡 + 나일론 메신저 백", "비니 (Beanie) + 은색 체인 팔찌"])
                
            elif "캐주얼" in selected_style:
                chosen_top = random.choice(["오버핏 회색 맨투맨", "검은색 무지 티셔츠", "베이지 린넨 셔츠", "흰색 롱슬리브 티"])
                chosen_bottom = random.choice(["진청 데늄 팬츠", "연청 데늄 팬츠", "생지 데늄 팬츠", "베이지 치노 팬츠"])
                chosen_shoe = random.choice(["독일군 스니커즈", "미니멀 화이트 스니커즈", "뉴발란스 그레이 러닝화"])
                chosen_acc = random.choice(["뿔테 안경 + 빈티지 가죽 벨트", "검은색 무지 볼캡 + 가죽 스퀘어 숄더백"])
                
            elif "비즈니스" in selected_style:
                chosen_top = random.choice(["네이비 스트라이프 셔츠", "흰색 기본 셔츠", "올리브그린 카디건"])
                chosen_bottom = random.choice(["베이지 치노 팬츠", "차콜 울 테이퍼드 슬랙스", "검은색 와이드 슬랙스"])
                chosen_shoe = random.choice(["가죽 블로퍼", "닥터마틴 3홀 로퍼", "클래식 검은색 더비 슈즈"])
                chosen_acc = random.choice(["클래식 메탈 시계", "빈티지 가죽 벨트 + 뿔테 안경"])
                
            elif "고프코어" in selected_style:
                chosen_top = random.choice(["반집업 니트 스웨터", "차콜 그래픽 후드티"])
                chosen_bottom = random.choice(["나일론 파라슈트 팬츠", "카키 카고 팬츠"])
                chosen_shoe = random.choice(["살로몬 고어텍스 트레킹화", "뉴발란스 그레이 러닝화"])
                chosen_acc = random.choice(["카키 버킷햇 + 나일론 메신저 백", "비니 (Beanie) + 나일론 메신저 백"])

            # 화면 출력
            st.info(f"**[상의]** {chosen_top}")
            st.info(f"**[하의]** {chosen_bottom}")
            st.info(f"**[신발]** {chosen_shoe}")
            st.info(f"**[액세서리]** {chosen_acc}")
            
            # 새로고침 유도 버튼
            if st.button("🔄 다른 조합 보기 (재추천)", use_container_width=True):
                st.rerun()

        with res_col2:
            st.subheader("🛒 AI 스마트 옷장 피드백")
            
            if "미니멀" in selected_style:
                st.warning("💡 **추가 구매 제안**\n\n1. **카멜색 미니멀 울 코트**: 가을/겨울 슬랙스 매칭 전천후 아이템\n2. **미니멀 레더 스퀘어 토 로퍼**: 더비 슈즈보다 조금 더 세련된 실루엣 연출 가능")
            elif "스트릿" in selected_style:
                st.warning("💡 **추가 구매 제안**\n\n1. **헤비웨이트 피그먼트 워싱 맨투맨**: 빈티지한 스트릿 무드 극대화\n2. **실버 볼 체인 지갑 체인**: 하의 벨트 고리에 걸어 확실한 스트릿 포인트 연출")
            elif "캐주얼" in selected_style:
                st.warning("💡 **추가 구매 제안**\n\n1. **네이비 오버핏 바시티 자켓**: 캠퍼스 룩 및 캐주얼 아우터의 정석\n2. **⚡ 크로스백 또는 토트백**: 가볍게 소지품을 넣기 좋은 매칭 유닛")
            elif "비즈니스" in selected_style:
                st.warning("💡 **추가 구매 제안**\n\n1. **네이비 싱글 브레스트 블레이저 자켓**: 치노 팬츠, 청바지 어디에나 비즈니스 무드 장착\n2. **브라운 시계 가죽 스트랩**: 가을/겨울철 따뜻하고 지적인 인상 부여")
            elif "고프코어" in selected_style:
                st.warning("💡 **추가 구매 제안**\n\n1. **바람막이 쉘 자켓 (고기능성)**: 고프코어 스타일링의 80%를 차지하는 필수 아우터\n2. **테크니컬 슬링백**: 유틸리티 감성을 더해주는 테크니컬 기어 소품")
