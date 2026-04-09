import streamlit as st
import asyncio
import edge_tts
import os

# Ultra-Stable Page Configuration
st.set_page_config(page_title="Harsh AI Production Studio", page_icon="🎙️", layout="wide")

# Translator Logic
try:
    from googletrans import Translator
    translator = Translator()
    trans_ready = True
except:
    trans_ready = False

# Professional CSS
st.markdown("""
    <style>
    .stApp { background-color: #F8F9FA; color: #202124; }
    .main-header {
        background: linear-gradient(90deg, #1A73E8, #34A853);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.8rem; font-weight: 800; text-align: center; margin-bottom: 5px;
    }
    .stats-card {
        background: #FFFFFF; padding: 15px; border-radius: 12px;
        text-align: center; border: 1px solid #E0E0E0; box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .stButton>button {
        background-color: #1A73E8 !important; color: white !important;
        border-radius: 10px !important; font-weight: bold !important;
        height: 50px; width: 100%; transition: 0.3s;
    }
    label { font-weight: 600 !important; color: #3C4043 !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>Harsh AI Production Studio</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #5F6368;'>Voice Generation + Background Atmosphere</p>", unsafe_allow_html=True)
st.write("---")

col1, col2 = st.columns([1.6, 1], gap="large")

with col1:
    st.markdown("### 📝 SCRIPT EDITOR")
    
    with st.expander("🌐 Quick Translator (Hindi ➔ English)"):
        h_text = st.text_area("Paste Hindi text here:", height=100)
        if st.button("Translate Now"):
            if h_text and trans_ready:
                try:
                    res = translator.translate(h_text, dest='en')
                    st.code(res.text)
                except: st.error("Translator busy. Please retry.")
            else: st.warning("Translator initializing...")

    script = st.text_area("Enter your final script:", height=320, placeholder="Type or paste here...", key="main_script")
    
    # Live Stats with Duration
    words = len(script.split())
    chars = len(script)
    total_sec = round((words / 150) * 60)
    
    s1, s2, s3 = st.columns(3)
    s1.markdown(f"<div class='stats-card'>Words<br><b>{words}</b></div>", unsafe_allow_html=True)
    s2.markdown(f"<div class='stats-card'>Chars<br><b>{chars}</b></div>", unsafe_allow_html=True)
    s3.markdown(f"<div class='stats-card'>Duration<br><b style='color:#1A73E8;'>{total_sec // 60}m {total_sec % 60}s</b></div>", unsafe_allow_html=True)

    if st.button("🗑️ Reset Editor"):
        st.session_state.main_script = ""
        st.rerun()

with col2:
    st.markdown("### 🎙️ VOICE & ATMOSPHERE")
    
    v_map = {
        "--- HINDI MODELS ---": "hi-IN-MadhurNeural",
        "Madhur (Deep Male)": "hi-IN-MadhurNeural",
        "Swara (Clear Female)": "hi-IN-SwaraNeural",
        "Asad (Bold Male)": "ur-PK-AsadNeural",
        "--- WESTERN MODELS ---": "en-US-ChristopherNeural",
        "Christopher (US Male)": "en-US-ChristopherNeural",
        "Guy (US Male)": "en-US-GuyNeural",
        "Ava (US Female)": "en-US-AvaNeural",
        "Thomas (UK Male)": "en-GB-ThomasNeural",
        "Libby (UK Female)": "en-GB-LibbyNeural",
        "--- INDIAN ACCENT ---": "en-IN-PrabhatNeural",
        "Prabhat (News Style)": "en-IN-PrabhatNeural"
    }
    
    selected_voice = st.selectbox("Select Voice:", list(v_map.keys()))
    
    st.write("---")
    st.markdown("### 🎚️ TUNING")
    pitch = st.slider("Vocal Depth", -20, 20, -5)
    rate = st.slider("Speech Rate", -20, 20, -2)
    
    st.write("---")
    # NEW FEATURE: BGM PRESETS
    st.markdown("### 🎵 ATMOSPHERIC BGM")
    bgm_mood = st.selectbox("Select Background Mood:", ["None", "Serious News", "Mysterious", "Emotional", "Cinematic"])
    st.caption("Note: Mix BGM during video editing for better volume control.")

st.write("---")

if st.button("🚀 GENERATE PROFESSIONAL PRODUCTION"):
    if "---" in selected_voice:
        st.error("Please select a specific voice model.")
    elif not script.strip():
        st.warning("Script is empty!")
    else:
        try:
            voice_id = v_map[selected_voice]
            async def run_tts():
                p, r = f"{pitch}Hz", f"{rate}%"
                comm = edge_tts.Communicate(script, voice_id, pitch=p, rate=r)
                await comm.save("harsh_final.mp3")

            with st.spinner("AI Studio is processing your request..."):
                asyncio.run(run_tts())
            
            st.success("✅ Voice Generated Successfully!")
            st.audio("harsh_final.mp3")
            
            with open("harsh_final.mp3", "rb") as f:
                st.download_button("📥 Download Audio", f, file_name="Harsh_Production.mp3")
        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("<p style='text-align: center; color: #999; margin-top: 50px;'>Harsh AI Production Studio | v6.0 | 2026</p>", unsafe_allow_html=True)
