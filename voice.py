import streamlit as st
import asyncio
import edge_tts
import os

# Page Setup
st.set_page_config(page_title="Harsh AI Studio", page_icon="🎙️", layout="wide")

# Modern Light Mode Theme (Apple/Google Style)
st.markdown("""
    <style>
    .stApp {
        background-color: #F8F9FA;
        color: #202124;
    }
    .main-header {
        background: linear-gradient(90deg, #1A73E8 0%, #4285F4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.8rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 10px;
    }
    .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #202124 !important;
        border: 1px solid #DADCE0 !important;
        border-radius: 12px !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .stButton>button {
        background-color: #1A73E8 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        font-weight: 600 !important;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #1765CC !important;
        box-shadow: 0 4px 12px rgba(66, 133, 244, 0.3);
    }
    .voice-box {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #DADCE0;
    }
    label {
        color: #5F6368 !important;
        font-weight: 600 !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>Harsh AI Voice Studio</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #5F6368;'>प्रोफेशनल और रियलिस्टिक वॉइस जनरेशन</p>", unsafe_allow_html=True)

col1, col2 = st.columns([1.6, 1], gap="medium")

with col1:
    text_area = st.text_area("अपनी स्क्रिप्ट यहाँ लिखें", height=400, placeholder="नमस्ते दोस्तों, आज हम चर्चा करेंगे...", key="input_text")
    if st.button("🗑️ Clear Script"):
        st.session_state.input_text = ""
        st.rerun()

with col2:
    st.markdown("### 🎙️ वॉइस सिलेक्शन")
    
    # 15 प्रीमियम आवाजों का कलेक्शन (हिंदी पर विशेष जोर)
    voice_map = {
        "--- 🇮🇳 शुद्ध हिंदी (Hindi) ---": "hi-IN-MadhurNeural",
        "1. मधुर (Madhur) - दमदार पुरुष": "hi-IN-MadhurNeural",
        "2. स्वर (Swara) - साफ महिला": "hi-IN-SwaraNeural",
        "3. असद (Asad) - भारी आवाज़ (Deep Base)": "ur-PK-AsadNeural",
        "4. उज्मा (Uzma) - शांत महिला": "ur-PK-UzmaNeural",
        "5. प्रभात (Prabhat) - न्यूज़ एंकर स्टाइल": "en-IN-PrabhatNeural",
        "6. नीरजा (Neerja) - सॉफ्ट महिला": "en-IN-NeerjaNeural",
        "7. रवि (Ravi) - दोस्ताना लहजा": "en-IN-RaviNeural",
        
        "--- 🇺🇸 अमेरिकन एक्सेंट (US English) ---": "en-US-GuyNeural",
        "8. क्रिस्टोफर (Christopher) - भारी पुरुष": "en-US-ChristopherNeural",
        "9. गाय (Guy) -
