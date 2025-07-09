
import streamlit as st
import pandas as pd

# ダミーデータ（本来はCSVなどから読み込み）
data = {'店舗': ['新宿', '渋谷', '横浜', '梅田', '名古屋', '札幌'], '売上': [1050000, 950000, 870000, 990000, 910000, 800000], '在庫数': [500, 450, 400, 470, 430, 380], 'CVR': [0.032, 0.028, 0.03, 0.034, 0.029, 0.027], '死に筋SKU数': [12, 15, 10, 9, 13, 17]}
df = pd.DataFrame(data)

st.title("アパレル店舗別 業務ダッシュボード")

# 売上グラフ
st.subheader("店舗別 売上")
st.bar_chart(df.set_index("店舗")["売上"])

# 在庫数グラフ
st.subheader("店舗別 在庫数")
st.bar_chart(df.set_index("店舗")["在庫数"])

# CVR表示
st.subheader("CVR（Conversion Rate）")
st.dataframe(df[["店舗", "CVR"]].sort_values(by="CVR", ascending=False))

# 死に筋商品警告
st.subheader("死に筋SKU数（15以上は要注意）")
st.dataframe(df[df["死に筋SKU数"] >= 15])
