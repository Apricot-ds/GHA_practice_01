import streamlit as st

st.title("時刻読み取り")
st.write("now_time.txt から現在の日本時刻を読み取ります。")
with open("now_time.txt", "r", encoding="utf-8") as f:
    time_str = f.read()
st.write("現在の日本時刻:", time_str)