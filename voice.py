import streamlit as st
import asyncio
import edge_tts
import os

# Ultra Modern Page Setup
st.set_page_config(
    page_title="Harsh AI Studio", 
    page_icon="🎙️", 
    layout="wide"
)

# ChatGPT/Gemini Style Professional Design
st.markdown("""
    <style>
    .stApp {
        background-color: #0d0d0d;
        color: #FFFFFF;
    }
    .main-header {
        background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 20px;
    }
    .stTextArea textarea {
        background-color: #1a1a1a !important;
        color: #ffffff !important;
        border: 1px solid #333 !important;
        border-radius: 12px !important;
    }
    .stButton>button {
        background: linear-gradient(45deg, #10a37f, #1a7f64) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 12px 24px !important;
        width: 100%;
        font-weight: bold !important;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.01);
        box-shadow: 0 4px 15px rgba(16, 163, 127, 0.4);
    }
    label {
        color: #888 !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>Harsh AI Voice Studio</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([1.5, 1], gap="large")

with col1:
    text_area = st.text_area("SCRIPT INPUT", height=380, placeholder="अपनी स्क्रिप्ट यहाँ लिखें...", key="input_text")
    if st.button("🗑️ Clear Canvas"):
        st.session_state.input_text = ""
        st.rerun()

with col2:
    st.markdown("### CONFIGURATION")
    voice_map = {
        "--- Indian Hindi ---": "hi-IN-MadhurNeural",
        "Male: Madhur (Hindi)": "hi-IN-MadhurNeural",
        "Female: Swara (Hindi)": "hi-IN-SwaraNeural",
        "--- US English ---": "en-US-GuyNeural",
        "Male: Christopher (US)": "en-US-ChristopherNeural",
        "Female: Ava (US)": "en-US-AvaNeural",
        "--- UK English ---": "en-GB-ThomasNeural",
        "Male: Thomas (UK)": "en-GB-ThomasNeural",
        "Female: Libby (UK)": "en-GB-LibbyNeural"
    }
    voice_choice = st.selectbox("VOCAL MODEL", list(voice_map.keys()))
    
    st.write("---")
    pitch = st.slider("VOCAL PITCH", -20, 20, -5)
    rate = st.slider("SPEECH RATE", -20, 20, -2)

st.write("---")

if st.button("🚀 RUN GENERATION"):
    if "---" in voice_choice:
        st.error("Please select a valid voice model.")
    elif not text_area.strip():
        st.warning("Script is empty.")
    else:
        try:
            target_v = voice_map[voice_choice]
            async def run_tts():
                p = f"{pitch}Hz"
                r = f"{rate}%"
                comm = edge_tts.Communicate(text_area, target_v, pitch=p, rate=r)
                await comm.save("output.mp3")

            with st.spinner("AI Processing..."):
                asyncio.run(run_tts())
            
            st.audio("output.mp3")
            with open("output.mp3", "rb") as f:
                st.download_button("⬇️ Download Audio", f, file_name="harsh_audio.mp3")
        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("<p style='text-align: center; color: #333; margin-top: 50px;'>Harsh AI | 2026 Pro Version</p>", unsafe_allow_html=True)
