import streamlit as st
import asyncio
import edge_tts
import os

# Ultra Clean Page Config
st.set_page_config(page_title="Harsh AI Studio Pro", page_icon="🎙️", layout="wide")

# Modern Light Theme - Fully English Labels
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; color: #202124; }
    .main-header {
        background: linear-gradient(90deg, #1A73E8, #4285F4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem; font-weight: 800; text-align: center;
    }
    .stTextArea textarea {
        border: 2px solid #E0E0E0 !important;
        border-radius: 15px !important;
        background-color: #F8F9FA !important;
    }
    .stButton>button {
        background-color: #1A73E8 !important;
        color: white !important;
        border-radius: 12px !important;
        font-weight: bold !important;
        width: 100%; height: 50px;
    }
    .stats-box {
        padding: 10px; border-radius: 10px; background-color: #E8F0FE;
        color: #1967D2; font-weight: bold; text-align: center; margin-bottom: 10px;
    }
    label { font-size: 1rem !important; font-weight: 600 !important; color: #3C4043 !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>Harsh AI Voice Studio</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Premium Vocal Production Platform</p>", unsafe_allow_html=True)
st.write("---")

col1, col2 = st.columns([1.5, 1], gap="large")

with col1:
    st.markdown("### 🖋️ SCRIPT EDITOR")
    text_data = st.text_area("Enter your script here:", height=380, placeholder="Type or paste your content...", key="user_script")
    
    # Feature: Real-time Stats
    char_count = len(text_data)
    words = len(text_data.split())
    est_time = round(words / 2.5) # Approx 150 words per minute
    
    st.markdown(f"""
        <div style='display: flex; gap: 10px;'>
            <div class='stats-box' style='flex: 1;'>Characters: {char_count}</div>
            <div class='stats-box' style='flex: 1;'>Words: {words}</div>
            <div class='stats-box' style='flex: 1;'>Est. Duration: {est_time}s</div>
        </div>
    """, unsafe_allow_html=True)

    if st.button("🗑️ Clear Canvas"):
        st.session_state.user_script = ""
        st.rerun()

with col2:
    st.markdown("### 🎙️ VOCAL LIBRARY")
    v_map = {
        "1. Madhur (Hindi Male)": "hi-IN-MadhurNeural",
        "2. Swara (Hindi Female)": "hi-IN-SwaraNeural",
        "3. Asad (Urdu/Hindi Deep Male)": "ur-PK-AsadNeural",
        "4. Uzma (Urdu/Hindi Soft Female)": "ur-PK-UzmaNeural",
        "5. Prabhat (Indian English Male)": "en-IN-PrabhatNeural",
        "6. Neerja (Indian English Female)": "en-IN-NeerjaNeural",
        "7. Ravi (Indian English Male)": "en-IN-RaviNeural",
        "8. Christopher (US Male - Deep)": "en-US-ChristopherNeural",
        "9. Guy (US Male - Neutral)": "en-US-GuyNeural",
        "10. Ava (US Female - Soft)": "en-US-AvaNeural",
        "11. Jenny (US Female - Professional)": "en-US-JennyNeural",
        "12. Thomas (UK Male - Serious)": "en-GB-ThomasNeural",
        "13. Ryan (UK Male - Young)": "en-GB-RyanNeural",
        "14. Libby (UK Female - Clear)": "en-GB-LibbyNeural",
        "15. Maisie (UK Female - Soft)": "en-GB-MaisieNeural"
    }
    selected_v = st.selectbox("Select Voice Model:", list(v_map.keys()))
    
    st.write("---")
    st.markdown("### 🎚️ TUNING PANEL")
    v_pitch = st.slider("Vocal Pitch (Bass/Treble)", -20, 20, -5)
    v_rate = st.slider("Speech Rate (Speed)", -20, 20, -2)
    
    # Feature: Audio Format Selection
    a_format = st.radio("Output Format:", ["mp3", "wav"], horizontal=True)

st.write("---")

if st.button("🚀 GENERATE PROFESSIONAL AUDIO"):
    if not text_data.strip():
        st.warning("Please enter some text in the script editor first.")
    else:
        try:
            target_voice = v_map[selected_v]
            async def start_tts():
                p = f"{v_pitch}Hz"
                r = f"{v_rate}%"
                # Updated for better quality
                comm = edge_tts.Communicate(text_data, target_voice, pitch=p, rate=r)
                await comm.save(f"output.{a_format}")

            with st.spinner("AI is crafting your voice..."):
                asyncio.run(start_tts())
            
            st.success("Audio Generated Successfully!")
            st.audio(f"output.{a_format}")
            with open(f"output.{a_format}", "rb") as f:
                st.download_button(f"📥 Download {a_format.upper()}", f, file_name=f"Harsh_AI_Studio.{a_format}")
        except Exception as err:
            st.error(f"System Error: {err}")

st.markdown("<p style='text-align: center; color: #BDC1C6; margin-top: 50px;'>Harsh AI Studio | Pro Edition 2026</p>", unsafe_allow_html=True)
