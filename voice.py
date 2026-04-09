import streamlit as st
import asyncio
import edge_tts
import os
import random

# 1. PAGE SETUP
st.set_page_config(page_title="Harsh AI Rock-Solid Studio", page_icon="🎙️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    .main-header {
        background: linear-gradient(90deg, #1A73E8, #34A853);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem; font-weight: 800; text-align: center;
    }
    .stButton>button {
        background-color: #1A73E8 !important; color: white !important;
        border-radius: 12px !important; font-weight: bold !important;
        height: 60px; width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>Harsh AI Rock-Solid Studio</h1>", unsafe_allow_html=True)
st.write("---")

# 2. FIXED VOICE DATABASE (Pitch & Rate locked for stability)
VOICE_DB = {
    "1. Madhur (Hindi Male)": {"id": "hi-IN-MadhurNeural", "p": "-5Hz", "r": "-2%"},
    "2. Hemant (Hindi Deep)": {"id": "hi-IN-HemantNeural", "p": "-10Hz", "r": "-5%"},
    "3. Ankit (Hindi Bold)": {"id": "hi-IN-AnkitNeural", "p": "-5Hz", "r": "-2%"},
    "4. Swara (Hindi Female)": {"id": "hi-IN-SwaraNeural", "p": "0Hz", "r": "0%"},
    "5. Prabhat (Ind Eng)": {"id": "en-IN-PrabhatNeural", "p": "0Hz", "r": "0%"},
    "6. Christopher (US Deep)": {"id": "en-US-ChristopherNeural", "p": "-10Hz", "r": "-5%"},
    "7. Thomas (UK Formal)": {"id": "en-GB-ThomasNeural", "p": "-5Hz", "r": "0%"}
}

col1, col2 = st.columns([1.5, 1], gap="large")

with col1:
    st.markdown("### 📝 SCRIPT EDITOR")
    script = st.text_area("Enter your script:", height=350, placeholder="Paste your story here...")

with col2:
    st.markdown("### 🎙️ VOICE SELECTION")
    chosen = st.selectbox("Select Voice:", list(VOICE_DB.keys()))
    st.info("⚠️ Note: Voice settings are pre-tuned for maximum stability and professional sound. Sliders removed to prevent errors.")
    
    bgm = st.selectbox("Background Mood:", ["None", "Mysterious", "Serious News"])

# 3. GENERATION ENGINE (No UI interaction with Pitch/Rate)
async def generate_audio(text, v_config):
    filename = f"final_{random.randint(100,999)}.mp3"
    try:
        communicate = edge_tts.Communicate(text, v_config['id'], pitch=v_config['p'], rate=v_config['r'])
        await communicate.save(filename)
        return True, filename
    except Exception:
        return False, None

if st.button("🚀 GENERATE AUDIO"):
    if not script.strip():
        st.warning("Script is empty!")
    else:
        with st.spinner("Generating..."):
            success, file = asyncio.run(generate_audio(script, VOICE_DB[chosen]))
            if success:
                st.success("✅ Success!")
                st.audio(file)
                with open(file, "rb") as f:
                    st.download_button("📥 Download", f, file_name="Harsh_Studio_Audio.mp3")
            else:
                st.error("Server is busy. Please try again after 10 seconds.")
