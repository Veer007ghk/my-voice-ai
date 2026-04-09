import streamlit as st
import asyncio
import edge_tts
import os
from googletrans import Translator

# Page Configuration
st.set_page_config(page_title="Harsh AI Ultimate Studio", page_icon="🎙️", layout="wide")

# Translator Initialize
translator = Translator()

# Premium CSS Styling
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    .main-header {
        background: linear-gradient(90deg, #1A73E8, #34A853);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem; font-weight: 800; text-align: center;
    }
    .stats-card {
        background: #F1F3F4; padding: 15px; border-radius: 10px;
        text-align: center; border: 1px solid #E0E0E0;
    }
    .stButton>button {
        border-radius: 10px !important; font-weight: bold !important;
        height: 45px; transition: 0.3s;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>Harsh AI Ultimate Studio</h1>", unsafe_allow_html=True)

# Sidebar for Advanced Tools
with st.sidebar:
    st.header("🛠️ ADVANCED TOOLS")
    
    # Feature 1: Auto-Translation
    st.subheader("1. Instant Translator")
    source_text = st.text_area("Paste Hindi text to translate:")
    if st.button("Translate to English"):
        if source_text:
            translated = translator.translate(source_text, src='hi', dest='en')
            st.success("Translated Text:")
            st.code(translated.text)
        else:
            st.warning("Please enter text first.")

    st.write("---")
    st.subheader("2. Interview Mode Help")
    st.info("To create an interview, generate Person 1's audio, then Person 2's, and join them in your video editor. (Full auto-merge coming soon!)")

# Main Dashboard
col1, col2 = st.columns([1.5, 1], gap="large")

with col1:
    st.markdown("### 🖋️ SCRIPT & ANALYSIS")
    script = st.text_area("Enter your script here:", height=350, placeholder="Hello everyone, today we discuss...", key="main_script")
    
    # Feature 2: Stats Box
    words = len(script.split())
    chars = len(script)
    est_time = round(words / 2.5)
    
    s1, s2, s3 = st.columns(3)
    s1.markdown(f"<div class='stats-card'>📝 Words<br><b>{words}</b></div>", unsafe_allow_html=True)
    s2.markdown(f"<div class='stats-card'>🔢 Characters<br><b>{chars}</b></div>", unsafe_allow_html=True)
    s3.markdown(f"<div class='stats-card'>⏳ Est. Time<br><b>{est_time}s</b></div>", unsafe_allow_html=True)

    if st.button("🗑️ Reset Editor"):
        st.session_state.main_script = ""
        st.rerun()

with col2:
    st.markdown("### 🎙️ VOCAL CONFIGURATION")
    
    v_map = {
        "--- HINDI MODELS ---": "hi-IN-MadhurNeural",
        "Madhur (Deep Male)": "hi-IN-MadhurNeural",
        "Swara (Clean Female)": "hi-IN-SwaraNeural",
        "Asad (Bold Male)": "ur-PK-AsadNeural",
        "--- WESTERN MODELS (US/UK) ---": "en-US-ChristopherNeural",
        "Christopher (US - Documentary)": "en-US-ChristopherNeural",
        "Guy (US - Narrative)": "en-US-GuyNeural",
        "Ava (US - Soft)": "en-US-AvaNeural",
        "Thomas (UK - Formal)": "en-GB-ThomasNeural",
        "Libby (UK - Professional)": "en-GB-LibbyNeural",
        "--- INDIAN ACCENT ENGLISH ---": "en-IN-PrabhatNeural",
        "Prabhat (News Style)": "en-IN-PrabhatNeural",
        "Ananya (Modern)": "en-IN-AnanyaNeural"
    }
    
    selected_voice = st.selectbox("Choose Vocal Cord:", list(v_map.keys()))
    
    st.write("---")
    st.markdown("### 🎚️ TUNING")
    pitch = st.slider("Vocal Depth (Pitch)", -20, 20, -5)
    speed = st.slider("Reading Speed", -20, 20, -2)
    
    st.write("---")
    # Feature 3: Background Music Suggestion (Visual Only for now)
    st.markdown("🎵 **BGM Mood Suggestion:**")
    bgm_mood = st.selectbox("Select video mood for BGM advice:", ["Serious/News", "Mysterious", "Cinematic", "Educational"])
    if bgm_mood == "Serious/News":
        st.caption("Tip: Use 'Low Bass' corporate tracks.")

st.write("---")

# Generation Logic
if st.button("🚀 GENERATE MASTER AUDIO"):
    if "---" in selected_voice:
        st.error("Please select a specific voice, not a category header.")
    elif not script.strip():
        st.warning("Script is empty! Please write something.")
    else:
        try:
            voice_id = v_map[selected_voice]
            async def generate():
                p = f"{pitch}Hz"
                s = f"{speed}%"
                communicate = edge_tts.Communicate(script, voice_id, pitch=p, rate=s)
                await communicate.save("harsh_final.mp3")

            with st.spinner("AI is synthesizing your VIP audio..."):
                asyncio.run(generate())
            
            st.success("✅ Audio Processed Successfully!")
            st.audio("harsh_final.mp3")
            
            with open("harsh_final.mp3", "rb") as f:
                st.download_button("📥 Download HQ Audio", f, file_name="Harsh_Master_Audio.mp3")
                
        except Exception as e:
            st.error(f"Error encountered: {e}")

st.markdown("<p style='text-align: center; color: #999; margin-top: 50px;'>Harsh AI Ultimate Studio v3.0 | 2026</p>", unsafe_allow_html=True)
