
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")

st.set_page_config(
    page_title="人材定着支援ダッシュボード",
    page_icon="📊"
)

st.title("📊 人材定着支援ダッシュボード")

st.write("社員情報を入力すると離職リスクを予測します。")

age = st.slider("年齢", 18, 60, 30)

monthly_income = st.number_input(
    "月収",
    min_value=1000,
    value=300000
)

distance = st.number_input(
    "通勤距離(km)",
    min_value=0,
    value=5
)

years = st.number_input(
    "勤続年数",
    min_value=0,
    value=3
)

job_level = st.selectbox(
    "職位レベル",
    [1, 2, 3, 4, 5]
)

overtime = st.selectbox(
    "残業の有無",
    ["Yes", "No"]
)

if st.button("離職リスクを予測"):

    input_df = pd.DataFrame({
        "Age": [age],
        "MonthlyIncome": [monthly_income],
        "DistanceFromHome": [distance],
        "YearsAtCompany": [years],
        "JobLevel": [job_level],
        "OverTime": [overtime]
    })

    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)

    confidence = probability.max() * 100
