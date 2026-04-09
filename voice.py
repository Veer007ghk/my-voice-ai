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

# Professional AI Theme (ChatGPT/Gemini Style)
st.markdown("""
    <style>
    /* पूरे पेज का बैकग्राउंड - Deep Dark */
    .stApp {
        background-color: #050505;
        color: #FFFFFF;
    }
    
    /* टॉप हेडर स्टाइल */
    .main-header {
        background: linear-gradient(90deg, #1e3a8a, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 5px;
        font-family: 'Inter', sans-serif;
    }

    /* कार्ड्स और कंटेनर - Modern Border */
    div[data-testid="stVerticalBlock"] > div:has(div.stTextArea) {
        background: #111111;
        padding: 25px;
        border-radius: 20px;
        border: 1px solid #222222;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }

    /* टेक्स्ट एरिया कस्टमाइजेशन */
    .stTextArea textarea {
        background-color: #000000 !important;
        color: #ffffff !important;
        border: 1px solid #333333 !important;
        border-radius: 12px !important;
        font-family: 'Monaco', monospace;
    }

    /* बटन - ChatGPT Style Green/Blue */
    .stButton>button {
        background-color: #10a37f !important; /* ChatGPT Green */
        color: white !important;
        border-radius: 10px !important;
        border: none !important;
        padding: 12px 24px !important;
        font-weight: 600 !important;
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #1a7f64 !important;
        transform: scale(1.02);
    }

    /* स्लाइडर्स और सेलेक्ट बॉक्स */
    .stSlider [data-baseweb="slider"] {
        margin-top: 20px;
    }
    
    /* लेबल टेक्स्ट */
    label {
        color: #999999 !important;
        font-weight: 500 !important;
    }

    /* ऑडियो प्लेयर को क्लीन बनाना */
    audio {
        width: 100%;
        border-radius: 10px;
        margin-top: 20px;
        filter: invert(100%) hue-rotate(180deg) brightness(1.5); /* Dark Mode Audio Player */
    }
    </style>
    """, unsafe_allow_html=True)

# हैडर
st.markdown("<h1 class='main-header'>Harsh AI Voice Studio</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Ultimate AI Voice Production Platform</p>", unsafe_allow_html=True)

# मुख्य कंटेंट
st.markdown("---")

col1, col2 = st.columns([1.5, 1])

with col1:
    # टेक्स्ट इनपुट
    text_area = st.text_area("SCRIPT INPUT", height=400, placeholder="अपनी स्क्रिप्ट यहाँ लिखें या पेस्ट करें...", key="main_text")
    
    # क्लियर बटन छोटा और साइड में
    if st.button("Clear Desktop"):
        st.session_state.main_text = ""
        st.rerun()

with col2:
    st.markdown("### CONFIGURATION")
    
    voice_map = {
        "--- Indian Hindi ---": "hi-IN-MadhurNeural",
        "Male: Madhur (Pure Hindi)": "hi-IN-MadhurNeural",
        "Female: Swara (Pure Hindi)": "hi-IN-SwaraNeural",
        "--- US English (Global) ---": "en-US-GuyNeural",
        "Male: Christopher (Deep US)": "en-US-ChristopherNeural",
        "Male: Guy (Neutral US)": "en-US-GuyNeural",
        "Female: Ava (Soft US)": "en-US-AvaNeural",
        "--- UK English (Royal) ---": "en-GB-ThomasNeural",
        "Male: Thomas (British)": "en-GB-ThomasNeural",
        "Female: Libby (British)": "en-GB-LibbyNeural"
    }
    
    voice_choice = st.selectbox("SELECT VOCAL MODEL", list(voice_map.keys()))
    
    st.markdown("---")
    pitch = st.slider("VOCAL PITCH", -20, 20, -5)
    rate = st.slider("SPEECH RATE", -20, 20, -2)

# जेनरेट बटन
st.markdown("<br>", unsafe_allow_
