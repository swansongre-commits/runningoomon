import pathlib

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="러너 게임", page_icon="🏃", layout="centered")

# 모바일 친화적으로 상단 여백 축소
st.markdown(
    """
    <style>
      .block-container { padding-top: 3.5rem; padding-bottom: 0.5rem; max-width: 860px; }
    </style>
    <h1 style='text-align:center; margin-bottom:0; font-size:1.6rem;'>🏃 러너 게임</h1>
    <p style='text-align:center; color:#888; margin-top:4px; font-size:0.9rem;'>
        구글 공룡게임 스타일 · 🐱 고양이 / 🐰 토끼 / 🐢 거북이 / 👽 외계인 중 선택!
    </p>
    """,
    unsafe_allow_html=True,
)

game_html = pathlib.Path(__file__).with_name("index.html").read_text(encoding="utf-8")
# 모바일에서는 화면 터치 버튼이 추가로 표시되어 높이를 넉넉히 확보
components.html(game_html, height=560, scrolling=False)

st.caption("📱 모바일: 가로모드 권장 · 화면을 탭하면 점프 · ⬇버튼은 숙이기   |   💻 PC: 화면 클릭 후 스페이스(점프)/↓(숙이기)/ESC(나가기)")
