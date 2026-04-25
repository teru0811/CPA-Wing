import streamlit as st
import os

# --- スタイル設定（CSS） ---
st.markdown("""
    <style>
    /* 全体の背景 */
    .stApp {
        background: linear-gradient(180deg, #0f2027 0%, #203a43 50%, #2b5876 100%);
        color: #ffffff;
    }
    
    /* ガラス風のカードデザイン */
    .stMetric, .stButton>button {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        color: white !important;
        padding: 20px;
    }

    /* ボタンのホバー効果 */
    .stButton>button:hover {
        background: rgba(0, 172, 193, 0.3) !important;
        border: 1px solid #00acc1 !important;
        box-shadow: 0 0 15px #00acc1;
        transition: 0.5s;
    }

    /* 進捗バーの色を水色に */
    div.stProgress > div > div > div > div {
        background-color: #00e5ff;
    }
    
    /* 文字の色調整 */
    h1, h2, h3, p {
        color: #e0f7fa !important;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 200;
    }
    </style>
    """, unsafe_allow_html=True)

# --- データの保存・読込処理（前回と同じ） ---
SAVE_FILE = "study_progress.txt"
def load_data():
    return int(open(SAVE_FILE, "r").read()) if os.path.exists(SAVE_FILE) else 0

def save_data(count):
    with open(SAVE_FILE, "w") as f: f.write(str(count))

if 'count' not in st.session_state:
    st.session_state.count = load_data()

# --- メインコンテンツ ---
st.title("🦋 Deep Sea Study Log")
st.write("一歩進むたびに、暗闇に光が灯ります。")

# 進捗メトリクス
total = 100
col1, col2 = st.columns(2)
with col1:
    st.metric(label="完了", value=f"{st.session_state.count} / {total}")
with col2:
    st.metric(label="進捗率", value=f"{(st.session_state.count/total)*100:.1f}%")

st.progress(st.session_state.count / total)

st.markdown("<br>", unsafe_allow_html=True)

# ポチポチボタン（巨大化）
if st.button("✨ 講義を撃破して次へ進む"):
    st.session_state.count += 1
    save_data(st.session_state.count)
    st.balloons()

# 履歴の視覚化（蝶が並ぶ）
st.markdown("---")
st.subheader("Collected Lights")
history_html = "".join(["<span style='font-size:30px; text-shadow: 0 0 10px #00e5ff;'>🦋</span>" for _ in range(st.session_state.count)])
st.markdown(history_html, unsafe_allow_html=True)
