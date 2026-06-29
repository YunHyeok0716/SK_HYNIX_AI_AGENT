import streamlit as st
import time

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
    
    # 스캔이 완료되었을 때만 데이터 노출 (각 품목별 10개 이상 데이터)
    if st.session_state.scanned:
        with st.expander("👔 상의 (Tops) - 10개", expanded=True):
            st.text("• 흰색 기본 셔츠\n• 오버핏 회색 맨투맨\n• 검은색 무지 티셔츠\n• 네이비 스트라이프 셔츠\n• 베이지 린넨 셔츠\n• 차콜 그래픽 후드티\n• 브라운 카라 니트\n• 반집업 니트 스웨터\n• 올리브그린 카디건\n• 흰색 롱슬리브 티")
        with st.expander("👖 하의 (Bottoms) - 10개", expanded=True):
            st.text("• 와이드 크림진\n• 검은색 와이드 슬랙스\n• 진청 데님 팬츠\n• 연청 데님 팬츠\n• 카키 카고 팬츠\n• 그레이 트레이닝 조거팬츠\n• 베이지 치노 팬츠\n• 차콜 울 테이퍼드 슬랙스\n• 생지 데님 팬츠\n• 나일론 파라슈트 팬츠")
        with st.expander("👟 신발 (Shoes) - 10개", expanded=False):
            st.text("• 미니멀 화이트 스니커즈\n• 클래식 검은색 더비 슈즈\n• 뉴발란스 그레이 러닝화\n• 독일군 스니커즈\n• 스웨이드 첼시 부츠\n• 반스 블랙 올드스쿨\n• 닥터마틴 3홀 로퍼\n• 살로몬 고어텍스 트레킹화\n• 메종 미하라 야스히로 스니커즈\n• 가죽 블로퍼")
        with st.expander("🕶️ 액세서리 & 모자 (Accessories) - 10개", expanded=False):
            st.text("• 레이어드 실버 목걸이\n• 검은색 무지 볼캡\n• 나일론 메신저 백\n• 가죽 스퀘어 숄더백\n• 클래식 메탈 시계\n• 빈티지 가죽 벨트\n• 카키 버킷햇\n• 은색 체인 팔찌\n• 뿔테 안경\n• 비니 (Beanie)")
    else:
        st.info("옷장을 스캔하시면 AI가 분석한 보유 아이템 목록이 여기에 시각화됩니다.")

# ==========================================
# [오른쪽 영역] AI 스타일링 및 추천 로직
# ==========================================
with col_right:
    st.header("💡 AI 맞춤 스타일링 에이전트")
    
    # 2. 패션 스타일 선택 (5가지 스타일로 확장)
    selected_style = st.selectbox(
        "오늘 어떤 스타일의 패션을 원하시나요?",
        ["스타일을 선택하세요...", "미니멀 (Minimal)", "스트릿 (Street)", "캐주얼 (Casual)", "비즈니스 캐주얼 (Ameiswank / Office)", "고프코어 (Gorpcore)"]
    )
    
    # 스캔 안 하고 스타일 먼저 고른 경우 방어 코드
    if selected_style != "스타일을 선택하세요..." and not st.session_state.scanned:
        st.error("🚨 왼쪽 메뉴에서 [옷장 전체 스캔]을 먼저 완료해야 취향 분석 및 아이템 조합이 가능합니다.")
        
    # 조건 만족 시 조합 결과 출력
    elif selected_style != "스타일을 선택하세요..." and st.session_state.scanned:
        st.markdown("---")
        with st.spinner(f"✨ 보유하신 데이터베이스를 기반으로 최적의 {selected_style} 룩을 매칭 중입니다..."):
            time.sleep(1.5)
            
        st.success(f"🎉 오늘 추천하는 최적의 **{selected_style}** 스타일 조합입니다!")
        
        # 상세 결과화면 레이아웃 나누기
        res_col1, res_col2 = st.columns([3, 2])
        
        with res_col1:
            st.subheader("📋 오늘의 추천 OOTD 조합")
            
            if "미니멀" in selected_style:
                st.info("**[상의]** 흰색 기본 셔츠 + 브라운 카라 니트 (레이어드)")
                st.info("**[하의]** 검은색 와이드 슬랙스")
                st.info("**[신발]** 클래식 검은색 더비 슈즈")
                st.info("**[액세서리]** 레이어드 실버 목걸이 + 가죽 스퀘어 숄더백")
            elif "스트릿" in selected_style:
                st.info("**[상의]** 차콜 그래픽 후드티")
                st.info("**[하의]** 나일론 파라슈트 팬츠 또는 카키 카고 팬츠")
                st.info("**[신발]** 메종 미하라 야스히로 스니커즈")
                st.info("**[액세서리]** 검은색 무지 볼캡 + 나일론 메신저 백")
            elif "캐주얼" in selected_style:
                st.info("**[상의]** 오버핏 회색 맨투맨 + 흰색 롱슬리브 티 (레이어드 타이트)")
                st.info("**[하의]** 연청 데님 팬츠")
                st.info("**[신발]** 독일군 스니커즈 또는 반스 블랙 올드스쿨")
                st.info("**[액세서리]** 뿔테 안경 + 빈티지 가죽 벨트")
            elif "비즈니스" in selected_style:
                st.info("**[상의]** 네이비 스트라이프 셔츠 + 올리브그린 카디건")
                st.info("**[하의]** 베이지 치노 팬츠 또는 차콜 울 테이퍼드 슬랙스")
                st.info("**[신발]** 가죽 블로퍼 또는 닥터마틴 3홀 로퍼")
                st.info("**[액세서리]** 클래식 메탈 시계")
            elif "고프코어" in selected_style:
                st.info("**[상의]** 반집업 니트 스웨터 (이너로 흰색 무지 티셔츠)")
                st.info("**[하의]** 나일론 파라슈트 팬츠")
                st.info("**[신발]** 살로몬 고어텍스 트레킹화")
                st.info("**[액세서리]** 카키 버킷햇 + 나일론 메신저 백")

        with res_col2:
            st.subheader("🛒 AI 스마트 옷장 피드백")
            
            if "미니멀" in selected_style:
                st.warning("💡 **스타일 매력도 업그레이드를 위한 추가 구매 제안**\n\n현재 옷장에 미니멀 감성의 깔끔한 아이템이 대다수 배치되어 있습니다. 여기에 다음 아이템을 추가하면 조합력이 200% 증가합니다.\n\n1. **카멜색 미니멀 울 코트**: 가을/겨울 슬랙스 매칭 전천후 아이템\n2. **미니멀 레더 스퀘어 토 로퍼**: 더비 슈즈보다 조금 더 세련된 실루엣 연출 가능")
            elif "스트릿" in selected_style:
                st.warning("💡 **스타일 매력도 업그레이드를 위한 추가 구매 제안**\n\n트렌디한 하이프(Hype) 스트릿 무드를 내기에 좋은 하의 위주로 구성되어 있습니다. 상의의 포인트를 늘리기 위해 다음 아이템을 제안합니다.\n\n1. **헤비웨이트 피그먼트 워싱 맨투맨**: 빈티지한 스트릿 무드 극대화\n2. **실버 볼 체인 지갑 체인**: 하의 벨트 고리에 걸어 확실한 스트릿 포인트 연출")
            elif "캐주얼" in selected_style:
                st.warning("💡 **스타일 매력도 업그레이드를 위한 추가 구매 제안**\n\n대중적이고 깔끔한 데일리 아이템들이 아주 훌륭하게 갖춰져 있습니다. 꾸안꾸 느낌의 포인트를 주기 위해 다음 아이템을 추천합니다.\n\n1. **네이비 오버핏 바시티 자켓**: 캠퍼스 룩 및 캐주얼 아우터의 정석\n2. **캔버스 가방 (토트백)**: 가볍게 전공 서적이나 소지품을 넣기 좋은 매칭 유닛")
            elif "비즈니스" in selected_style:
                st.warning("💡 **스타일 매력도 업그레이드를 위한 추가 구매 제안**\n\n단정하면서도 위트 있는 오피스룩 연출이 가능한 상태입니다. 룩의 무게감과 완성도를 잡기 위해 다음 꿀조합 템을 추천합니다.\n\n1. **네이비 싱글 브레스트 블레이저 자켓**: 치노 팬츠, 청바지 어디에나 비즈니스 무드 장착\n2. **브라운 시계 가죽 스트랩**: 메탈 시계 대신 가을/겨울철 따뜻하고 지적인 인상 부여")
            elif "고프코어" in selected_style:
                st.warning("💡 **스타일 매력도 업그레이드를 위한 추가 구매 제안**\n\n기능성과 힙함을 두루 갖춘 테크웨어 믹스매치가 돋보입니다. 완전한 고프코어 룩 완성을 위해 아우터와 소품을 보강해 보세요.\n\n1. **바람막이 쉘 자켓 (아크테릭스 스타일)**: 고프코어 스타일링의 80%를 차지하는 필수 아우터\n2. **테크니컬 슬링백 (전면 지퍼 포인트)**: 유틸리티 감성을 더해주는 테크니컬 기어 소품")
