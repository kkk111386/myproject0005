import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 경로 지정
FILE_PATH = "jadongcadeungroghyeonhwangbogo_jadongcadeungrogdaesuhyeonhwang_yeondobyeol-1990-2024.csv"

# 데이터 불러오기
df = pd.read_csv(FILE_PATH, header=[0, 1])

# 연도 추출
years = df.index if '년(Annual)' not in df.columns else df['년(Annual)']

# 승용, 승합, 화물, 특수, 총계 별 합계 컬럼만 추출 (계)
category = ['승용', '승합', '화물', '특수', '총계']
usage_type = '계'
columns = [(cat, usage_type) for cat in category]

# '년(Annual)' 컬럼이 인덱스가 아니라면 연도 인덱스로 설정
data = df[columns]
if '년(Annual)' in df.columns:
    data['연도'] = df['년(Annual)']
    data = data.set_index('연도')

# Streamlit 앱
st.title("자동차 등록 현황 (1990~2024)")

# 라인 차트
st.line_chart(data)

# 바 차트 옵션 제공
if st.checkbox("막대 그래프 보기"):
    st.bar_chart(data)
