import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

st.set_page_config(page_title="网页采集工具", layout="wide")
st.title("🌐 简易网页数据采集工具")

url = st.text_input("输入网页URL", "https://www.baidu.com")
if st.button("开始采集"):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=5)
        res.encoding = "utf-8"
        soup = BeautifulSoup(res.text, "html.parser")
        titles = [i.text.strip() for i in soup.find_all(["h1","h2","h3"])][:20]
        df = pd.DataFrame(titles, columns=["采集标题"])
        st.dataframe(df, use_container_width=True)
        csv = df.to_csv(index=False, encoding="utf-8-sig")
        st.download_button("导出CSV", csv, "采集结果.csv", "text/csv")
    except Exception as e:
        st.error(f"错误：{str(e)}")
