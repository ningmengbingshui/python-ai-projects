import streamlit as st
import pandas as pd

st.set_page_config(page_title="数据清洗工具", layout="wide")
st.title("📊 Excel自动化数据清洗工具")

uploaded = st.file_uploader("上传CSV/Excel文件", type=["csv", "xlsx"])

if uploaded:
    if uploaded.name.endswith("csv"):
        df = pd.read_csv(uploaded)
    else:
        df = pd.read_excel(uploaded)

    st.subheader("原始数据")
    st.dataframe(df, use_container_width=True)

    df_clean = df.dropna().drop_duplicates()
    st.subheader(f"清洗后数据（{df_clean.shape[0]}行）")
    st.dataframe(df_clean, use_container_width=True)

    csv = df_clean.to_csv(index=False, encoding="utf-8-sig")
    st.download_button("下载清洗结果", csv, "清洗完成.csv", "text/csv")
