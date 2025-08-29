# 1회차: Streamlit 기초 및 환경 구축
# 파일명: session1_basic.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 페이지 설정
st.set_page_config(
    page_title="Streamlit 기초 학습",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 메인 타이틀
st.title("🚀 내 첫 Streamlit 앱")
st.markdown("---")

# 1. 텍스트 요소들
st.header("1️⃣ 텍스트 요소들")
st.subheader("다양한 텍스트 표시 방법")

st.text("이것은 일반 텍스트입니다.")
st.markdown("**굵은 글씨**와 *기울임 글씨*를 사용할 수 있습니다.")
st.markdown("> 이것은 인용문입니다.")

st.code("""
# 파이썬 코드 예시
def hello_streamlit():
    return "Hello, Streamlit!"
    
print(hello_streamlit())
""", language='python')

st.latex(r'''
a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
\sum_{k=0}^{n-1} ar^k =
a \left(\frac{1-r^{n}}{1-r}\right)
''')

st.markdown("---")

# 2. 샘플 데이터 생성 및 표시
st.header("2️⃣ 데이터 표시")

# 샘플 데이터 생성
@st.cache_data
def create_sample_data():
    np.random.seed(42)
    data = {
        '이름': ['김철수', '이영희', '박민수', '최수진', '정대만'],
        '나이': np.random.randint(20, 60, 5),
        '점수': np.random.randint(60, 100, 5),
        '부서': ['개발팀', '마케팅팀', '영업팀', '개발팀', '마케팅팀'],
        '급여': np.random.randint(3000, 8000, 5) * 10000
    }
    return pd.DataFrame(data)

df = create_sample_data()

col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 데이터프레임")
    st.dataframe(df, use_container_width=True)

with col2:
    st.subheader("📊 정적 테이블")
    st.table(df.head(3))

# JSON 데이터 표시
st.subheader("📄 JSON 형태")
sample_json = {
    "총 직원 수": len(df),
    "평균 나이": float(df['나이'].mean()),
    "최고 점수": int(df['점수'].max()),
    "부서별 인원": df['부서'].value_counts().to_dict()
}
st.json(sample_json)

st.markdown("---")

# 3. 기본 차트들
st.header("3️⃣ 기본 차트")

# 시계열 데이터 생성
chart_data = pd.DataFrame({
    '일자': pd.date_range('2024-01-01', periods=30, freq='D'),
    '매출': np.random.randn(30).cumsum() + 100,
    '방문자': np.random.randn(30).cumsum() + 50,
    '전환율': np.random.randn(30).cumsum() + 10
})

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("📈 라인 차트")
    st.line_chart(chart_data.set_index('일자')[['매출', '방문자']])
    
    st.subheader("📊 바 차트")
    st.bar_chart(df.set_index('이름')['점수'])

with chart_col2:
    st.subheader("📊 영역 차트")
    st.area_chart(chart_data.set_index('일자')['전환율'])
    
    st.subheader("🎯 메트릭")
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    with metric_col1:
        st.metric("총 매출", "₩1,234,567", "12%")
    with metric_col2:
        st.metric("방문자", "5,678", "-2%")
    with metric_col3:
        st.metric("전환율", "3.2%", "0.5%")

st.markdown("---")

# 4. Matplotlib/Seaborn 차트
st.header("4️⃣ Matplotlib & Seaborn 차트")

fig_col1, fig_col2 = st.columns(2)

with fig_col1:
    st.subheader("Matplotlib 히스토그램")
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(df['점수'], bins=10, alpha=0.7, color='skyblue', edgecolor='black')
    ax.set_xlabel('점수')
    ax.set_ylabel('빈도')
    ax.set_title('점수 분포')
    st.pyplot(fig)

with fig_col2:
    st.subheader("Seaborn 박스플롯")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(data=df, x='부서', y='급여', ax=ax)
    plt.xticks(rotation=45)
    plt.title('부서별 급여 분포')
    st.pyplot(fig)

st.markdown("---")

# 5. 사이드바
st.sidebar.title("🎛️ 사이드바")
st.sidebar.markdown("여기는 사이드바입니다!")

sidebar_option = st.sidebar.selectbox(
    "옵션을 선택하세요:",
    ["옵션 1", "옵션 2", "옵션 3"]
)

st.sidebar.write(f"선택된 옵션: {sidebar_option}")

# 사이드바에 차트 추가
st.sidebar.subheader("📊 사이드바 차트")
sidebar_data = df['부서'].value_counts()
st.sidebar.bar_chart(sidebar_data)

# 6. 알림 메시지
st.header("5️⃣ 알림 메시지")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("성공 메시지"):
        st.success("성공적으로 처리되었습니다! ✅")

with col2:
    if st.button("정보 메시지"):
        st.info("추가 정보입니다. ℹ️")

with col3:
    if st.button("경고 메시지"):
        st.warning("주의가 필요합니다! ⚠️")

with col4:
    if st.button("에러 메시지"):
        st.error("오류가 발생했습니다! ❌")

# 7. 데이터 통계 정보
st.markdown("---")
st.header("6️⃣ 데이터 분석 정보")

with st.expander("📊 상세 통계 정보"):
    st.write("**기본 통계:**")
    st.write(df.describe())
    
    st.write("**결측값 정보:**")
    st.write(df.isnull().sum())
    
    st.write("**데이터 타입:**")
    st.write(df.dtypes)

# 푸터
st.markdown("---")
