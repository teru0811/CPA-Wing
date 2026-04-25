import streamlit as st
import time
import random
from datetime import date
from streamlit_javascript import st_javascript

# --- ページ設定 ---
st.set_page_config(page_title="守護クマCPA攻略🧸", page_icon="🧸")

# --- 1. デザイン（カラフル＆クマさん仕様） ---
st.markdown("""
    <style>
    .stApp { background-color: #FFF9F2; }
    .status-card {
        background: white; padding: 15px; border-radius: 20px;
        border: 2px solid #FFE4B5; text-align: center; margin-bottom: 10px;
    }
    .goal-card {
        background: linear-gradient(135deg, #FF4B4B 0%, #FF8E8E 100%);
        color: white; padding: 15px; border-radius: 20px;
        text-align: center; margin-bottom: 10px;
    }
    .bear-bubble {
        background: #FFFFFF; padding: 15px; border-radius: 40px;
        border: 2px solid #FFDAB9; position: relative; margin-bottom: 20px;
        text-align: center; font-weight: bold; color: #8B4513;
    }
    .money-text { color: #D4AF37; font-size: 28px; font-weight: bold; margin: 0; }
    /* 科目ボタンのスタイル */
    .stButton > button {
        background: linear-gradient(135deg, #FFDAB9, #FFB6C1);
        color: #8B4513; height: 70px; width: 100%;
        border-radius: 35px; font-size: 18px; font-weight: bold; border: 3px solid #FFF;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 🧠 記憶の魔法（LocalStorageから読み込み） ---
# 財務、管理、お金の3つのデータをブラウザから取得
s_money = st_javascript("localStorage.getItem('my_study_money');")
s_z_count = st_javascript("localStorage.getItem('my_z_count');")
s_k_count = st_javascript("localStorage.getItem('my_k_count');")

# 初回起動時や保存がない場合の初期値設定
if 'money' not in st.session_state:
    st.session_state.money = int(s_money) if s_money and s_money != "null" else 0
    st.session_state.z_count = int(s_z_count) if s_z_count and s_z_count != "null" else 39
    st.session_state.k_count = int(s_k_count) if s_k_count and s_k_count != "null" else 15

# --- 3. 保存用関数 ---
def save_all():
    st_javascript(f"localStorage.setItem('my_study_money', '{st.session_state.money}');")
    st_javascript(f"localStorage.setItem('my_z_count', '{st.session_state.z_count}');")
    st_javascript(f"localStorage.setItem('my_k_count', '{st.session_state.k_count}');")

# --- 4. メイン表示 ---
st.title("🧸 CPA不滅の進捗ログ 💰")

# クマのメッセージ
bear_messages = ["財務も管理も、ボクがしっかり数えておくよ！", "ポチポチするたび、合格とご褒美に近づくね🧸", "5/31まで一緒に走り抜けよう！"]
st.markdown('<div style="text-align: center; font-size: 50px;">🧸</div>', unsafe_allow_html=True)
st.markdown(f'<div class="bear-bubble">「{random.choice(bear_messages)}」</div>', unsafe_allow_html=True)

# カウントダウン & 貯金
days_left = (date(2026, 5, 31) - date.today()).days
c1, c2 = st.columns(2)
with c1:
    st.markdown(f'<div class="goal-card"><p style="margin:0;font-size:10px;">🏁 5/31まで</p><p style="margin:0;font-size:24px;font-weight:bold;">{max(0, days_left)} 日</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown(f'<div class="status-card"><p style="margin:0;font-size:10px;color:#999;">💰 ご褒美貯金</p><p class="money-text">¥{st.session_state.money:,}</p></div>', unsafe_allow_html=True)

# 科目タブ
tab1, tab2 = st.tabs(["📊 財務会計 (70)", "📉 管理会計 (33)"])

with tab1:
    z_total = 70
    st.subheader(f"進捗: {st.session_state.z_count} / {z_total}")
    st.progress(st.session_state.z_count / z_total)
    if st.button("✨ 財務を1コマ完了！"):
        st.session_state.z_count += 1
        st.session_state.money += 500
        save_all()
        st.balloons()
        st.rerun()

with tab2:
    k_total = 33
    st.subheader(f"進捗: {st.session_state.k_count} / {k_total}")
    st.progress(st.session_state.k_count / k_total)
    if st.button("🔥 管理を1コマ完了！"):
        st.session_state.k_count += 1
        st.session_state.money += 500
        save_all()
        st.balloons()
        st.rerun()

# 修正ボタン（サイドバー）
st.sidebar.header("修正用")
if st.sidebar.button("財務を1つ戻す"):
    st.session_state.z_count -= 1
    save_all()
    st.rerun()
if st.sidebar.button("管理を1つ戻す"):
    st.session_state.k_count -= 1
    save_all()
    st.rerun()
