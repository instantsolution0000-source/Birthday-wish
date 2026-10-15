import streamlit as st
import time

# Configure page for mobile view
st.set_page_config(page_title="Happy Birthday!", page_icon="🎂", layout="centered")

# Custom CSS for a mobile card look
st.markdown("""
    <style>
    .birthday-card {
        background: linear-gradient(135deg, #ff758c 0%, #ff7eb3 100%);
        padding: 30px 20px;
        border-radius: 20px;
        text-align: center;
        color: white;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        font-family: 'sans-serif';
        margin-top: 20px;
    }
    .birthday-title {
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .birthday-name {
        font-size: 26px;
        color: #fffac2;
        margin-bottom: 20px;
    }
    .birthday-msg {
        font-size: 18px;
        line-height: 1.5;
    }
    </style>
""", unsafe_allow_html=True)

# Replace with the birthday person's name
NAME = "Gobinda"

st.markdown(f"""
    <div class="birthday-card">
        <div class="birthday-title">🎉 Happy Birthday! 🎂</div>
        <div class="birthday-name">Dear {NAME} ✨</div>
        <div class="birthday-msg">
            Wishing you a day filled with laughter, love, and all your favorite things. 
            May this year bring you closer to all your dreams!
        </div>
    </div>
""", unsafe_allow_html=True)

st.write("") # Spacing

# Interactive mobile button (full width)
if st.button("🎁 Tap to Open Your Surprise!", use_container_width=True):
    st.balloons()
    time.sleep(0.5)
    st.success(f"🥳 Have an amazing year ahead, {NAME}! 🥂")
    st.snow()
