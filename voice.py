import streamlit as st
import asyncio
import edge_tts
import os

# Ultra Safe Page Config
st.set_page_config(page_title="Harsh AI Studio Pro", page_icon="🎙️", layout="wide")

# Try to import translator safely
try:
    from googletrans import Translator
    translator = Translator()
    translator_available = True
except:
    translator_available = False

# CSS Styling
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
        background: #F8F9FA; padding: 10px; border-radius: 10px;
        text-align: center; border: 1px solid #E0E0E0; margin-bottom: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>Harsh AI Ultimate Studio</h1>", unsafe_allow_html=True)

# Sidebar for Translator
with st.sidebar:
    st.header("🌐 QUICK TRANSLATOR")
    if translator_available:
        source_text = st.text_area("Hindi to English:")
        if st.button("Translate Now"):
            if source_text:
                try:
                    res = translator.translate(source_text, dest='en')
                    st.code(res.text)
                except:
                    st.error("Translation server busy. Try again later.")
    else:
        st.warning("Translator is updating. Use the Main Studio for Voice.")

# Main Dashboard
col1, col2 = st.columns([1.5, 1], gap="large")

with col1:
    st.markdown("### 🖋️ SCRIPT EDITOR")
    script = st.text_area("Enter your script:", height=380, placeholder="Type here...", key="main_script")
    
    # Live Stats
    words = len(script.split())
    chars = len(script)
    st.markdown(f"""
        <div style='display: flex; gap: 10px;'>
            <div class='stats-card' style='flex: 1;'>Words: {words}</div>
            <div class='stats-card' style='flex: 1;'>Characters: {chars}</div>
        </div>
    """, unsafe_allow_html=True)

    if st.button("🗑️ Clear Canvas"):
        st.session_state.main_script = ""
        st.rerun()

with col2:
    st.markdown("### 🎙️ VOCAL LIBRARY")
    v_map = {
        "--- HINDI ---": "hi-IN-MadhurNeural",
        "Madhur (Deep Male)": "hi-IN-MadhurNeural",
        "Swara (Clean Female)": "hi-IN-SwaraNeural",
        "Asad (Bold Male)": "ur-PK-AsadNeural",
        "--- ENGLISH (US) ---": "en-US-ChristopherNeural",
        "Christopher (US Male)": "en-US-ChristopherNeural",
        "Guy (US Male)": "en-US-GuyNeural",
        "Ava (US Female)": "en-US-AvaNeural",
        "--- ENGLISH (UK) ---": "en-GB-ThomasNeural",
        "Thomas (UK Male)": "en-GB-ThomasNeural",
        "Libby (UK Female)": "en-GB-LibbyNeural",
        "--- INDIAN ENGLISH ---": "en-IN-PrabhatNeural",
        "Prabhat (News Style)": "en-IN-PrabhatNeural"
    }
    selected_voice = st.selectbox("Select Voice:", list(v_map.keys()))
    
    st.markdown("---")
    st.markdown("### 🎚️ TUNING")
    pitch = st.slider("Vocal Depth", -20, 20, -5)
    speed = st.slider("Reading Speed", -20, 20, -2)

st.write("---")

if st.button("🚀 GENERATE MASTER AUDIO"):
    if "---" in selected_voice:
        st.error("Please select a voice model.")
    elif not script.strip():
        st.warning("Script is empty!")
    else:
        try:
            voice_id = v_map[selected_voice]
            async def generate():
                p = f"{pitch}Hz"
                s = f"{speed}%"
                communicate = edge_tts.Communicate(script, voice_id, pitch=p, rate=s)
                await communicate.save("final.mp3")

            with st.spinner("AI is working..."):
                asyncio.run(generate())
            
            st.success("✅ Success!")
            st.audio("final.mp3")
            with open("final.mp3", "rb") as f:
                st.download_button("📥 Download MP3", f, file_name="Harsh_Voice.mp3")
        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("<p style='text-align: center; color: #999; margin-top: 50px;'>Harsh AI Studio v3.5 | Pro</p>", unsafe_allow_html=True)
