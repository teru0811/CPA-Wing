import streamlit as st
import os
from datetime import date

# --- 1. カウントダウン設定 ---
EXAM_DATE = date(2026, 5, 31)
days_left = (EXAM_DATE - date.today()).days

# --- 2. スタイル設定（もっとカラフル・ネオン） ---
st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%);
        color: white;
    }}
    .stTabs [data-baseweb="tab-list"] {{
        gap: 10px;
        background-color: rgba(255,255,255,0.1);
        border-radius: 10px;
        padding: 5px;
    }}
    .stTabs [data-baseweb="tab"] {{
        color: white !important;
        font-weight: bold;
    }}
    .count-box {{
        background: rgba(255, 255, 255, 0.2);
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.3);
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. データ保存・読込（2科目対応） ---
SAVE_FILE = "study_data_v3.txt"
def load_all_data():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            d = f.read().split(',')
            return int(d[0]), int(d[1])
    return 39, 15  # 初期値：財務39回、管理15回

def save_all_data(z_count, k_count):
    with open(SAVE_FILE, "w") as f:
        f.write(f"{z_count},{k_count}")

if 'z_count' not in st.session_state:
    st.session_state.z_count, st.session_state.k_count = load_all_data()

# --- 4. メイン表示 ---
st.title("🌈 CPA Victory Log")

# カウントダウン
st.markdown(f'<div class="count-box"><h2>🏁 5/31まで あと {days_left} 日</h2></div>', unsafe_allow_html=True)

# 科目切り替えタブ
tab1, tab2 = st.tabs(["📊 財務会計論", "📉 管理会計論"])

# --- 財務会計 ---
with tab1:
    z_total = 70
    z_per = st.session_state.z_count / z_total
    st.header(f"{st.session_state.z_count} / {z_total}")
    st.progress(z_per)
    st.write(f"あと **{z_total - st.session_state.z_count}** 回！")
    if st.button("✨ 財務を1コマ撃破！"):
        st.session_state.z_count += 1
        save_all_data(st.session_state.z_count, st.session_state.k_count)
        st.balloons()
        st.rerun()

# --- 管理会計 ---
with tab2:
    k_total = 33
    k_per = st.session_state.k_count / k_total
    st.header(f"{st.session_state.k_count} / {k_total}")
    st.progress(k_per)
    st.write(f"あと **{k_total - st.session_state.k_count}** 回！")
    if st.button("🔥 管理を1コマ撃破！"):
        st.session_state.k_count += 1
        save_all_data(st.session_state.z_count, st.session_state.k_count)
        st.balloons()
        st.rerun()

# --- 5. サイドバー（修正用） ---
st.sidebar.header("修正ボタン")
if st.sidebar.button("財務を1つ戻す"):
    st.session_state.z_count -= 1
    save_all_data(st.session_state.z_count, st.session_state.k_count)
    st.rerun()
if st.sidebar.button("管理を1つ戻す"):
    st.session_state.k_count -= 1
    save_all_data(st.session_state.z_count, st.session_state.k_count)
    st.rerun()
